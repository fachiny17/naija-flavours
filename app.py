from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
import qrcode
import io
from datetime import datetime
import os

from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT

app = Flask(__name__)

# environment variables for production
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'nigerian-restaurant-secret-key-2026')

# SIMPLE DATABASE URL FIX
database_url = os.environ.get('DATABASE_URL')
if database_url and database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)
elif not database_url:
    database_url = 'sqlite:///nigerian_restaurant.db'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///nigerian_restaurant.db').replace('postgres://', 'postgresql://')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    icon = db.Column(db.String(50), nullable=True)
    items = db.relationship('MenuItem', backref='category', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Category {self.name}>'

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    available = db.Column(db.Boolean, default=True)
    is_spicy = db.Column(db.Boolean, default=False)
    is_vegetarian = db.Column(db.Boolean, default=False)
    prep_time = db.Column(db.String(20), nullable=True)
    image_url = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<MenuItem {self.name}>'

# Initialize database - WITH ERROR HANDLING
def init_db():
    try:
        with app.app_context():
            print(f"🔗 Using database URL: {app.config['SQLALCHEMY_DATABASE_URI']}")
            db.create_all()
            print("✅ Database tables created!")
            
            # Add sample data if no categories exist
            if Category.query.count() == 0:
                print("📝 Adding sample data...")
                categories = [
                    Category(name='Soups & Stews', description='Traditional Nigerian soups rich in flavor', icon='🍲'),
                    Category(name='Rice & Grains', description='Rice dishes and grain-based meals', icon='🍚'),
                    Category(name='Proteins & Sides', description='Grilled meats and accompaniments', icon='🍖'),
                    Category(name='Swallow & Fufu', description='Staple Nigerian swallows', icon='🥘'),
                    Category(name='Snacks & Small Chops', description='Nigerian appetizers and street food', icon='🍢'),
                    Category(name='Beverages', description='Refreshing Nigerian drinks', icon='🥤')
                ]
                db.session.add_all(categories)
                db.session.commit()
                
                items = [
                    # Soups & Stews
                    MenuItem(name='Egusi Soup', description='Ground melon seed soup with assorted meat, stockfish, and vegetables. A rich, hearty classic.', 
                            price=3500, category_id=1, is_spicy=True, prep_time='25-30 min'),
                    MenuItem(name='Ogbono Soup', description='Draw soup made from wild mango seeds, served with your choice of protein.', 
                            price=3200, category_id=1, is_spicy=False, prep_time='20-25 min'),
                    MenuItem(name='Efo Riro', description='Yoruba-style vegetable soup with spinach, locust beans, and peppers. Packed with nutrients.', 
                            price=2800, category_id=1, is_spicy=True, is_vegetarian=False, prep_time='20 min'),
                    MenuItem(name='Banga Soup', description='Delta-style palm nut soup with fresh fish and traditional spices.', 
                            price=3800, category_id=1, is_spicy=True, prep_time='30-35 min'),
                    MenuItem(name='Afang Soup', description='Nutritious vegetable soup with waterleaf, afang leaves, and assorted proteins.', 
                            price=4000, category_id=1, is_spicy=False, prep_time='25 min'),
                    
                    # Rice & Grains
                    MenuItem(name='Jollof Rice', description='The iconic Nigerian party rice cooked in a rich tomato base with aromatic spices. Served with plantain and coleslaw.', 
                            price=2500, category_id=2, is_spicy=True, prep_time='15 min'),
                    MenuItem(name='Fried Rice', description='Colorful mixed vegetable rice with liver, shrimp, and chicken. A celebration favorite.', 
                            price=2800, category_id=2, is_spicy=False, prep_time='15 min'),
                    MenuItem(name='Coconut Rice', description='Fragrant rice cooked in coconut milk with vegetables and spices.', 
                            price=2200, category_id=2, is_spicy=False, prep_time='15 min'),
                    MenuItem(name='Ofada Rice with Ayamase', description='Local unpolished rice served with spicy green pepper sauce and assorted meat.', 
                            price=3500, category_id=2, is_spicy=True, prep_time='20 min'),
                    MenuItem(name='Native Jollof (Iwuk Edesi)', description='Traditional palm oil jollof rice from the South-South region.', 
                            price=2800, category_id=2, is_spicy=True, prep_time='18 min'),
                    
                    # Proteins & Sides
                    MenuItem(name='Suya', description='Spicy grilled beef skewers marinated in groundnut spice mix (yaji). A Northern delicacy.', 
                            price=1800, category_id=3, is_spicy=True, prep_time='10 min'),
                    MenuItem(name='Asun', description='Spicy grilled goat meat chopped and peppered to perfection. Yoruba specialty.', 
                            price=3500, category_id=3, is_spicy=True, prep_time='12 min'),
                    MenuItem(name='Gizdodo', description='Gizzard and plantain in a spicy pepper sauce. Crowd favorite!', 
                            price=2200, category_id=3, is_spicy=True, prep_time='15 min'),
                    MenuItem(name='Fried Plantain (Dodo)', description='Sweet ripe plantain sliced and fried to golden perfection.', 
                            price=800, category_id=3, is_spicy=False, is_vegetarian=True, prep_time='10 min'),
                    MenuItem(name='Grilled Chicken', description='Whole chicken marinated and grilled with Nigerian spices.', 
                            price=4500, category_id=3, is_spicy=True, prep_time='15 min'),
                    
                    # Swallow & Fufu
                    MenuItem(name='Pounded Yam', description='Smooth, stretchy yam swallow. The king of all swallows!', 
                            price=1200, category_id=4, is_spicy=False, is_vegetarian=True, prep_time='5 min'),
                    MenuItem(name='Eba (Garri)', description='Classic cassava swallow, perfect with any soup.', 
                            price=500, category_id=4, is_spicy=False, is_vegetarian=True, prep_time='5 min'),
                    MenuItem(name='Fufu (Akpu)', description='Fermented cassava swallow with a distinctive tangy flavor.', 
                            price=800, category_id=4, is_spicy=False, is_vegetarian=True, prep_time='5 min'),
                    MenuItem(name='Amala', description='Dark yam flour swallow, perfectly pairs with ewedu and gbegiri.', 
                            price=700, category_id=4, is_spicy=False, is_vegetarian=True, prep_time='5 min'),
                    MenuItem(name='Semovita', description='Smooth wheat swallow, lighter alternative to pounded yam.', 
                            price=600, category_id=4, is_spicy=False, is_vegetarian=True, prep_time='5 min'),
                    
                    # Snacks & Small Chops
                    MenuItem(name='Puff Puff', description='Sweet deep-fried dough balls, fluffy and golden. Nigerian donuts!', 
                            price=500, category_id=5, is_spicy=False, is_vegetarian=True, prep_time='5 min'),
                    MenuItem(name='Chin Chin', description='Crunchy fried pastry snack, perfect with any drink.', 
                            price=800, category_id=5, is_spicy=False, is_vegetarian=True, prep_time='5 min'),
                    MenuItem(name='Akara (Bean Cake)', description='Fried bean fritters, crispy outside, soft inside. Street food classic!', 
                            price=600, category_id=5, is_spicy=True, is_vegetarian=True, prep_time='10 min'),
                    MenuItem(name='Spring Rolls', description='Crispy vegetable-filled rolls served with sweet chili sauce.', 
                            price=1200, category_id=5, is_spicy=False, is_vegetarian=True, prep_time='8 min'),
                    MenuItem(name='Samosa', description='Spiced meat or vegetable-filled pastry pockets.', 
                            price=1000, category_id=5, is_spicy=True, prep_time='8 min'),
                    
                    # Beverages
                    MenuItem(name='Chapman', description='Sparkling Nigerian cocktail with grenadine, lime, and cucumber. Non-alcoholic.', 
                            price=1000, category_id=6, is_spicy=False, is_vegetarian=True, prep_time='5 min'),
                    MenuItem(name='Zobo', description='Refreshing hibiscus tea infused with ginger and pineapple.', 
                            price=800, category_id=6, is_spicy=False, is_vegetarian=True, prep_time='2 min'),
                    MenuItem(name='Palm Wine', description='Fresh, naturally fermented palm tree sap. Traditional village drink.', 
                            price=1500, category_id=6, is_spicy=False, is_vegetarian=True, prep_time='2 min'),
                    MenuItem(name='Kunnu', description='Spiced millet drink from the North, served chilled.', 
                            price=700, category_id=6, is_spicy=False, is_vegetarian=True, prep_time='2 min'),
                    MenuItem(name='Fresh Fruit Juice', description='Choice of orange, pineapple, watermelon, or mixed.', 
                            price=1200, category_id=6, is_spicy=False, is_vegetarian=True, prep_time='5 min')
                ]
                db.session.add_all(items)
                db.session.commit()
                print("✅ Nigerian restaurant sample data added!")
    except Exception as e:
        print(f"⚠️ Database initialization error: {str(e)}")
        print("⚠️ Continuing without database...")

# Call init_db AFTER all models and routes are defined
init_db()

# Routes (ALL ROUTES REMAIN THE SAME)
@app.route('/')
def index():
    try:
        categories = Category.query.all()
        menu_items = MenuItem.query.filter_by(available=True).all()
    except:
        categories = []
        menu_items = []
    return render_template('index.html', categories=categories, menu_items=menu_items)

@app.route('/menu')
def menu():
    try:
        categories = Category.query.all()
        menu_items = MenuItem.query.filter_by(available=True).all()
    except:
        categories = []
        menu_items = []
    return render_template('menu.html', categories=categories, menu_items=menu_items)

@app.route('/admin')
def admin():
    try:
        categories = Category.query.all()
        menu_items = MenuItem.query.all()
    except:
        categories = []
        menu_items = []
    return render_template('admin.html', categories=categories, menu_items=menu_items)

@app.route('/category/add', methods=['POST'])
def add_category():
    try:
        name = request.form.get('name')
        description = request.form.get('description')
        icon = request.form.get('icon')
        
        if name:
            category = Category(name=name, description=description, icon=icon)
            db.session.add(category)
            db.session.commit()
            flash('Category added successfully!', 'success')
    except Exception as e:
        flash(f'Error adding category: {str(e)}', 'error')
    return redirect(url_for('admin'))

@app.route('/category/delete/<int:id>')
def delete_category(id):
    try:
        category = Category.query.get_or_404(id)
        db.session.delete(category)
        db.session.commit()
        flash('Category deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting category: {str(e)}', 'error')
    return redirect(url_for('admin'))

@app.route('/item/add', methods=['POST'])
def add_item():
    try:
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        category_id = request.form.get('category_id')
        prep_time = request.form.get('prep_time')
        is_spicy = request.form.get('is_spicy') == 'on'
        is_vegetarian = request.form.get('is_vegetarian') == 'on'
        
        if name and price and category_id:
            item = MenuItem(
                name=name,
                description=description,
                price=float(price),
                category_id=int(category_id),
                prep_time=prep_time,
                is_spicy=is_spicy,
                is_vegetarian=is_vegetarian
            )
            db.session.add(item)
            db.session.commit()
            flash('Menu item added successfully!', 'success')
    except Exception as e:
        flash(f'Error adding item: {str(e)}', 'error')
    return redirect(url_for('admin'))

@app.route('/item/toggle/<int:id>')
def toggle_item(id):
    try:
        item = MenuItem.query.get_or_404(id)
        item.available = not item.available
        db.session.commit()
        flash(f'Item {"enabled" if item.available else "disabled"} successfully!', 'success')
    except Exception as e:
        flash(f'Error toggling item: {str(e)}', 'error')
    return redirect(url_for('admin'))

@app.route('/item/delete/<int:id>')
def delete_item(id):
    try:
        item = MenuItem.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        flash('Item deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting item: {str(e)}', 'error')
    return redirect(url_for('admin'))

@app.route('/item/edit/<int:id>', methods=['POST'])
def edit_item(id):
    try:
        item = MenuItem.query.get_or_404(id)
        item.name = request.form.get('name')
        item.description = request.form.get('description')
        item.price = float(request.form.get('price'))
        item.category_id = int(request.form.get('category_id'))
        item.prep_time = request.form.get('prep_time')
        item.is_spicy = request.form.get('is_spicy') == 'on'
        item.is_vegetarian = request.form.get('is_vegetarian') == 'on'
        
        db.session.commit()
        flash('Item updated successfully!', 'success')
    except Exception as e:
        flash(f'Error updating item: {str(e)}', 'error')
    return redirect(url_for('admin'))

# QR Code Generation
@app.route('/qr-code')
def generate_qr():
    # Direct PDF download URL
    pdf_url = request.host_url + 'qr-pdf'
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(pdf_url)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to bytes
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

@app.route('/qr')
def qr_page():
    # Page to display the QR code
    menu_url = request.host_url + 'menu'
    return render_template('qr_page.html', menu_url=menu_url)

@app.route('/qr-pdf')
def qr_pdf_download():
    """Route that directly downloads PDF when accessed via QR code"""
    flash('Thank you for scanning! Downloading menu...', 'success')
    return download_menu_pdf()

@app.route('/download-menu-pdf')
def download_menu_pdf():
    """Generate and download the complete menu as a PDF"""
    
    # Create a buffer to hold the PDF
    buffer = BytesIO()
    
    # Create the PDF document
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=50, leftMargin=50, 
                           topMargin=50, bottomMargin=50)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.HexColor('#008751'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#666666'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    category_style = ParagraphStyle(
        'CategoryStyle',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.HexColor('#008751'),
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    item_name_style = ParagraphStyle(
        'ItemName',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#1a1a1a'),
        fontName='Helvetica-Bold'
    )
    
    item_desc_style = ParagraphStyle(
        'ItemDesc',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#666666'),
        fontName='Helvetica'
    )
    
    # Add title
    title = Paragraph("Naija Flavours Menu", title_style)
    elements.append(title)
    
    # Add subtitle
    subtitle = Paragraph("Authentic Nigerian Cuisine", subtitle_style)
    elements.append(subtitle)
    
    # Add date
    date_text = Paragraph(f"Generated on {datetime.now().strftime('%B %d, %Y')}", 
                         ParagraphStyle('DateStyle', parent=styles['Normal'], 
                                      fontSize=9, textColor=colors.grey, 
                                      alignment=TA_CENTER))
    elements.append(date_text)
    elements.append(Spacer(1, 20))
    
    # Get all categories and items
    categories = Category.query.all()
    
    for category in categories:
        # Get items for this category
        items = MenuItem.query.filter_by(category_id=category.id, available=True).all()
        
        if items:
            # Category header
            cat_name = f"{category.icon} {category.name}" if category.icon else category.name
            cat_header = Paragraph(cat_name, category_style)
            elements.append(cat_header)
            
            if category.description:
                cat_desc = Paragraph(category.description, item_desc_style)
                elements.append(cat_desc)
                elements.append(Spacer(1, 10))
            
            # Create table for items
            table_data = []
            
            for item in items:
                # Item name and price row
                name_cell = Paragraph(item.name, item_name_style)
                price_cell = Paragraph(f"₦{item.price:,.0f}", item_name_style)
                
                # Build tags
                tags = []
                if item.is_spicy:
                    tags.append("🌶️ Spicy")
                if item.is_vegetarian:
                    tags.append("🌱 Vegetarian")
                if item.prep_time:
                    tags.append(f"⏱️ {item.prep_time}")
                
                tags_text = " • ".join(tags) if tags else ""
                
                # Description with tags
                desc_text = item.description if item.description else ""
                if tags_text:
                    desc_text += f"<br/><i>{tags_text}</i>"
                
                desc_cell = Paragraph(desc_text, item_desc_style)
                
                # Add rows
                table_data.append([name_cell, price_cell])
                table_data.append([desc_cell, ''])
                table_data.append([Spacer(1, 8), ''])  # Add spacing between items
            
            # Create and style the table
            item_table = Table(table_data, colWidths=[4.5*inch, 1.5*inch])
            item_table.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                ('TOPPADDING', (0, 0), (-1, -1), 2),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ]))
            
            elements.append(item_table)
            elements.append(Spacer(1, 15))
    
    # Add footer
    elements.append(Spacer(1, 30))
    footer = Paragraph(
        "Thank you for choosing Naija Flavours!<br/>For orders and inquiries, <a href='https://naija-flavours.onrender.com/'><b>visit us online</b></a>.",
        ParagraphStyle('Footer', parent=styles['Normal'], 
                      fontSize=9, textColor=colors.grey, 
                      alignment=TA_CENTER, fontName='Helvetica-Oblique')
    )
    elements.append(footer)
    
    # Build PDF
    doc.build(elements)
    
    # Move buffer position to beginning
    buffer.seek(0)
    
    # Send the PDF
    return send_file(
        buffer,
        as_attachment=True,
        download_name='naija-flavors-menu.pdf',
        mimetype='application/pdf'
    )



# Add a health check endpoint
@app.route('/health')
def health():
    try:
        category_count = Category.query.count()
        return jsonify({
            'status': 'healthy',
            'database': 'connected',
            'categories': category_count,
            'app': 'naija-flavors'
        })
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'database': 'disconnected',
            'error': str(e),
            'app': 'naija-flavors'
        }), 500

@app.route('/init-db')
def init_db_route():
    """Manually initialize database"""
    init_db()
    return "Database initialization attempted. Check logs."

if __name__ == '__main__':
    app.run(debug=True)
# 🍲 Naija Flavours - Professional Nigerian Restaurant Web App

A stunning, production-ready restaurant menu application featuring authentic Nigerian cuisine with professional UI/UX design.

## ✨ Features

### 🎨 Professional Design
- **Authentic Nigerian Aesthetic**: Colors inspired by the Nigerian flag (green, white, gold)
- **Modern Typography**: Playfair Display for headers, DM Sans for body text
- **Smooth Animations**: Fade-ins, hover effects, and micro-interactions
- **Responsive Design**: Perfect on mobile, tablet, and desktop
- **Cultural Elements**: Nigerian-inspired patterns and styling

### 🏠 Landing Page
- Eye-catching hero section with gradient backgrounds
- Animated food category cards
- Feature highlights section
- Statistics showcase
- Smooth scroll navigation

### 📋 Menu Page
- Category-based filtering with smooth transitions
- Beautiful card-based menu items
- Price display in Nigerian Naira (₦)
- Spicy, Vegetarian, and Prep Time badges
- Detailed descriptions for each dish
- Interactive hover effects

### 🔧 Admin Dashboard
- Complete CRUD operations for categories and menu items
- Category management with emoji icons
- Menu item management with:
  - Name, description, price
  - Preparation time
  - Spicy and vegetarian tags
  - Availability toggle
- Professional table view
- Flash message notifications
- Clean, intuitive interface

### 🍽️ Nigerian Cuisine Categories
Pre-loaded with authentic Nigerian dishes:
1. **Soups & Stews**: Egusi, Ogbono, Efo Riro, Banga, Afang
2. **Rice & Grains**: Jollof Rice, Fried Rice, Coconut Rice, Ofada Rice
3. **Proteins & Sides**: Suya, Asun, Gizdodo, Grilled Chicken
4. **Swallow & Fufu**: Pounded Yam, Eba, Fufu, Amala, Semovita
5. **Snacks & Small Chops**: Puff Puff, Chin Chin, Akara, Spring Rolls
6. **Beverages**: Chapman, Zobo, Palm Wine, Kunnu, Fresh Juices

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quick Start

1. **Clone or download the project files**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open in browser**
   - Landing Page: http://127.0.0.1:5000/
   - Menu: http://127.0.0.1:5000/menu
   - Admin Panel: http://127.0.0.1:5000/admin

The app comes pre-loaded with sample Nigerian menu items!

## 📁 Project Structure

```
naija-flavors/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── templates/
│   ├── index.html             # Landing page
│   ├── menu.html              # Menu display page
│   └── admin.html             # Admin dashboard
│
└── nigerian_restaurant.db     # SQLite database (auto-created)
```

## 🎯 Usage Guide

### For Customers (Public View)

**Landing Page**
- Beautiful introduction to the restaurant
- Quick navigation to menu or admin
- Feature highlights and statistics

**Menu Page**
- Browse all dishes or filter by category
- View prices in Nigerian Naira
- See preparation times and dietary tags
- Click category buttons to filter instantly

### For Restaurant Owners (Admin Panel)

**Managing Categories**
1. Enter category name (e.g., "Main Courses")
2. Add an emoji icon (e.g., 🍖)
3. Write a brief description
4. Click "Add Category"
5. Delete categories with the trash icon

**Managing Menu Items**
1. Fill in item details:
   - Name: Dish name
   - Category: Select from dropdown
   - Description: Full description
   - Price: In Naira (₦)
   - Prep Time: e.g., "15-20 min"
   - Tags: Check spicy/vegetarian if applicable
2. Click "Add Menu Item"
3. Toggle availability with play/pause button
4. Delete items with trash icon

## 🎨 Customization

### Change Color Scheme
Edit the CSS variables in each template:
```css
:root {
    --green: #008751;        /* Primary color */
    --orange: #FF6B35;       /* Accent color */
    --gold: #FDB913;         /* Highlight color */
    --cream: #FFF8E7;        /* Background */
}
```

### Add More Sample Data
Edit the `init_db()` function in `app.py` to add more categories or items.

### Modify Typography
Update the Google Fonts import and font-family values:
```css
@import url('https://fonts.googleapis.com/css2?family=Your+Font&display=swap');
```

## 💾 Database Schema

**Category Model**
- id: Integer (Primary Key)
- name: String (Unique)
- description: Text
- icon: String (Emoji)

**MenuItem Model**
- id: Integer (Primary Key)
- name: String
- description: Text
- price: Float
- category_id: Integer (Foreign Key)
- available: Boolean
- is_spicy: Boolean
- is_vegetarian: Boolean
- prep_time: String
- image_url: String
- created_at: DateTime

## 🔒 Security Notes

For production deployment:
1. Change the SECRET_KEY in `app.py`
2. Use environment variables for sensitive data
3. Add authentication for admin panel
4. Use PostgreSQL or MySQL instead of SQLite
5. Enable HTTPS
6. Add rate limiting
7. Implement CSRF protection

## 🚢 Deployment

### Heroku
```bash
# Add Procfile
echo "web: gunicorn app:app" > Procfile

# Add gunicorn to requirements.txt
echo "gunicorn==21.2.0" >> requirements.txt

# Deploy
heroku create your-restaurant-name
git push heroku main
```

### PythonAnywhere / Render / Railway
Follow their Flask deployment guides and ensure:
- requirements.txt is present
- Database is properly configured
- Static files are served correctly

## 🌟 Features Roadmap

Future enhancements:
- [ ] User authentication for admin
- [ ] Image uploads for menu items
- [ ] Online ordering system
- [ ] Table reservation
- [ ] Multiple restaurant locations
- [ ] Multilingual support (Yoruba, Igbo, Hausa)
- [ ] Customer reviews and ratings
- [ ] Email notifications
- [ ] Payment integration
- [ ] Mobile app version

## 🤝 Contributing

Feel free to fork this project and customize it for your own restaurant!

## 📄 License

This project is open source and available for personal and commercial use.

## 🙏 Acknowledgments

- Designed with love for Nigerian cuisine
- Inspired by authentic Nigerian restaurants
- Built with Flask and modern web technologies

---

**Enjoy showcasing authentic Nigerian flavors! 🇳🇬🍲**

For questions or support, refer to Flask documentation at https://flask.palletsprojects.com/
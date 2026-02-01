# 🍲 Naija Flavours - Professional Nigerian Restaurant Web App

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Production-success.svg)

**A modern, production-ready restaurant management system showcasing authentic Nigerian cuisine**

[Live Demo](https://naija-flavours.onrender.com/) • [Report Bug](https://github.com/fachiny17/naija-flavours/issues) • [Request Feature](https://github.com/fachiny17/naija-flavours/issues)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Database Schema](#-database-schema)
- [Deployment](#-deployment)
- [Customization](#-customization)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🌟 Overview

**Naija Flavours** is a sophisticated, full-stack web application built with Flask that celebrates authentic Nigerian cuisine. The platform features a beautifully designed customer-facing menu, comprehensive admin dashboard, and animated backgrounds inspired by traditional Nigerian aesthetics.

This project demonstrates modern web development practices, responsive design principles, and cultural authenticity in digital product design.

### Why Naija Flavors?

- 🎨 **Culturally Authentic Design**: Nigerian flag colors, Adire patterns, and traditional aesthetics
- 🚀 **Production Ready**: Deployed on Render with professional-grade architecture
- 📱 **Fully Responsive**: Optimized for mobile, tablet, and desktop experiences
- ⚡ **Performance Optimized**: CSS-only animations, efficient database queries
- 🔒 **Secure & Scalable**: Built with security best practices and scalability in mind

---

## 🌐 Live Demo

**Experience the application live:**

🔗 **[https://naija-flavours.onrender.com/](https://naija-flavours.onrender.com/)**

### Quick Navigation
- **Home**: Landing page with hero section and features
- **Menu**: Browse 30+ authentic Nigerian dishes with filtering
- **Admin**: Management dashboard (accessible at `/admin`)

> **Note**: The demo may take 30-60 seconds to load on first visit due to Render's free tier spin-down policy.

---

## ✨ Features

### 🎨 Design & User Experience

#### **Animated Backgrounds**
- **Landing Page**: Floating food icons, pulsing spice dots, rotating Adire patterns
- **Menu Page**: Gentle floating elements with breathing gradients
- **Admin Panel**: Professional geometric grid animations
- All animations are GPU-accelerated and performance-optimized

#### **Typography & Colors**
- **Fonts**: Playfair Display (headings) + DM Sans (body)
- **Color Palette**: 
  - Nigerian Green: `#008751`
  - Vibrant Orange: `#FF6B35`
  - Gold Accent: `#FDB913`
  - Warm Cream: `#FFF8E7`

#### **Responsive Design**
- Mobile-first approach
- Breakpoints: 768px (tablet), 1024px (desktop)
- Touch-friendly interface elements
- Optimized images and assets

### 🍽️ Customer Features

- **Dynamic Menu Display**: Category-based organization with smooth filtering
- **Detailed Dish Information**: 
  - Name, description, and price (in Naira ₦)
  - Preparation time estimates
  - Dietary indicators (🌶️ Spicy, 🌱 Vegetarian)
- **Interactive UI**: Hover effects, smooth transitions, card-based layout
- **Search & Filter**: Quick category filtering with visual feedback

### 🔧 Admin Dashboard

- **Category Management**:
  - Add/delete categories with emoji icons
  - Custom descriptions for each category
  - Automatic item count tracking

- **Menu Item Management**:
  - Full CRUD operations (Create, Read, Update, Delete)
  - Toggle item availability without deletion
  - Rich text descriptions
  - Dietary tags and prep time
  - Price management in Naira

- **User Feedback**:
  - Flash message notifications
  - Confirmation dialogs for destructive actions
  - Visual status indicators

### 📊 Pre-loaded Content

**6 Authentic Categories:**
1. 🍲 Soups & Stews
2. 🍚 Rice & Grains  
3. 🍖 Proteins & Sides
4. 🥘 Swallow & Fufu
5. 🍢 Snacks & Small Chops
6. 🥤 Beverages

**30+ Traditional Dishes:**
- Egusi Soup, Jollof Rice, Suya
- Pounded Yam, Asun, Chapman
- And many more Nigerian favorites!

---

## 🛠️ Tech Stack

### Backend
- **Framework**: Flask 3.0.0
- **ORM**: Flask-SQLAlchemy 3.1.1
- **Database**: SQLite (development), PostgreSQL (production-ready)
- **Language**: Python 3.8+

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Custom animations, Grid, Flexbox
- **JavaScript**: Vanilla JS for filtering and interactions
- **Fonts**: Google Fonts (Playfair Display, DM Sans)

### Infrastructure
- **Hosting**: Render (Platform as a Service)
- **Version Control**: Git
- **Package Management**: pip

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning)
- Virtual environment (recommended)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/naija-flavors.git
   cd naija-flavors
   ```

2. **Create virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python app.py
   ```
   This will:
   - Create `nigerian_restaurant.db`
   - Set up all tables
   - Populate with sample Nigerian dishes

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open browser to: `http://127.0.0.1:5000/`
   - Landing Page: `http://127.0.0.1:5000/`
   - Menu: `http://127.0.0.1:5000/menu`
   - Admin: `http://127.0.0.1:5000/admin`

---

## 📖 Usage

### For Restaurant Owners

#### Managing Categories
1. Navigate to `/admin`
2. Scroll to "Manage Categories" section
3. Fill in category details:
   - **Name**: Category name (e.g., "Main Courses")
   - **Icon**: Single emoji (e.g., 🍖)
   - **Description**: Brief category description
4. Click "Add Category"
5. Delete categories using the trash icon (⚠️ deletes all items in category)

#### Managing Menu Items
1. Navigate to `/admin`
2. Scroll to "Manage Menu Items" section
3. Complete the form:
   - **Name**: Dish name
   - **Category**: Select from dropdown
   - **Description**: Detailed dish description
   - **Price**: Amount in Naira (₦)
   - **Prep Time**: e.g., "15-20 min"
   - **Tags**: Check Spicy/Vegetarian as applicable
4. Click "Add Menu Item"
5. Use action buttons:
   - ⏸️/▶️ Toggle availability
   - 🗑️ Delete permanently

### For Customers

#### Browsing the Menu
1. Visit the homepage
2. Click "Explore Menu" or navigate to `/menu`
3. Use category filters to browse specific sections
4. View dish details, prices, and dietary information
5. Note preparation times for ordering

---

## 💾 Database Schema

### Category Table
```python
class Category(db.Model):
    id              Integer (Primary Key)
    name            String(50) (Unique, Not Null)
    description     Text
    icon            String(50) (Emoji)
    items           Relationship → MenuItem
```

### MenuItem Table
```python
class MenuItem(db.Model):
    id              Integer (Primary Key)
    name            String(100) (Not Null)
    description     Text
    price           Float (Not Null)
    category_id     Integer (Foreign Key → Category)
    available       Boolean (Default: True)
    is_spicy        Boolean (Default: False)
    is_vegetarian   Boolean (Default: False)
    prep_time       String(20)
    image_url       String(200)
    created_at      DateTime (Default: UTC Now)
```

### Relationships
- One-to-Many: Category → MenuItems
- Cascade Delete: Deleting a category removes all its items

---

## 🌍 Deployment

### Deployed on Render

**Live URL**: [https://naija-flavours.onrender.com/](https://naija-flavours.onrender.com/)

#### Render Configuration

**Build Command**:
```bash
pip install -r requirements.txt
```

**Start Command**:
```bash
gunicorn app:app
```

#### Environment Variables
```env
PYTHON_VERSION=3.11.0
SECRET_KEY=your-production-secret-key
DATABASE_URL=your-database-url (optional for PostgreSQL)
```

### Deploy to Other Platforms

#### Heroku
```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
heroku create naija-flavors
git push heroku main
heroku open
```

#### PythonAnywhere
1. Upload files via "Files" tab
2. Create virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Configure WSGI file to point to `app.py`
5. Reload web app

#### Railway
1. Connect GitHub repository
2. Railway auto-detects Flask
3. Add environment variables
4. Deploy automatically on git push

---

## 🎨 Customization

### Color Scheme

Edit CSS variables in any template file:

```css
:root {
    --green: #008751;        /* Primary brand color */
    --orange: #FF6B35;       /* Accent color */
    --gold: #FDB913;         /* Highlight color */
    --cream: #FFF8E7;        /* Background color */
    --text-dark: #1a1a1a;    /* Primary text */
    --text-light: #666;      /* Secondary text */
}
```

### Typography

Replace Google Fonts import:

```html
<link href="https://fonts.googleapis.com/css2?family=Your+Font:wght@400;700&display=swap" rel="stylesheet">
```

Update CSS:
```css
body {
    font-family: 'Your Font', sans-serif;
}
```

### Adding More Sample Data

Edit `app.py` in the `init_db()` function:

```python
items = [
    MenuItem(
        name='New Dish Name',
        description='Detailed description',
        price=2500,
        category_id=1,
        is_spicy=True,
        prep_time='20 min'
    ),
    # Add more items...
]
```

### Logo & Branding

Replace the logo text in navigation:

```html
<div class="logo">Your Restaurant Name</div>
```

---

## 🔌 API Reference

While this application primarily uses server-side rendering, here are the available routes:

### Public Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Landing page |
| GET | `/menu` | Menu display page |
| GET | `/admin` | Admin dashboard |

### Category Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/category/add` | Create new category |
| GET | `/category/delete/<id>` | Delete category |

### Menu Item Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/item/add` | Create new menu item |
| POST | `/item/edit/<id>` | Update menu item |
| GET | `/item/toggle/<id>` | Toggle availability |
| GET | `/item/delete/<id>` | Delete menu item |

---

## 🔒 Security Considerations

### For Production Deployment

1. **Change Secret Key**
   ```python
   app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-key')
   ```

2. **Use Environment Variables**
   ```python
   import os
   DATABASE_URL = os.environ.get('DATABASE_URL')
   ```

3. **Enable HTTPS**
   - Render provides automatic HTTPS
   - Force HTTPS redirects in production

4. **Add Authentication**
   - Implement Flask-Login for admin panel
   - Use password hashing (bcrypt)
   - Add CSRF protection

5. **Input Validation**
   - Sanitize all user inputs
   - Use Flask-WTF for forms
   - Implement rate limiting

6. **Database Security**
   - Use PostgreSQL in production
   - Regular backups
   - Parameterized queries (SQLAlchemy handles this)

---

## 🗺️ Roadmap

### Planned Features

- [ ] **User Authentication**: Secure admin login system
- [ ] **Image Upload**: Add dish photos
- [ ] **Online Ordering**: Shopping cart and checkout
- [ ] **Payment Integration**: Paystack/Flutterwave
- [ ] **Table Reservation**: Booking system
- [ ] **Multi-language**: Yoruba, Igbo, Hausa support
- [ ] **Customer Reviews**: Rating and feedback system
- [ ] **Email Notifications**: Order confirmations
- [ ] **Analytics Dashboard**: Sales and traffic metrics
- [ ] **Mobile App**: React Native version
- [ ] **QR Code Menu**: Digital menu for dine-in
- [ ] **Loyalty Program**: Customer rewards

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Bugs

1. Check existing issues first
2. Create detailed bug report with:
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - Environment details

### Suggesting Features

1. Open an issue with "Feature Request" label
2. Describe the feature and use case
3. Explain why it would benefit the project

### Pull Requests

1. Fork the repository
2. Create feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m 'Add AmazingFeature'`
4. Push to branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Test thoroughly before submitting

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 Naija Flavors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 👨‍💻 Author & Contact

**Project Maintainer**: Your Name

- 💼 LinkedIn: [linkedin.com/in/fachiny17](https://linkedin.com/in/fachiny17)
- 📱 GitHub: [@fachiny17](https://github.com/fachiny17)

---

## 🙏 Acknowledgments

- **Nigerian Cuisine**: Inspired by authentic recipes and traditional cooking methods
- **Design Inspiration**: Adire textile patterns, Nigerian flag colors
- **Flask Community**: Excellent documentation and support
- **Render Platform**: Reliable hosting and deployment
- **Google Fonts**: Beautiful typography (Playfair Display, DM Sans)
- **Contributors**: Thanks to everyone who has contributed to this project

---


## 💡 Support

If you find this project helpful, consider:

- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features

---

<div align="center">

**Built with ❤️ for Nigerian cuisine lovers worldwide**

🍲 **[View Live Demo](https://naija-flavours.onrender.com/)** 🍲

© 2026 Naija Flavors. All Rights Reserved.

</div>
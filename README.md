# Fitness Web Application (Django)

This is a simple fitness web application built using Django.  
It includes multiple pages, a contact system, login authentication, and a dynamic SEO system for each page.

The project is designed for learning Django and building a real-world structured website.

---

## Project Overview

This fitness web application provides:

- Static fitness pages (Home, About, Programs, Support)
- Contact form with database storage
- User login system with authentication
- Dynamic SEO management for every page

Each page loads SEO data dynamically from the database using a page name.

---

## Features

### 1. Pages
The website includes the following pages:

- Home
- About
- Programs
- Support
- Contact
- Login

Each page is rendered using Django templates.

---

### 2. SEO System

The SEO system is handled using a database model.

Each page has its own SEO record stored in the database.

#### SEO Fields:
- Page name (unique identifier)
- Title (meta title)
- Meta description
- Keywords
- Canonical URL (optional)

#### How it works:
- Each view fetches SEO using:
  - `SEO.objects.filter(page_name="page_name").first()`
- SEO data is passed to templates dynamically

---

### 3. Contact System

Users can submit messages through the contact form.

#### Contact Fields:
- Name
- Email
- WhatsApp number
- Message
- Image upload (optional)

#### Functionality:
- Data is saved in database using Contact model
- Supports image upload stored in media folder
- Returns JSON response after successful submission:
  - "Your message has been sent successfully!"

---

### 4. Login System

The application includes user authentication using Django.

#### Features:
- Login using username and password
- Uses Django `authenticate()` and `login()`
- Displays error messages using Django messages framework
- Redirects authenticated users to premium page
- premium page where nutraion plan and exercise plane shared by coach to each user
- If user is already logged in → redirects automatically

---

## How It Works

### SEO Loading
Each page loads SEO like this:
```python
SEO.objects.filter(page_name='home').first()
Build A fitness Web App

### to clone?
git clone https://github.com/your-username/fitness-web-app.git
pip install django
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser

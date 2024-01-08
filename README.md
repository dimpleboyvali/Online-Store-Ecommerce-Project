# Online Store E-commerce Project

## Overview

The Online Store E-commerce Project is a web application built using DJANGO that allows users to browse products, add them to the cart. This project aims to provide a comprehensive and user-friendly experience.

## Features

- **Product Catalog:**
  - Display a wide range of products with details such as images, descriptions, and prices.

- **User Authentication:**
  - Allow users to create accounts, log in, and manage their profiles.

- **Shopping Cart:**
  - Enable users to add products to the cart, view the cart contents.

- **Admin Dashboard:**
  - Include an admin interface to manage products, view orders, and handle user accounts.

## Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/banothjalandhar/Online-Store-Ecommerce-Project.git
cd online-store-ecommerce

2. Create a Virtual Environment
```bash
python -m venv venv

3. Activate the Virtual Environment
On Windows:

```bash
.\venv\Scripts\activate

5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate

6. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser

7. Start the Development Server
```bash
python manage.py runserver

8. Access the Application
Visit http://localhost:8000 in your web browser.

Usage
Browse the product catalog and select items to add to your cart.
Admins can log in to the admin dashboard at http://localhost:8000/admin to manage products and orders.

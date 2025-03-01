![Alt text](./abc.png)
![Alt text](./abcd.png)

# Django E-commerce Project 🛒


A simple e-commerce application built with Django, featuring product listings, search functionality, a cart system using localStorage, and a checkout page for order review and shipping details.

## Features

- **Product Listing:** Browse and paginate products.
- **Search:** Search products by title and description.
- **Cart System:** Add/remove products to/from the cart, stored in localStorage.
- **Checkout:** Review cart items, calculate the total, and submit shipping details.

## Tech Stack
- **Backend:** Django 5.1.1
- **Frontend:** HTML, Bootstrap 4.3, jQuery 3.4.1
- **Database:** SQLite (easily configurable to use PostgreSQL, MySQL, etc.)
- **Image Processing:** Pillow

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   
2.Create a virtual environment:
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

3.Install dependencies:
pip install -r requirements.txt

4.Set up the database:
python manage.py migrate

5.Create a superuser to access the admin panel:
python manage.py createsuperuser

6.Run the development server:
python manage.py runserver

7.Access the application at http://127.0.0.1:8000/.
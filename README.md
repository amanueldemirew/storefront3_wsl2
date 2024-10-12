E-commerce Backend with Django
This project is an e-commerce backend built with Django and Django REST Framework (DRF). It includes unit tests, performance tests, and is set up for production-grade deployment using Redis.

Features
Product Management: CRUD operations for products, including images and reviews.
Collection Management: Manage product collections.
Cart Management: Persistent shopping cart functionality.
Customer Management: Manage customer information.
Order Management: Handle order creation and tracking.
Unit and Performance Testing: Comprehensive tests to ensure code quality and performance.
Installation
Prerequisites
Python 3.8+
Django 3.2+
Django REST Framework
Redis
Docker (for deployment)
Setup
Clone the repository:
git clone https://github.com/yourusername/ecommerce-backend.git
cd ecommerce-backend

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Run the development server:
python manage.py runserver

Create a superuser:
python manage.py createsuperuser

API Endpoints
The API uses DRF’s router system for endpoint management. Below are the main endpoints:

Python

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
products_router.register('images', views.ProductImageViewSet, basename='product-images')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')
AI-generated code. Review and use carefully. More info on FAQ.
Testing
Unit Tests
Run unit tests with:

python manage.py test

Performance Tests
Use a tool like Locust or JMeter for performance testing. Example with Locust:

locust -f locustfile.py

Deployment
Settings Configuration
The project uses separate settings files for different environments: common.py, dev.py, and prod.py.

Using Redis
Ensure Redis is installed and running. Update your settings to use Redis for caching and session management.

Vercel Deployment
Deploy the project to Vercel using the following URL: storefront3-wsl2.vercel.app

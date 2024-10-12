# E-commerce Backend with Django

This project is an e-commerce backend built with Django and Django REST Framework (DRF). It includes unit tests, performance tests, and is set up for production-grade deployment using Redis and Celery.

## Features

- **Product Management**: CRUD operations for products, including images and reviews.
- **Collection Management**: Manage product collections.
- **Cart Management**: Persistent shopping cart functionality.
- **Customer Management**: Manage customer information.
- **Order Management**: Handle order creation and tracking.
- **Unit and Performance Testing**: Comprehensive tests to ensure code quality and performance.
- **Background Tasks**: Asynchronous task processing using Celery.

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST Framework
- Redis
- Celery
- Docker (for deployment)

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ecommerce-backend.git
    cd ecommerce-backend
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

## Models System

### Product Model

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```

### Collection Model

```python
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self):
        return self.title
```

### Cart Model

```python
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = [['cart', 'product']]
```

### Customer Model

```python
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.user.username
```

### Order Model

```python
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')])

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
```

## API Endpoints

The API uses DRF's router system for endpoint management. Below are the main endpoints:

```python
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
```

## Testing

### Unit Tests

Unit tests are essential for ensuring the correctness of your code. Run unit tests with:
```bash
python manage.py test
```

### Performance Tests

Use a tool like Locust or JMeter for performance testing. Example with Locust:
```bash
locust -f locustfile.py
```

## Background Tasks with Celery

Celery is used for handling asynchronous tasks such as sending emails, processing orders, etc.

### Setup Celery

1. **Install Celery**:
    ```bash
    pip install celery
    ```

2. **Configure Celery in your Django project**:
    ```python
    # settings.py
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    ```

3. **Create a `celery.py` file in your project directory**:
    ```python
    from __future__ import absolute_import, unicode_literals
    import os
    from celery import Celery

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

    app = Celery('your_project')
    app.config_from_object('django.conf:settings', namespace='CELERY')
    app.autodiscover_tasks()
    ```

4. **Define tasks in your Django apps**:
    ```python
    # tasks.py
    from celery import shared_task

    @shared_task
    def example_task():
        print("Task executed")
    ```

5. **Run Celery worker**:
    ```bash
    celery -A your_project worker --loglevel=info
    ```

## Deployment

### Settings Configuration

The project uses separate settings files for different environments: `common.py`, `dev.py`, and `prod.py`.

### Using Redis

Ensure Redis is installed and running. Update your settings to use Redis for caching and session management.

### Vercel Deployment

Deploy the project to Vercel using the following URL: [storefront3-wsl2.vercel.app](https://storefront3-wsl2.vercel.app)

### Environment Variables

Ensure the `DJANGO_SETTINGS_MODULE` environment variable is set during deployment. For example:
```bash
export DJANGO_SETTINGS_MODULE=your_project.settings.prod
```


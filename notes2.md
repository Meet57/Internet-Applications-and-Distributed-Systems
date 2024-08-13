
### 1. **Basic Query**
   - **Retrieve all objects from a model:**
     ```python
     all_objects = ModelName.objects.all()
     ```

### 2. **Filtering Data**
   - **Filter objects based on a condition:**
     ```python
     filtered_objects = ModelName.objects.filter(field_name='value')
     ```

   - **Filter using multiple conditions (AND):**
     ```python
     filtered_objects = ModelName.objects.filter(field_name='value', another_field='another_value')
     ```

   - **Filter using multiple conditions (OR):**
     ```python
     from django.db.models import Q
     filtered_objects = ModelName.objects.filter(Q(field_name='value') | Q(another_field='another_value'))
     ```

### 3. **Excluding Data**
   - **Exclude certain objects from the result:**
     ```python
     excluded_objects = ModelName.objects.exclude(field_name='value')
     ```

### 4. **Field Lookups**
   - **Retrieve objects where a field contains a certain substring:**
     ```python
     contains_objects = ModelName.objects.filter(field_name__contains='substring')
     ```

   - **Retrieve objects where a field starts with a certain value:**
     ```python
     startswith_objects = ModelName.objects.filter(field_name__startswith='value')
     ```

   - **Retrieve objects where a field is greater than a certain value:**
     ```python
     greater_than_objects = ModelName.objects.filter(field_name__gt=10)
     ```

   - **Retrieve objects where a field is in a list of values:**
     ```python
     in_list_objects = ModelName.objects.filter(field_name__in=[1, 2, 3, 4])
     ```

### 5. **Ordering Data**
   - **Order objects by a field:**
     ```python
     ordered_objects = ModelName.objects.order_by('field_name')
     ```

   - **Order objects in descending order:**
     ```python
     ordered_objects_desc = ModelName.objects.order_by('-field_name')
     ```

### 6. **Aggregating Data**
   - **Count the number of objects:**
     ```python
     from django.db.models import Count
     count = ModelName.objects.count()
     ```

   - **Calculate the sum of a field:**
     ```python
     from django.db.models import Sum
     total_sum = ModelName.objects.aggregate(Sum('field_name'))
     ```

### 7. **Related Models**
   - **Retrieve related objects using foreign keys:**
     ```python
     related_objects = RelatedModel.objects.filter(foreign_key_field__field_name='value')
     ```

   - **Prefetch related objects to minimize database queries:**
     ```python
     objects_with_related = ModelName.objects.prefetch_related('related_model_name').all()
     ```

### 8. **Updating Data**
   - **Update a field for all objects:**
     ```python
     ModelName.objects.update(field_name='new_value')
     ```

   - **Update specific objects:**
     ```python
     ModelName.objects.filter(field_name='value').update(another_field='new_value')
     ```

### 9. **Deleting Data**
   - **Delete specific objects:**
     ```python
     ModelName.objects.filter(field_name='value').delete()
     ```

   - **Delete all objects:**
     ```python
     ModelName.objects.all().delete()
     ```

### 10. **Raw SQL Queries**
   - **Execute raw SQL queries:**
     ```python
     results = ModelName.objects.raw('SELECT * FROM appname_modelname WHERE field_name = %s', ['value'])
     ```



Here are Django ORM queries for creating, updating, deleting objects, and handling foreign key relationships:

### 1. **Create a New Object**

   - **Create a single object:**
     ```python
     new_object = ModelName.objects.create(field_name='value', another_field='another_value')
     ```

   - **Alternative way to create an object (using `.save()`):**
     ```python
     new_object = ModelName(field_name='value', another_field='another_value')
     new_object.save()
     ```

### 2. **Delete an Object**

   - **Delete a specific object:**
     ```python
     object_to_delete = ModelName.objects.get(id=1)
     object_to_delete.delete()
     ```

   - **Delete multiple objects based on a condition:**
     ```python
     ModelName.objects.filter(field_name='value').delete()
     ```

   - **Delete all objects:**
     ```python
     ModelName.objects.all().delete()
     ```

### 3. **Handling ForeignKey Relationships**

   Assuming you have two models, `Author` and `Book`, where `Book` has a ForeignKey to `Author`:

   ```python
   class Author(models.Model):
       name = models.CharField(max_length=100)

   class Book(models.Model):
       title = models.CharField(max_length=100)
       author = models.ForeignKey(Author, on_delete=models.CASCADE)
   ```

   - **Create a `Book` object associated with an `Author`:**
     ```python
     author = Author.objects.get(id=1)
     new_book = Book.objects.create(title='New Book Title', author=author)
     ```

   - **Retrieve all books by a specific author:**
     ```python
     books_by_author = Book.objects.filter(author=author)
     ```

   - **Access the related `Author` of a `Book`:**
     ```python
     book = Book.objects.get(id=1)
     book_author = book.author
     ```

   - **Access all `Books` for a specific `Author`:**
     ```python
     author = Author.objects.get(id=1)
     books = author.book_set.all()  # This uses the related name `book_set` automatically
     ```

### 4. **Update an Object**

   - **Update a specific object's field:**
     ```python
     object_to_update = ModelName.objects.get(id=1)
     object_to_update.field_name = 'new_value'
     object_to_update.save()
     ```

   - **Update multiple objects at once:**
     ```python
     ModelName.objects.filter(field_name='value').update(another_field='new_value')
     ```

   - **Update an object with a foreign key:**
     ```python
     author = Author.objects.get(id=2)
     book_to_update = Book.objects.get(id=1)
     book_to_update.author = author
     book_to_update.save()
     ```


Certainly! Here's an example of a Django project that includes a `Model`, a `Form`, and a `View` to handle input fields like name, email, and phone number, along with other typical fields.

### 1. **Model**

First, define a model to store the data. The model will include fields for name, email, phone number, and any other fields you'd like to include.

```python
# models.py

from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
```

### 2. **Form**

Create a form to handle user input. This form will include fields corresponding to the model fields.

```python
# forms.py

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message'}),
        }
```

### 3. **View**

Create a view to handle the form submission and rendering.

```python
# views.py

from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')
```

### 4. **Template**

Create a template to render the form. This will be a basic HTML form that Django will populate with the form fields.

```html
<!-- templates/contact_form.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

### 5. **URL Configuration**

Finally, map the view to a URL in your `urls.py`.

```python
# urls.py

from django.urls import path
from .views import contact_view, success_view

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
]
```

### 6. **Success Template**

Create a simple template to display after a successful form submission.

```html
<!-- templates/success.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
</head>
<body>
    <h1>Thank you for your submission!</h1>
    <p>We will get back to you shortly.</p>
</body>
</html>
```

### Summary

- **Model (`Contact`)**: Stores data like name, email, phone number, etc.
- **Form (`ContactForm`)**: Handles form rendering and validation.
- **View (`contact_view`)**: Manages form display and processing.
- **Template (`contact_form.html`)**: Displays the form to the user.
- **URL Configuration**: Maps the view to a URL for access.



---

Here are some notes on setting up basic authentication in a Django project, covering the `Model`, `View`, and `Template` components:

### 1. **Model: User Authentication**

For basic authentication, Django uses its built-in `User` model, which is part of `django.contrib.auth`. This model includes fields like username, password, email, and more.

- **No Custom Model Needed**: Django's default `User` model already includes the necessary fields for basic authentication. If you want to extend the user model with additional fields, you can create a custom user model by inheriting from `AbstractUser`.

### 2. **Views for Authentication**

Django provides built-in views for common authentication tasks such as login, logout, and password management.

#### a. **Login View**

- **Using Built-in View**:
  Django provides a built-in login view (`LoginView`) that can be used out of the box.
  ```python
  # urls.py

  from django.urls import path
  from django.contrib.auth import views as auth_views

  urlpatterns = [
      path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  ]
  ```

- **Custom Login View** (if additional logic is required):
  ```python
  # views.py

  from django.contrib.auth import authenticate, login
  from django.shortcuts import render, redirect

  def custom_login_view(request):
      if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(request, username=username, password=password)
          if user is not None:
              login(request, user)
              return redirect('home')  # Redirect to a success page
          else:
              return render(request, 'login.html', {'error': 'Invalid credentials'})
      else:
          return render(request, 'login.html')
  ```

#### b. **Logout View**

- **Using Built-in View**:
  Django also provides a built-in logout view (`LogoutView`).
  ```python
  # urls.py

  urlpatterns = [
      path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  ]
  ```

#### c. **Registration View**

- **Custom Registration View**:
  To register new users, you'll typically create a custom view.
  ```python
  # views.py

  from django.contrib.auth.models import User
  from django.contrib.auth.forms import UserCreationForm
  from django.shortcuts import render, redirect

  def register_view(request):
      if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('login')  # Redirect to login page after successful registration
      else:
          form = UserCreationForm()
      return render(request, 'register.html', {'form': form})
  ```

- **URL Configuration**:
  ```python
  # urls.py

  urlpatterns = [
      path('register/', register_view, name='register'),
  ]
  ```

### 3. **Templates**

Templates are used to render the HTML for the authentication views.

#### a. **Login Template**

- **login.html**:
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Login</title>
  </head>
  <body>
      <h2>Login</h2>
      {% if error %}
          <p style="color:red;">{{ error }}</p>
      {% endif %}
      <form method="post">
          {% csrf_token %}
          <label for="username">Username:</label>
          <input type="text" id="username" name="username" required>
          <br>
          <label for="password">Password:</label>
          <input type="password" id="password" name="password" required>
          <br>
          <button type="submit">Login</button>
      </form>
      <p>Don't have an account? <a href="{% url 'register' %}">Register here</a>.</p>
  </body>
  </html>
  ```

#### b. **Registration Template**

- **register.html**:
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Register</title>
  </head>
  <body>
      <h2>Register</h2>
      <form method="post">
          {% csrf_token %}
          {{ form.as_p }}
          <button type="submit">Register</button>
      </form>
      <p>Already have an account? <a href="{% url 'login' %}">Login here</a>.</p>
  </body>
  </html>
  ```

#### c. **Logout Confirmation (Optional)**

- **logout.html** (Optional):
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Logout</title>
  </head>
  <body>
      <h2>Are you sure you want to logout?</h2>
      <form method="post">
          {% csrf_token %}
          <button type="submit">Logout</button>
      </form>
  </body>
  </html>
  ```

### Summary

- **Model**: No need for a custom model if using Django’s built-in `User` model. If extending, use `AbstractUser`.
- **Views**:
  - **Login**: Use `auth_views.LoginView` or create a custom login view.
  - **Logout**: Use `auth_views.LogoutView`.
  - **Register**: Create a custom view using `UserCreationForm`.
- **Templates**:
  - **login.html**: For the login page.
  - **register.html**: For the registration page.
  - **logout.html**: (Optional) For logout confirmation.


---

### **Sessions and Cookies in Django**

Django uses sessions and cookies to maintain state and store information across requests from the same user. Understanding how these work is crucial for implementing features like user authentication, shopping carts, and user preferences.

#### **1. Cookies**

**What are Cookies?**
- **Definition**: A cookie is a small piece of data sent from a server and stored on the user's computer by the user's web browser.
- **Usage**: Cookies are used to identify users and store user preferences, sessions, and other data between requests.

**How Django Uses Cookies:**
- Django automatically sends a cookie to the browser to store the session ID, which is used to identify the session on the server side.
- Cookies can be accessed and set manually in Django using the `HttpResponse` object.

**Setting a Cookie in Django:**
```python
# views.py

from django.http import HttpResponse

def set_cookie_view(request):
    response = HttpResponse("Setting a cookie")
    response.set_cookie('my_cookie', 'cookie_value', max_age=3600)  # Cookie expires in 1 hour
    return response
```

**Accessing a Cookie in Django:**
```python
# views.py

def get_cookie_view(request):
    cookie_value = request.COOKIES.get('my_cookie')
    return HttpResponse(f'The value of the cookie is: {cookie_value}')
```

**Deleting a Cookie:**
```python
# views.py

def delete_cookie_view(request):
    response = HttpResponse("Deleting a cookie")
    response.delete_cookie('my_cookie')
    return response
```

#### **2. Sessions**

**What are Sessions?**
- **Definition**: A session allows you to store data across requests from the same user without requiring them to re-authenticate or provide the same information again.
- **Usage**: Sessions are commonly used to maintain user login states, shopping carts, or other user-specific data.

**How Django Uses Sessions:**
- Django stores session data on the server side and uses a cookie (typically named `sessionid`) to store the session ID on the client side.
- When a user makes a request, Django retrieves the session data using the session ID stored in the cookie.

**Enabling Sessions in Django:**
- Sessions are enabled by default in Django when `django.contrib.sessions` is included in `INSTALLED_APPS` and middleware.

**Working with Sessions in Django:**

**Setting Session Data:**
```python
# views.py

def set_session_view(request):
    request.session['user_name'] = 'John Doe'
    request.session['user_email'] = 'john@example.com'
    return HttpResponse("Session data set")
```

**Accessing Session Data:**
```python
# views.py

def get_session_view(request):
    user_name = request.session.get('user_name', 'Guest')
    user_email = request.session.get('user_email', 'No email set')
    return HttpResponse(f'User: {user_name}, Email: {user_email}')
```

**Deleting Session Data:**
```python
# views.py

def delete_session_view(request):
    try:
        del request.session['user_name']
        del request.session['user_email']
    except KeyError:
        pass
    return HttpResponse("Session data cleared")
```

**Session Expiry:**
- You can set session expiry time either globally in `settings.py` or for individual sessions.
- **Globally**: Set `SESSION_COOKIE_AGE` in `settings.py` to define the default expiry time (in seconds).
- **Individually**: Use `request.session.set_expiry(value)` where `value` is in seconds.

**Example:**
```python
request.session.set_expiry(300)  # Session expires in 5 minutes
```

#### **3. Session Backends**

Django supports different session backends to store session data:

1. **Database-backed sessions** (default): Stores session data in the database.
2. **Cached sessions**: Stores session data in the cache.
3. **File-based sessions**: Stores session data in the filesystem.
4. **Cookie-based sessions**: Stores session data directly in the client's cookie (useful for small, non-sensitive data).

**Setting the Session Backend:**
- In `settings.py`, set the `SESSION_ENGINE` to the desired backend.

**Examples:**
```python
# Database-backed sessions (default)
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Cached sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# File-based sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.file'

# Cookie-based sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
```

#### **4. Security Considerations**

- **Secure Cookies**: Use `SESSION_COOKIE_SECURE = True` to ensure cookies are only sent over HTTPS.
- **HTTPOnly Cookies**: Use `SESSION_COOKIE_HTTPONLY = True` to prevent JavaScript access to cookies.
- **Session Timeout**: Implement session timeouts to automatically log users out after inactivity.

#### **5. Example: Using Sessions and Cookies Together**

You can use both sessions and cookies in tandem. For example, you might store a user's preferred language in a cookie while keeping their authentication state in the session.

```python
# views.py

def language_preference_view(request):
    # Set a cookie for the user's language preference
    response = HttpResponse("Language preference set")
    response.set_cookie('preferred_language', 'en', max_age=31536000)  # 1 year
    return response

def user_dashboard_view(request):
    # Use session for user authentication
    if not request.session.get('user_authenticated'):
        return redirect('login')
    preferred_language = request.COOKIES.get('preferred_language', 'en')
    return HttpResponse(f'Welcome! Preferred Language: {preferred_language}')
```

### **Summary**

- **Cookies**: Small pieces of data stored on the client-side, often used for storing non-sensitive data like preferences.
- **Sessions**: Server-side storage used to maintain state across user requests, commonly for authentication, shopping carts, etc.
- **Security**: Important to secure both sessions and cookies, especially in production environments.

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


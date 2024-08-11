from django import forms
from myapp.models import Order, Review

class FeedbackForm(forms.Form):
    FEEDBACK_CHOICES = [
        ('B', 'Borrow'),
        ('P', 'Purchase'),
    ]
    feedback = forms.MultipleChoiceField(choices=FEEDBACK_CHOICES, widget=forms.CheckboxSelectMultiple())

class SearchForm(forms.Form):
    name = forms.CharField(required=False, label='Your Name')
    CATEGORY_CHOICES = [
        ('F', 'Fiction'),
        ('NF', 'Non-Fiction'),
        ('S', 'Science'),
        ('B', 'Biography'),
        # Add more categories as needed
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False, widget=forms.RadioSelect, label='Select a category:')
    max_price = forms.IntegerField(min_value=1, label='Maximum Price')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['books', 'member', 'order_type']
        widgets = {
            'books': forms.CheckboxSelectMultiple(),
            'order_type': forms.RadioSelect
        }
        labels = {
            'member': 'Member name',
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer', 'book', 'rating', 'comments']
        widgets = {
            'book': forms.RadioSelect(),
        }
        labels = {
            'reviewer': 'Please enter a valid email',
            'rating': 'Rating: An integer between 1 (worst) and 5 (best)',
        }
import datetime
import random

from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Publisher, Order, Member
from django.http import HttpResponse
from .forms import FeedbackForm, SearchForm, OrderForm, ReviewForm, Review
from django.db.models import Avg
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    message = None
    booklist = Book.objects.all().order_by('id')[:10]
    last_login = request.session.get('last_login')
    if last_login:
        message = f'Your last login was at {last_login}'
    return render(request, 'myapp/index0.html', {'booklist': booklist, 'message': message})

def setcookie(request):
    if 'counter' not in request.session or request.session['counter'] == 3:
        request.session['counter'] = 0
    request.session['counter'] += 1

    response = render(request, 'myapp/setcookie.html', {'counter': request.session['counter']})
    response.set_cookie('cookie1', 50, max_age=5)
    response.set_cookie('cookie2', 50, max_age=5)
    return response

def about(request):
    if 'lucky_num' in request.COOKIES:
        mynum = request.COOKIES['lucky_num']
    else:
        mynum = random.randint(1, 100)
    response = render(request, 'myapp/about0.html', {'mynum': mynum})
    response.set_cookie('lucky_num', mynum, max_age=300)  # Expires after 5 minutes
    return response


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # book details
    context = {
        'book': book,
        'title': book.title.upper(),
        'price': f"${book.price}",
        'publisher': book.publisher.name,
        'num_pages': book.num_pages
    }
    return render(request, 'myapp/detail0.html', context)



def getFeedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.cleaned_data['feedback']
            choices = ', '.join([dict(FeedbackForm.FEEDBACK_CHOICES).get(f) for f in feedback])
            choice = f'{choices}'
            return render(request, 'myapp/fb_results.html', {'choice': choice})
        else:
            return HttpResponse('Invalid data')
    else:
        form = FeedbackForm()
        return render(request, 'myapp/feedback.html', {'form': form})


def findbooks(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            max_price = form.cleaned_data['max_price']
            booklist = Book.objects.all()
            if category:
                booklist = [book for book in booklist if book.price <= max_price and book.category == category]
            else:
                booklist = [book for book in booklist if book.price <= max_price]
            return render(request, 'myapp/results.html', {'name': name, 'category': category, 'booklist': booklist})
        else:
            return HttpResponse('Invalid data')
    else:
        form = SearchForm()
        return render(request, 'myapp/findbooks.html', {'form': form})

def bookhistory(request):
    orders = Order.objects.all()
    return render(request, 'myapp/history.html', {'orders': orders})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            books = form.cleaned_data['books']
            order = form.save(commit=False)
            member = order.member
            type = order.order_type
            order.save()
            form.save_m2m()
            if type == 1:
                for b in order.books.all():
                    member.borrowed_books.add(b)
            return render(request, 'myapp/order_response.html', {'books': books, 'order': order})
        else:
            return render(request, 'myapp/placeorder.html', {'form': form})
    else:
        form = OrderForm()
        return render(request, 'myapp/placeorder.html', {'form': form})

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            if 1 <= rating <= 5:
                review = form.save()
                book = review.book
                book.num_reviews += 1
                book.save()
                return redirect('myapp:index')
            else:
                return render(request, 'myapp/review.html', {'form': form, 'error_message': 'You must enter a rating between 1 and 5!'})
        else:
            return render(request, 'myapp/review.html', {'form': form})
    else:
        form = ReviewForm()
        return render(request, 'myapp/review.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session['last_login'] = str(datetime.datetime.now())
                request.session.set_expiry(3600)
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'myapp/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp:index'))

@login_required
def chk_reviews(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.user:
        reviews = Review.objects.filter(book=book, reviewer=request.user.email)
        if reviews.exists():
            avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
            return render(request, 'myapp/chk_reviews.html', {'avg_rating': avg_rating, 'book': book})
        else:
            return render(request, 'myapp/chk_reviews.html', {'message': 'No reviews submitted for this book.', 'book': book})
    else:
        return render(request, 'myapp/chk_reviews.html', {'message': 'You are not a registered member!', 'book': book})

    # if 'order_counter' not in request.session:
    #     request.session['order_counter'] = 0
    # request.session['order_counter'] += 1
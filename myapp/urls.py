from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('feedback/', views.getFeedback, name='feedback1'),
    path('findbooks/', views.findbooks, name='findbooks'),
    path('history/', views.bookhistory, name='history'),
    path('place_order/', views.place_order, name='place_order'),
    path('review/', views.review, name='review'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('setcookie/', views.setcookie, name='setcookie'),
    path('chk_reviews/<int:book_id>/', views.chk_reviews, name='chk_reviews'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),# Added this line to make the library app the default app
    #path('hello/', views.hello, name='hello'), # Added this line to include the library app views
    path('books/', views.books, name='books'), # Added this line to include the library app views
    path('students/', views.students, name='students'), # Added this line to include the library app views
    path('create_book/', views.create_book, name='create_book'), # Added this line to include the library app views
    path('create_student/', views.create_student, name='create_student'), # Added this line to include the library app views
    path('loginpage/', views.loginpage, name='loginpage'), # Added this line to include the library app views
    path('register/', views.register, name='register'), # Added this line to include the library app views
    path('logoutUser/', views.logoutUser, name='logout'), # Added this line to include the library app views
]
from django.forms import ModelForm
from .models import Books, Students
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'genre', 'isbn']

class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'student_id', 'books', 'return_date', 'fine']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
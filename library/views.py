from django.shortcuts import render, redirect
from .models import Books, Students
from .forms import BookForm, StudentForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='loginpage')
def home(request):
    total_books = Books.objects.count()
    total_students = Students.objects.count()
    total_available_books = Books.objects.filter(available=True).count()
    return render(request, 'home.html', {'total_books': total_books, 'total_students': total_students, 'total_available_books': total_available_books})


@login_required(login_url='loginpage')
def books(request):
    books = Books.objects.all()
    return render(request, 'books.html', {'books': books})

@login_required(login_url='loginpage')
def students(request):
    students = Students.objects.all()
    return render(request, 'students.html', {'students': students})

@login_required(login_url='loginpage')
def stats(request):
    return render(request, 'stats.html')

@login_required(login_url='loginpage')
def create_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    context = {'form': form}
    return render(request, 'bookform.html', context)

@login_required(login_url='loginpage')
def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    context = {'form': form}
    return render(request, 'studentsform.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username') 
            password = request.POST.get('password') 
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('loginpage')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('loginpage')
        context = {'form': form}
        return render(request, 'register.html', context)
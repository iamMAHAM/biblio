from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from .forms import RegisterForm


def home(request):
    return render(request, 'home.html')


def books(request):
    all_books = [
        {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'price': 200},
        {'title': 'The Monk Who Sold His Ferrari',
            'author': 'Robin Sharma', 'price': 300},
        {'title': 'The 7 Habits of Highly Effective People',
            'author': 'Stephen R. Covey', 'price': 400},
        {'title': 'The Power of Positive Thinking',
            'author': 'Norman Vincent Peale', 'price': 500},
        {'title': 'The Power of Your Subconscious Mind',
            'author': 'Joseph Murphy', 'price': 600}
    ]
    return render(request, 'books.html', {"books": all_books})


def profile(request):
    return render(request, 'profile.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)

        user = authenticate(username=username, password=password)

        if user:
            django_login(request, user)
            return redirect('home')

        messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            django_login(request, user)
            return redirect('login')

        messages.error(request, form.errors)
    return render(request, 'register.html', {"form": form})


def about(request):
    return render(request, 'about.html')

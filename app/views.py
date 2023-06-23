from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as Login, logout as Logout
from django.contrib import messages
from app.models import Livre, Utilisateur
from .forms import RegisterForm
# Create your views here.
from django.shortcuts import render


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
        username = request.POST['username']
        mdp = request.POST['mdp']
        user = authenticate(request, username=username, password=mdp)
        print(user)
        if user:
            Login(request, user)
            return redirect('books')

        return render(request, 'login.html')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        # get the post parameter
        try:
            form = RegisterForm(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('login')

            raise ValueError('form is not valid')
        except Exception as e:
            print(e)
            return render(request, 'register.html')

    return render(request, 'register.html', {'form': RegisterForm()})


def about(request):
    return render(request, 'about.html')

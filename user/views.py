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
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def about(request):
    return render(request, 'about.html')

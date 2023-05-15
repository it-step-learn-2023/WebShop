from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'accounts/profile.html', context={
        'title': 'Профіль',
        'page' : 'profile',
        'app' : 'accounts'
    })

def sign_in(request):
    return render(request, 'accounts/sign_in.html', context={
        'title': 'Вхід',
        'page' : 'sigh_in',
        'app' : 'accounts'
    })

def sign_up(request):
    return render(request, 'accounts/sign_up.html', context={
        'title': 'Реєстрація',
        'page' : 'sigh_up',
        'app' : 'accounts'
    })

def sign_out(request):
    return render(request, 'accounts/sign_out.html', context={
        'title': 'Вихід',
        'page' : 'sigh_out',
        'app' : 'accounts'
    })

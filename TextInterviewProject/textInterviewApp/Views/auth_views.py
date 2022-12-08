"""Authentication controller
"""
from django.shortcuts import render, redirect


def login(request):
    """ GET
    Return:

    """
    return render(request, 'accounts/login.html')


def signup(request):
    """ GET
    Return:

    """
    return render(request, 'accounts/signup.html')

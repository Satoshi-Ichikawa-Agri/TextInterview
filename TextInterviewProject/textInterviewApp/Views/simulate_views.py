"""Simulation controller
"""
from django.shortcuts import render, redirect


def sim_index(request):
    """ GET
    Return:

    """
    return render(request, 'simulations/index.html')


def sim_start(request):
    """ GET
    Return:

    """
    return render(request, 'simulations/start.html')

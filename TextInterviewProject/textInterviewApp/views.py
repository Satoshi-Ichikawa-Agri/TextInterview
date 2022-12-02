"""textInterviewApp
"""
from django.shortcuts import render, redirect

from .forms import *
from .models import *


def home(request):
    """ GET
    Return:

    """
    return render(request, 'home.html')


def index(request):
    """ GET
    Return:

    """
    question_list = Question.objects.all()
    context = {'question_list': question_list}

    return render(request, 'questions/index.html', context)


def create(request):
    """ GET & POST
    Return:

    """
    question_list = Question.objects.all()
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/index/')

    context = {'question_list': question_list, 'form': form}

    return render(request, 'questions/create.html', context)


def update(request, id):
    """ GET & POST
    Return:
        
    """
    question = Question.objects.get(id=id)
    form = QuestionForm(instance=question)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
        return redirect('/index/')

    context = {'form': form}

    return render(request, 'questions/update.html', context)


def delete(request, id):
    """ GET & POST
    Return:
        
    """
    item = Question.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('/index/')

    context = {'item': item}
    return render(request, 'questions/delete.html', context)

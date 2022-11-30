from django.shortcuts import render, redirect

from .forms import *
from .models import *


def index(request):
    question_list = Question.objects.all()
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'question_list': question_list, 'form': form}

    return render(request, 'index.html', context)



def update(request, id):
    question = Question.objects.get(id=id)
    form = QuestionForm(instance=question)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}

    return render(request, 'update.html', context)


def delete(request, id):
    item = Question.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'delete.html', context)

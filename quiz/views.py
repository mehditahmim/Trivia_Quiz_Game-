from django.shortcuts import render
import json
import random
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def showQuestions(request):  
    with open('quiz.json') as f:
        data = json.load(f)
        idx = getRandomQuestions(data)
        question = data[idx]
        choices = list(question["options"].items())
        print(choices)
        random.shuffle(choices)
        print(choices)
        question['options']=dict(choices)
        context = {'question':question}       
        return render(request, 'questions.html',context)

def getRandomQuestions(data):
    l = len(data)
    lst = [i for i in range(len(data))]
    rand_index = random.randint(0, len(lst)-1)
    return rand_index


def index(request):
    if request.method == 'POST':

        if request.POST.get("start_quiz"):
            request.session['points'] = 0
            return HttpResponseRedirect(reverse('questions'))
    return render(request, 'home.html')






def checkAnswer():
    pass       



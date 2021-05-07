from django.shortcuts import render
import json
# Create your views here.
def showQuestions(request):  
    with open('quiz.json') as f:
        data = json.load(f)
        question = data[1]
        choices = question['options']    
        print(choices)
        context = {'question':question, 'choices':choices}
        return render(request, 'questions.html',context)


        



from django.shortcuts import redirect, render
from .models import *

def main(request) :
    surveys = Survey.objects.all()
    return render(request, 'main.html', {'surveys' : surveys})

# def main(request) :
#     if Survey.objects.get_queryset().exists() : 
#         survey = Survey.objects.filter()[0]
#         return render(request, 'main.html', {'survey' : survey})
#     return render(request, 'main.html')

def new(request) :
    return render(request, "new.html")

def create(request) :
    if request.method == "POST" :
        survey = Survey()
        survey.question = request.POST["question"]
        survey.ans1 = request.POST["ans1"]
        survey.ans2 = request.POST["ans2"]
        survey.ans3 = request.POST["ans3"]
        survey.ans4 = request.POST["ans4"]
        survey.save()
    return redirect('main')

def save(request) :
    submit = Answer(surveyIdx = request.POST["surveyIdx"], choice = request.POST["choice"])
    submit.save()
    return render(request, "complete.html")
    # return render(request, "complete.html", {"surveyIdx" : surveyIdx})

# def result(request) :
#     surveyIdx = request.GET["surveyIdx"]
#     survey = Survey.objects.filter(surveyIdx=surveyIdx)[0]
#     results = {
#         survey.ans1 : 0,
#         survey.ans2 : 0,
#         survey.ans3 : 0,
#         survey.ans4 : 0 
#     }
    
#     answers = Answer.objects.filter(surveyIdx=surveyIdx)
#     for answer in answers : 
#         results[answer.choice] += 1
 
#     return render(request, 'result.html', {'results' : results})
    

def result(request, surveyIdx) :
    survey = Survey.objects.filter(surveyIdx=surveyIdx)[0]
    results = {
        survey.ans1 : 0,
        survey.ans2 : 0,
        survey.ans3 : 0,
        survey.ans4 : 0 
    }
    
    answers = Answer.objects.filter(surveyIdx=surveyIdx)
    for answer in answers : 
        results[answer.choice] += 1
 
    return render(request, 'result.html', {'results' : results})
    
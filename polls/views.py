
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse("Estás viendo la pregunta %s." % question_id)

def results(request, question_id):
    response = "Estás viendo los resultados de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Estás votando en la pregunta %s." % question_id)

# Create your views here.

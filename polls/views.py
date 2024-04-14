
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("Estás viendo la pregunta %s." % question_id)

def results(request, question_id):
    response = "Estás viendo los resultados de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Estás votando en la pregunta %s." % question_id)

# Create your views here.

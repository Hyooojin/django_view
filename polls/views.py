from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

from django.template import loader

# Create your views here
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello, world! ")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

    # return HttpResponse("detail page using HttpResponse")

def results(request, question_id):
    response = "Yor're looking at the results of question %s."
    return HttpResponse(response % question_id)
    # response = "response page using valiable and HttpResponse. You're looking at the results of question %s."
    # return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
    # return HttpResponse("vote page using HttpResponse")
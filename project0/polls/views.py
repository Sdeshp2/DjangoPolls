from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from . models import question
from django.template import loader
def index(request):
	latest_question_list = question.objects.order_by('-qdate')
	template = loader.get_template('polls/index.html')
	context = {

		'latest_question_list': latest_question_list,

	}

	return HttpResponse(template.render(context, request))
  
def about(request):
	return render(request, 'polls/about.html',{"value":"Shubhankar"})

def detail(request, question_id):
	ans = get_object_or_404(question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': ans,'Result':'Nothing to display'})
 
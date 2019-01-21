#C:\Users\Rhyle\Envs\Regodon\Scripts\activate.bat
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .forms import QuestionModelForm

# Create your views here
def index(request):
	context = {}
	question = Question.objects.all()
	context['questions'] = question
	return render(request, 'index.html', context)

def help(request):
	return HttpResponse('Help')

def details (request, question_id):
	context = {}
	context['question'] = Question.objects.get(id=question_id)
	return render(request, 'details.html', context)

def update (request,question_id):
	question = Question.objects.get(id = question_id)
	context = {}


	if request.method == 'POST':
		form = QuestionModelForm(request.POST, instance=question)
		if form.is_Valid():
			form.save()
			return HttpResponse('Question updated')
		else:
			context['form'] = form
			render(request, 'update.html', context)
	else:
		context['form'] = QuestionModelForm(instance = question)
	return render(request, 'update.html', context)

def vote(request, question_id):
	pass
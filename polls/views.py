from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Question, Choice
from django.urls import reverse

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	# output = ', '.join([q.question_text for q in latest_question_list])
	# return HttpResponse("Hello, world. You're at the polls index.")
	# return HttpResponse(template.render(context, request))
	return render(request, 'polls/index.html',context)
def detail(request, question_id):
	# try:
	# 	question = Question.objects.get(pk = quest
	# 	raise Http404("Question does not exist")
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/detail.html', {'question': question})
	# return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# print ("except {}".format(selected_choice.votes))
		return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.",})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		print ("else {}".format(selected_choice.votes))
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
	# return HttpResponse("You're voting on question %s." % question_id)

from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse

"""	#############################################
def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(re)
	
	#this code is imcomplete see lecture 4: Raising a 404 error
	
	############################################ """

	
def about(request):
	# Constructs an about page.
	context_dict = {'boldmessage': "This is the __about__ page!! Yayyy"}
	return render(request, 'rango/about.html', context=context_dict)
	return HttpResponse("Rango says hey there partner!")
	
def index(request):
	# Constructs a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	
	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	return render(request, 'rango/index.html', context=context_dict)
	
	# This is from previous work.
	# The HttpResponse just outputs a string onto the page.
	#return HttpResponse("Rango says hey there partner!")
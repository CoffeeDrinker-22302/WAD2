from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm

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
	
def add_category(request):
	form = CategoryForm()
	
	# A HTTP POST?
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		
		#Have we been provided with a valid form?
		if form.is_valid():
			# Save the new category to the database.
			form.save(commit=True)
			# Now that the category is aved
			# We could give a confirmation message
			# but since the most recent category added is on the index page
			# Then we can direct the user back to the index page.
			return index(request)
		else:
			# The supplied form contained errors -
			# just rint them to the terminal.
			print(form.errors)
	# Will handle the bad form, new form, or no form supplied cases
	# Render the form with error messages (if any)
	return render(request, 'rango/add_category.html', {'form':form})
	
def index(request):
	# Query the database for a list of ALL categories currently stored.
	# Order the categories by no. likes in descending order.
	# Retrieve the top 5 only - or all if less than 5.
	# Place the list in our context_dict dictionary
	# that will be passed to the template engine.
	category_list = Category.objects.order_by('-likes')[:5]
	category_list_most_views = Category.objects.order_by('-views')
	context_dict = {'categories': category_list,'most_liked':category_list_most_views}

	# Render the response and send it back!
	return render(request, 'rango/index.html', context_dict)
	
def show_category(request, category_name_slug):
	# Create a context dictionary which we can pass
	# to the template rendering engine.
	context_dict = {}
	try:
		# Can we find a category name slug with the given name?
		# If we can't, the .get() method raises a DoesNotExist exception.
		# So the .get() method returns one model instance or raises an exception.
		category = Category.objects.get(slug=category_name_slug)
		
		# Retrieve all of the associated pages.
		# Note that filter() will return a list of page objects or an empty list
		pages = Page.objects.filter(category=category)
		
		# Adds our results list to the template context under name pages.
		context_dict['pages'] = pages
		# We also add thhe category object from
		# the database to the context dictionary.
		# We'll use this in the template to verify that the category exists.
		context_dict['category'] = category
	except Category.DoesNotExist:
		# We get here if we didn't find the specified category
		# Don't do anything -
		# the template will display the "no category" message for us.
		context_dict['category'] = None
		context_dict['pages'] = None
	
	#Go render the response and return it to the client.
	return render(request, 'rango/category.html',context_dict)
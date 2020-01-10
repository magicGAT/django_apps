""" page load functions
user sends a request, server checks the `urlpatterns` variable in 
`urls.py` for a match, if a match is found, the second argument is invoked and
the server sends the client the result of that function (the commands for those 
functions are found inside this `views.py` file)

the view functions returns HTML templates, which are contained in the project folder
"""

# library for primitive HTTP server response
from django.http import HttpResponse

# library for serving HTML files
from django.shortcuts import render

# library for dictionary sorting (operator object)
import operator

# home page request function

def home_page(request):
	return render(request, "home.html")

def count(request):
	full_text = request.GET["full_text"]
	word_list = full_text.split()

	tallies = {}
	for word in word_list:
		if word in tallies:
			tallies[word] += 1
		else:
			tallies[word] = 1

	sorted_words = sorted(tallies.items(), key=operator.itemgetter(1), reverse=True)
	return render(request, "count.html", {"fulltext": full_text, "count":len(word_list), "tallies":sorted_words})

def about(request):
	return render(request, "about.html")
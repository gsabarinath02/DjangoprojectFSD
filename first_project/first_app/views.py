from django.shortcuts import render
from django.http import HttpResponseRedirect
from first_app.models import Degree, Student

from .forms import DegreeForm
import json

# Create your views here.
count = 1
def index(request) :
    global count
    count += 1
    files = ['settings.py', 'urls.py', 'views.py',
                'models.py', 'templates', 'static']

    degree_rows = Degree.objects.all()
    my_dict = {
        'name': '',
        'count' : count,
        'files' : files,
        'degree_rows' : degree_rows,
    }
    return render(request, "index.html", my_dict)

def get_degree(request):
  if request.method == 'POST':                  # if this is a POST request we need to process the form data
    form = DegreeForm(request.POST, request.FILES)   # create a form instance and populate it with data from the request:
    if form.is_valid():                         # check whether it's valid:
      title = form.cleaned_data['title']        # process the data in form.cleaned_data as required
      branch = form.cleaned_data['branch']
      print(title, branch)

      d = Degree(title=title, branch=branch)    # write to the database
      d.save()

      # Retrieve the json file and process here
      f = request.FILES['file']          # open the json files - get file handle
      data = json.load(f)
      #print(data['degree'])                # get json object as a dictionary
      for deg in data['degree']:         # iterate through the degree list
        t = deg['title']                 # get the title of each item in the list
        b = deg['branch']                # get the branch of each item in the list
        dl = Degree(title=t, branch=b)   # Create a Degree model instance
        dl.save()                        # save

      return HttpResponseRedirect('/degree/')   # redirect to a new URL:
  else:                                       # if a GET (or any other method) we'll create a blank form
    form = DegreeForm()

  return render(request, 'degree.html', {'form': form })

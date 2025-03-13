from django.shortcuts import render, redirect
from .form import JobSearchForm

# Create your views here.

#Home view
def home_view(request):
    return render(request, 'form_app/home.html')

#define the search view to handle search form
def search_view(request):
    if request.method == "POST":
        form = JobSearchForm(request.POST)
        if form.is_valid():
            return redirect('search-success')
    else:
        form = JobSearchForm()
    context = {'form': form}
    return render(request, 'form_app/search.html', context)

#Define the search success view

def form_success_view(request):
    return render(request, 'form_app/search_success.html')
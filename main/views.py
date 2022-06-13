from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .forms import SearchForm,AddMapForm
from .search import  searchFunction, storeFunction

def search(response):
    data=""
    if response.method=="POST":
        search_form=SearchForm(response.POST)
        if search_form.is_valid():
            data = searchFunction(search_form.cleaned_data["start"],search_form.cleaned_data["goal"])
         
    else:
        search_form=SearchForm()
    return render(response,'main/search.html', {"search_form":search_form, "data":data})
 
 
def add(response):
    data=""
    if response.method=="POST":
        add_map_form=AddMapForm(response.POST)
        if add_map_form.is_valid():
            data = storeFunction(add_map_form.cleaned_data["country_map"],add_map_form.cleaned_data["straight_length"])
              
    else:
        add_map_form=AddMapForm()
    return render(response,'main/add.html', {"add_map_form":add_map_form,"data":data})

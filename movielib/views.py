from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from movielib.models import Movie 
from movielib.forms import MovieMixin





class IndexView(ListView):
	template_name = 'index.html'
	model = Movie




class CreateView(CreateView):
	template_name= 'create.html'
	model = Movie
	success_url = '/movielib'



class UpdateView(UpdateView):
    template_name = 'update.html'
    model = Movie
    success_url = '/movielib'



class DeleteView(MovieMixin, DeleteView):
	template_name = 'confirm_delete.html'
	model = Movie
	success_url = '/movielib'







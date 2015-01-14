from django.contrib import admin
from movielib.models import Movie



# class ChoiceInline(admin.StackedInline):
# 	model = Movie
# 	extras = 2




class MovieAdmin(admin.ModelAdmin):
	list_display = ['title','genre', 'release_date','price']
	# inlines =[ChoiceInline]
	list_filter = ['release_date']
	search_fields = ['title']











admin.site.register(Movie, MovieAdmin)


# Register your models here.

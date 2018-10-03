from django.contrib import admin
from .models import Movie, ExtraInfo, Review, Actor

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ("name", "description", "year")
    list_display = ("name", "year", 'description', "released")
    list_filter = ("year", "released")
    search_fields = ("name", "description")

admin.site.register(ExtraInfo)
admin.site.register(Review)
admin.site.register(Actor)



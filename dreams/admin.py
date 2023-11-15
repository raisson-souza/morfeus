from django.contrib import admin
from dreams.models import Dream

class ListDreams(admin.ModelAdmin):
    list_test = ['id', 'title', 'time']

admin.site.register(Dream)

# Register your models here.

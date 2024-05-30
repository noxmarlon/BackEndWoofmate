from django.contrib import admin
from .models import Pet

# Register your models here.


class PetAdmin(admin.ModelAdmin):
    list_display = ['petName', 'petType', 'petAge', 'petBreed', 'owner']
    search_fields = ['petName', 'petType', 'petBreed', 'owner__username']

admin.site.register(Pet, PetAdmin)

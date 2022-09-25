from django.contrib import admin
from .models import *

admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(City)
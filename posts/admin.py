from django.contrib import admin
from .models import Experiment, MaterialsList, Procedure

# Register your models here.
admin.site.register(Experiment)
admin.site.register(MaterialsList)
admin.site.register(Procedure)

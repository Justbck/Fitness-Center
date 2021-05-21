from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Membership)
admin.site.register(Instructor)
admin.site.register(WorkoutSession)
admin.site.register(PersonalClass)
admin.site.register(GroupClass)


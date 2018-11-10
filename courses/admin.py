from django.contrib import admin
from .models import Course, Section, Room, Day

# Register your models here.
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Room)
admin.site.register(Day)

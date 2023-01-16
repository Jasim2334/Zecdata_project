from django.contrib import admin
from .models import HabitModel

# Register your models here.

class HabitAdmin(admin.ModelAdmin):
    list_display = ('id','habit1','habit2','habit3','habit4','habit5')


admin.site.register(HabitModel,HabitAdmin)

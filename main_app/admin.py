from django.contrib import admin
from .models import State, Score, Progress, TotalScore

# Register your models here.

admin.site.register(State)
admin.site.register(Score)
admin.site.register(Progress)
admin.site.register(TotalScore)
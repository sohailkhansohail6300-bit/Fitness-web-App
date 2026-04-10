from django.contrib import admin
from .models import ExerciseSchedule,NutrationPlane,video
# Register your models here.

@admin.register(ExerciseSchedule)
class Exerrcise_Schedule(admin.ModelAdmin):
    list_display=['Exercise_name','sets_reps','coach_notes']
    search_fields=['Exercise_name']


@admin.register(NutrationPlane)
class Nutration_Plane(admin.ModelAdmin):
    list_display=['Meal','Food_items','Macros','time']

@admin.register(video)
class Video(admin.ModelAdmin):
    list_display=['desc','video']
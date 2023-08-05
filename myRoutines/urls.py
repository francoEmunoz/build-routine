from django.urls import path
from .views import myRoutine, delete_routine, delete_day, delete_exercise, edit_routine, edit_exercise, shared_routines

myroutines_patterns = ([
    path('', myRoutine, name='myroutines'),
    path('edit_routine/<int:routine_id>/', edit_routine, name='edit_routine'),
    path('edit_exercise/<int:exercise_id>/', edit_exercise, name='edit_exercise'),
    path('delete_routine/<int:routine_id>/', delete_routine, name='delete_routine'),
    path('delete_day/<int:day_id>/', delete_day, name='delete_day'),
    path('delete_exercise/<int:exercise_id>/', delete_exercise, name='delete_exercise'),
    path('shared_routines/<int:routine_id>/', shared_routines, name='shared_routines')
], 'myroutines')
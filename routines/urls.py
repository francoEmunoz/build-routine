from django.urls import path
from .views import routines, copy_routine

routines_patterns = ([
    path('', routines, name='routines'),
    path('copy_routine/<int:routine_id>', copy_routine, name='copy_routine')
], 'routines')
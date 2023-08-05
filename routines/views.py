from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from myRoutines.models import Routine, Day, Exercise

# Create your views here.
def routines(request):
    routine = Routine.objects.filter(shared=True)
    day = Day.objects.all()
    exercise = Exercise.objects.all()

    return render(
        request,
        'routines.html',
        {
            'routine': routine,
            'day': day,
            'exercise': exercise,
        })

def copy_routine(request, routine_id):
    original_routine = get_object_or_404(Routine, id=routine_id)

    copied_routine = Routine.objects.create(title=original_routine.title, user=request.user)
    messages.success(request, 'Has agregado la rutina "' + copied_routine.title + '" a tus rutinas')

    for original_day in original_routine.day_set.all():
        copied_day = Day.objects.create(dayNumber=original_day.dayNumber, routine=copied_routine)

        for original_exercise in original_day.exercise_set.all():
            Exercise.objects.create(
                name=original_exercise.name,
                series=original_exercise.series,
                reps=original_exercise.reps,
                day=copied_day,
            )

    return redirect('/mis-rutinas')
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Routine, Day, Exercise
from .forms import RoutineForm, DayForm, ExerciseForm


# Create your views here.
def myRoutine(request):
    routine = Routine.objects.all()
    day = Day.objects.all()
    exercise = Exercise.objects.all()

    form = RoutineForm()
    if request.method == "POST":
        form = RoutineForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title'].capitalize()
            Routine.objects.create(title=title, user=request.user)
            messages.success(request, 'La rutina fue creada correctamente')

        else:
            print(form.errors)

    formDay = DayForm()
    if request.method == "POST":
        formDay = DayForm(data=request.POST)
        if formDay.is_valid():
            routineR = formDay.cleaned_data['routine']             
            for r in routine:
                if request.user == r.user and r == routineR:
                    day_count = r.day_set.count()
                    day_number = day_count + 1
                    Day.objects.create(dayNumber=day_number, routine=r)
                    messages.success(request, 'Se agregó un día a tu rutina')
        else:
            print(formDay.errors)
    
    formExercise = ExerciseForm()
    if request.method == "POST":
        formExercise = ExerciseForm(data=request.POST)
        if formExercise.is_valid():
            name = formExercise.cleaned_data['name'].capitalize()
            series = formExercise.cleaned_data['series']
            reps = formExercise.cleaned_data['reps']
            dayD = formExercise.cleaned_data['day']
            for r in routine:
                if request.user == r.user:
                    for d in day:
                        if d.routine == r and d == dayD:
                            Exercise.objects.create(name=name, series=series, reps=reps, day=d)
                            messages.success(request, 'Se agregó un ejercicio a la rutina "' + r.title + '"')
        else:
            print(formExercise.errors)

    return render(
        request,
        'myRoutines/myRoutines.html',
        {
            'form': RoutineForm,
            'dayform': DayForm,
            'exerciseform': ExerciseForm,
            'routine': routine,
            'day': day,
            'exercise': exercise,
        })


def edit_routine(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)

    if request.method == "POST":
        form = RoutineForm(request.POST, instance=routine)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu rutina se actualizó correctamente')
            return redirect('/mis-rutinas')
        
        
    else:
        form = RoutineForm(instance=routine)

    return render(
        request,
        {
            'form': form,
        }
    )


def edit_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)

    if request.method == "POST":
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            messages.success(request, 'El ejercicio se actualizó correctamente')
            return redirect('/mis-rutinas')
    else:
        form = ExerciseForm(instance=exercise)

    return render(
        request,
        {
            'form': form,
        }
    )


def delete_routine(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)

    if request.user == routine.user:
        routine.delete()
        messages.success(request, 'Se eliminó la rutina "' + routine.title + '"')
    
    return redirect('/mis-rutinas')


def delete_day(request, day_id):
    day = get_object_or_404(Day, id=day_id)

    if request.user == day.routine.user:
        day.delete()
        messages.success(request, 'Se eliminó un día de tu rutina')
    
    return redirect('/mis-rutinas')


def delete_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)

    if request.user == exercise.day.routine.user:
        exercise.delete()
        messages.success(request, 'Se eliminó un ejercicio de tu rutina')
    
    return redirect('/mis-rutinas')


def shared_routines(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)

    if request.user == routine.user:
        if routine.shared == False:
            routine.shared = True
            routine.save()
            messages.success(request, 'Has compartido tu rutina')
        else:
            messages.error(request, 'Ya has compartido esta rutina')
    
    return redirect('/mis-rutinas')
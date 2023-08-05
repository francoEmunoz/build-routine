from django import forms
from .models import Routine, Day, Exercise

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['title']


class DayForm(forms.Form):
    routine = forms.ModelChoiceField(queryset= Routine.objects.all())


# class ExerciseForm(forms.Form):
#     name = forms.CharField(required=True)
#     series = forms.CharField(required=True)
#     reps = forms.CharField(required=True)
#     day = forms.ModelChoiceField(queryset= Day.objects.all())

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'series', 'reps', 'day']
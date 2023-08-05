from django.db import models
from django.conf import settings

    
class Routine(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, default=None, null=True, on_delete=models.CASCADE)
    shared = models.BooleanField(default=False)

    class Meta:
        verbose_name = "rutina"
        verbose_name_plural = "rutinas"

    def __str__(self):
        return self.title


class Day(models.Model):
    dayNumber = models.PositiveSmallIntegerField(null=True)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "día"
        verbose_name_plural = "días"

    def __str__(self):
        return str(self.dayNumber)
    

class Exercise(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)
    series = models.PositiveSmallIntegerField(null=True)
    reps = models.PositiveSmallIntegerField(null=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "ejercicio"
        verbose_name_plural = "ejercicios"

    def __str__(self):
        return self.name
    

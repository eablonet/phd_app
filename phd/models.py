from django.db import models

# Create your models here.


class Substrat(models.Model):
    name = models.CharField(max_length=20)
    date_treatment = models.DateTimeField(
            blank=True, null=True
    )

    def __str__(self):
        return self.name


class Tensiometrie(models.Model):
    static = 'st'
    advancing = 'ad'
    receding = 're'
    method_choice = (
        (static, 'Static'),
        (advancing, 'Advancing'),
        (receding, 'Receding'),
    )

    substrate = models.ForeignKey(
        'Substrat',
        on_delete=models.CASCADE)
    date = models.DateTimeField(
            blank=True, null=True
    )
    serie = models.IntegerField(blank=True, null=True)
    left = models.FloatField(blank=True, null=True)
    right = models.FloatField(blank=True, null=True)
    method = models.CharField(
        max_length=2,
        choices=method_choice,
        default=static,
    )

    def __str__(self):
        return str(self.serie)

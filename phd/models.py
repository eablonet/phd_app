from django.db import models

# Create your models here.


class Substrate(models.Model):
    """
    Define substrat model.

    This model give the main properties of each sample.
    """

    name = models.CharField(max_length=20)
    date_treatment = models.DateTimeField(
            blank=True, null=True
    )
    chemistery = models.CharField(
        max_length=20,
        blank=True, null=True
    )
    treatment_time = models.FloatField(
        blank=True, null=True
    )
    oven_time = models.FloatField(
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='media/pic_folder/', default='pic_folder/None/no-img.jpg'
    )

    def __str__(self):
        """Return string for Substrat class."""
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
        'Substrate',
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

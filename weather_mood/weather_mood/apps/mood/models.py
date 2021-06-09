from django.db import models
import datetime


from weather_mood.apps.core.models import (
    CreationModificationDateBase,
    UuidBase,
)

class Mood(CreationModificationDateBase, UuidBase):

    MOOD_CHOICES =(
        (0, "Happy"),
        (1, "Sad"),
        (2, "Fear"),
        (3, "Anger"),
    )

    mood = models.IntegerField(
        blank=False,
        null=False,
        choices=MOOD_CHOICES
    )

    weather = models.CharField(
        max_length=255
    )

    ip = models.CharField(max_length=255)

    @property
    def mood_str(self):
        return self.MOOD_CHOICES[self.mood][1]


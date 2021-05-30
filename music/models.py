from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Genre name", help_text='Enter a song genre (e.g. rock, electro, punk...)')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Song(models.Model):

    title = models.CharField(max_length=200, verbose_name="Title")

    plot = models.TextField(blank=True, null=True, verbose_name="Description")

    release_date = models.DateField(blank=True, null=True,

                                    help_text="Please use the following format: <em>YYYY-MM-DD</em>.",

                                    verbose_name="Release date")

    lenght = models.IntegerField(blank=True, null=True,

                                  help_text="Please enter an integer value (minutes)",

                                  verbose_name="Lenght")

    rate = models.FloatField(default=5.0,

                             validators=[MinValueValidator(1.0), MaxValueValidator(10.0)],

                             null=True,

                             help_text="Please enter an float value (range 1.0 - 10.0)",

                             verbose_name="Rating")

    genres = models.ManyToManyField(Genre, help_text='Select a genre for this song')

    # Metadata

    class Meta:
        # Záznamy budou řazeny primárně sestupně (znaménko mínus) podle data uvedení,

        # sekundárně vzestupně podle názvu

        ordering = ["-release_date", "title", "rate"]

    def __str__(self):

        return f"{self.title}, year: {str(self.release_date.year)}, rate: {str(self.rate)}"

    def get_absolute_url(self):

        return reverse('film-detail', args=[str(self.id)])

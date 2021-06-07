from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


def attachment_path(instance, filename):
    return "song/" + str(instance.film.id) + "/attachments/" + filename


def album_path(instance, filename):
    return "song/" + str(instance.id) + "/album/" + filename


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

    class Meta:

        ordering = ["-release_date", "title", "rate"]

    def __str__(self):

        return f"{self.title}, year: {str(self.release_date.year)}, rate: {str(self.rate)}"

    def get_absolute_url(self):

        return reverse('song-detail', args=[str(self.id)])


class Album(models.Model):
    title = models.CharField(max_length=200, help_text="Album title")

    songs = models.ManyToManyField(Song, help_text="Songs in album")

    release_date = models.DateField(blank=True, null=True,

                                    help_text="Please use the following format: <em>YYYY-MM-DD</em>.",

                                    verbose_name="Release date")

    rate = models.FloatField(default=5.0,

                             validators=[MinValueValidator(1.0), MaxValueValidator(10.0)],

                             null=True,

                             help_text="Please enter an float value (range 1.0 - 10.0)",

                             verbose_name="Rating")

    def __str__(self):

        return f"{self.title}, year: {str(self.release_date.year)}, rate: {str(self.rate)}"


class Attachment(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")

    last_update = models.DateTimeField(auto_now=True)

    file = models.FileField(upload_to=attachment_path, null=True, verbose_name="File")

    TYPE_OF_ATTACHMENT = (
        ('audio', 'Audio'),
        ('image', 'Image'),
        ('text', 'Text'),
        ('video', 'Video'),
        ('other', 'Other'),
    )

    type = models.CharField(max_length=5, choices=TYPE_OF_ATTACHMENT, blank=True, default='image', help_text='Select allowed attachment type', verbose_name="Attachment type")

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-last_update", "type"]


class Playlist(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)

    plot = models.TextField(blank=True, null=True, verbose_name="Playlist description")

    song = models.ManyToManyField(Song, help_text="Select songs for your playlist")

    def __str__(self):
        return self.title

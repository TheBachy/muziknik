from django.shortcuts import render

from django.shortcuts import render
from music.models import *
from django.views.generic import DetailView


def index(request):
    """Metoda připravuje pohled pro domovskou stránku - šablona index.html"""

    # Uložení celkového počtu filmů v databázi do proměnné num_films
    num_songs = Song.objects.all().count()

    # Do proměnné films se uloží 3 filmy uspořádané podle hodnocení (sestupně)
    songs = Song.objects.order_by('-rate')[:3]

    """ Do proměnné context, která je typu slovník (dictionary) uložíme hodnoty obou proměnných """
    context = {
        'num_songs': num_songs,
        'songs': songs
    }

    """ Pomocí metody render vyrendrujeme šablonu index.html a předáme ji hodnoty v proměnné context k zobrazení """
    return render(request, 'index.html', context=context)


class SongDetailView(DetailView):

    model = Song

    context_object_name = 'song_detail'
    template_name = 'song/detail.html'




def topten(request):
    return render(request, 'topten.html')

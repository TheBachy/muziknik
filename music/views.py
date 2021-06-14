from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy

from music.models import *
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


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


class BandDetailView(DetailView):

    model = Band

    context_object_name = 'band_detail'
    template_name = 'band/detail.html'


class SongListView(ListView):

    model = Song

    context_object_name = 'song_list'
    template_name = 'song/list.html'
    paginate_by = 9


def topten(request):
    return render(request, 'topten.html')


class SongCreate(CreateView):
    model = Song
    fields = ['band', 'title', 'genres', 'release_date', 'rate', 'length', ]
    initial = {'rate': '5'}


class SongUpdate(UpdateView):
    model = Song
    template_name = 'form/song_bootstrap_form.html'
    fields = '__all__' # Not recommended (potential security issue if more fields added)


class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('films')

from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Album
from .forms import TrackFormSet


# Album Views
class AlbumListView(ListView):
    model = Album


class AlbumCreateView(CreateView):
    model = Album
    success_url=reverse_lazy('music:album_list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(AlbumCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['track_formset'] = TrackFormSet(self.request.POST)
        else:
            context['track_formset'] = TrackFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['track_formset']
        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)


class AlbumUpdateView(UpdateView):
    model = Album
    success_url=reverse_lazy('music:album_list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(AlbumUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['track_formset'] = TrackFormSet(self.request.POST, instance=self.object)
            context['track_formset'].full_clean()
        else:
            context['track_formset'] = TrackFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['track_formset']
        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)


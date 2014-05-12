from django.forms.models import inlineformset_factory
from .models import Album, Track

TrackFormSet = inlineformset_factory(Album, Track)



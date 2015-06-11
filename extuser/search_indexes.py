from haystack import indexes
from .models import ExtUser


class ExtUsereIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    location = indexes.CharField(model_attr='location')

    def get_model(self):
        return ExtUser

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

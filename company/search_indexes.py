from haystack import indexes
from .models import Company


class CompanyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    email = indexes.CharField(model_attr='email')
    type = indexes.CharField(model_attr='type')
    address = indexes.CharField(model_attr='address', default=None)
    location = indexes.CharField(model_attr='location')
    description = indexes.CharField(model_attr='description', default=None)
    added_at = indexes.DateTimeField(model_attr='added_at')
    last_change = indexes.DateTimeField(model_attr='last_change')

    def get_model(self):
        return Company

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

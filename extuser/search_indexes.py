from haystack import indexes
from .models import ExtUser


class ExtUsereIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    location = indexes.CharField(model_attr='location')
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')
    role = indexes.IntegerField(model_attr='role')
    desired_salary = indexes.IntegerField(model_attr='desired_salary', default=None)
    register_date = indexes.DateField(model_attr='register_date')
    email = indexes.CharField(model_attr='email')

    def get_model(self):
        return ExtUser

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

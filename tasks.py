from celery import task
from haystack.management.commands import update_index


@task
def update_indexes():
    update_index.Command().handle()

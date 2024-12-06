from characters.scraper import sync_characters_with_api

from celery import shared_task


@shared_task
def run_sync_with_api() -> None:
    sync_characters_with_api()

# celery -A rick_and_morty_api worker -l INFO --pool=solo
# (or celery -A rick_and_morty_api worker -l INFO --pool=gevent)
# celery -A rick_and_morty_api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

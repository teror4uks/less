from django.core.management.base import BaseCommand, CommandError

from src.apps.shorter.models import LessUrl


class Command(BaseCommand):
    help = 'Refresh all codes'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        return LessUrl.objects.refresh_shortcodes()
from ...models import (GuerrillaTelevisionItem, URL, Category, Tag, Genre,
                       Language, Producer, Collection, ProductionDate,
                       VideoTapeFormat)
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Clear Guerrilla Television data from the system.'

    def handle(self, *args, **options):
        GuerrillaTelevisionItem.objects.all().delete()
        URL.objects.all().delete()
        Category.objects.all().delete()
        Tag.objects.all().delete()
        Genre.objects.all().delete()
        Language.objects.all().delete()
        Producer.objects.all().delete()
        Collection.objects.all().delete()
        ProductionDate.objects.all().delete()
        VideoTapeFormat.objects.all().delete()

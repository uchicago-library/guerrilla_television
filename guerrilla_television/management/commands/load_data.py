import datetime, guerrilla_television, openpyxl, pytz, sys, wagtail
from ...models import (GuerrillaTelevisionItem, URL, Category, Tag, Genre,
                       Language, Producer, Collection, ProductionDate,
                       VideoTapeFormat)
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from wagtail.models import Page

# some data contains:
# ¬† Äî

def clean_integer_value(cell_value):
    """The data sometimes contains None, "null", "" or an integer. Regularize
       to return either None or an integer."""
    if cell_value == None:
        return None
    if str(cell_value).strip().lower() in ('null',):
        return None
    else:
        return int(cell_value)

def clean_string_value(cell_value):
    """Regularize strings."""
    if cell_value == None:
        cell_value = ''
    cell_value = str(cell_value)
    if cell_value.strip().lower() == 'none':
        cell_value = ''
    cell_value = cell_value.replace('_x000D_', '').strip()
    return cell_value

def clean_and_split_string_value(cell_value):
    """Split string values on |'s"""
    cell_value = clean_string_value(cell_value)
    values = []
    for s in cell_value.split('|'):
        c = clean_string_value(s)
        if c:
            values.append(c)
    return values

def get_unique_string_values(ws, column):
    """Get a unique list of string values from a particular spreadsheet column."""
    values = set()
    for r in range(2, ws.max_row+1):
        values |= set(
            clean_and_split_string_value(
                ws.cell(row=r, column=column).value
            )
        )
    return values

class Command(BaseCommand):
    help = 'Load video format data into the system.'

    def add_arguments(self, parser):
        parser.add_argument('xlsx', nargs=1, type=str)
        flag = parser.add_mutually_exclusive_group(required=True)
        flag.add_argument('-i', '--items', action='store_true')
        flag.add_argument('-d', '--videoformats', action='store_true')

    def handle(self, *args, **options):
        wb = openpyxl.load_workbook(options['xlsx'][0])
        ws = wb.active

        if options['videoformats']:
            # load video tape format data.
            r = 2
            while r <= ws.max_row:
                i = int(ws.cell(column=1, row=r).value)
                v = str(ws.cell(column=2, row=r).value)
                VideoTapeFormat(id=i, value=v).save()
                r += 1
            
        elif options['items']:
            headers = []
            for c in range(1, ws.max_column+1):
                headers.append(ws.cell(column=c, row=1).value)

            # load tables other than item or video tape format.
            for v in get_unique_string_values(ws, headers.index('URL') + 1):
                try:
                    URL.objects.get(value=v)
                except guerrilla_television.models.URL.DoesNotExist:
                    URL(value=v).save()
            for v in get_unique_string_values(ws, headers.index('Categories') + 1):
                try:
                    Category.objects.get(value=v)
                except guerrilla_television.models.Category.DoesNotExist:
                    Category(value=v).save()
            for v in get_unique_string_values(ws, headers.index('Tags') + 1):
                try:
                    Tag.objects.get(value=v)
                except guerrilla_television.models.Tag.DoesNotExist:
                    Tag(value=v).save()
            for v in get_unique_string_values(ws, headers.index('Genres') + 1):
                try:
                    Genre.objects.get(value=v)
                except guerrilla_television.models.Genre.DoesNotExist:
                    Genre(value=v).save()
            for v in get_unique_string_values(ws, headers.index('Languages') + 1):
                try:
                    Language.objects.get(value=v)
                except guerrilla_television.models.Language.DoesNotExist:
                    Language(value=v).save()
            for v in get_unique_string_values(ws, headers.index('Producers') + 1):
                try:
                    Producer.objects.get(value=v)
                except guerrilla_television.models.Producer.DoesNotExist:
                    Producer(value=v).save()
            for v in get_unique_string_values(ws, headers.index('Collections') + 1):
                try:
                    Collection.objects.get(value=v)
                except guerrilla_television.models.Collection.DoesNotExist:
                    Collection(value=v).save()

            for r in range(2, ws.max_row+1): 
                # title
                title = clean_string_value(
                    ws.cell(row=r, column=headers.index('Title') + 1).value
                )

                # get video_tape_format.
                pk = clean_integer_value(ws.cell(row=r, column=headers.index('video_tape_format') + 1).value)
                if pk == None:
                    video_tape_format = None
                else:
                    video_tape_format = VideoTapeFormat.objects.get(pk=pk)

                # post modified date.
                post_modified_date = ws.cell(row=r, column=headers.index('Post Modified Date') + 1).value
                post_modified_date = post_modified_date.replace(tzinfo=pytz.timezone('America/Chicago'))

                # create new item page.
                item = GuerrillaTelevisionItem(
                    title = title,
                    content = clean_string_value(
                        ws.cell(row=r, column=headers.index('Content') + 1).value
                    ),
                    excerpt = clean_string_value(
                        ws.cell(row=r, column=headers.index('Excerpt') + 1).value
                    ),
                    permalink = clean_string_value(
                        ws.cell(row=r, column=headers.index('Permalink') + 1).value
                    ),
                    additional_copies = clean_string_value(
                        ws.cell(row=r, column=headers.index('additional_copies') + 1).value
                    ),
                    color = clean_string_value(
                        ws.cell(row=r, column=headers.index('color') + 1).value
                    ),
                    control_number = clean_integer_value(
                        ws.cell(row=r, column=headers.index('control_number') + 1).value
                    ),
                    date_notation = clean_string_value(
                        ws.cell(row=r, column=headers.index('date_notation') + 1).value
                    ),
                    number_of_reels = clean_string_value(
                        ws.cell(row=r, column=headers.index('number_of_reels') + 1).value
                    ),
                    running_time = clean_string_value(
                        ws.cell(row=r, column=headers.index('running_time') + 1).value
                    ),
                    sound = clean_integer_value(
                        ws.cell(row=r, column=headers.index('sound') + 1).value
                    ),
                    video_tape_format=video_tape_format,
                    wpzoom_post_embed_code = clean_string_value(
                        ws.cell(row=r, column=headers.index('wpzoom_post_embed_code') + 1).value
                    ),
                    general_note = clean_string_value(
                        ws.cell(row=r, column=headers.index('general_note') + 1).value
                    ),
                    staff_comments = clean_string_value(
                        ws.cell(row=r, column=headers.index('staff_comments') + 1).value
                    ),
                    old_number = clean_string_value(
                        ws.cell(row=r, column=headers.index('old_number') + 1).value
                    ),
                    alternative_titles = clean_string_value(
                        ws.cell(row=r, column=headers.index('alternative_titles') + 1).value
                    ),
                    titles_on_reel = clean_string_value(
                        ws.cell(row=r, column=headers.index('titles_on_reel') + 1).value
                    ),
                    main_credits = clean_string_value(
                        ws.cell(row=r, column=headers.index('main_credits') + 1).value
                    ),
                    additional_credits = clean_string_value(
                        ws.cell(row=r, column=headers.index('additional_credits') + 1).value
                    ),
                    performers = clean_string_value(
                        ws.cell(row=r, column=headers.index('performers') + 1).value
                    ),
                    location_of_production = clean_string_value(
                        ws.cell(row=r, column=headers.index('location_of_production') + 1).value
                    ),
                    generation = clean_integer_value(
                        ws.cell(row=r, column=headers.index('generation') + 1).value
                    ),
                    video_start_point = clean_string_value(
                        ws.cell(row=r, column=headers.index('video_start_point') + 1).value
                    ),
                    condition = clean_string_value(
                        ws.cell(row=r, column=headers.index('condition') + 1).value
                    ),
                    acquisition_source = clean_string_value(
                        ws.cell(row=r, column=headers.index('acquisition_source') + 1).value
                    ),
                    actions = clean_string_value(
                        ws.cell(row=r, column=headers.index('actions') + 1).value
                    ),
                    main_contributors = clean_string_value(
                        ws.cell(row=r, column=headers.index('main_contributors') + 1).value
                    ),
                    corporate_names = clean_string_value(
                        ws.cell(row=r, column=headers.index('corporate_names') + 1).value
                    ),
                    document_assets = clean_string_value(
                        ws.cell(row=r, column=headers.index('document_assets') + 1).value
                    ),
                    related_items = clean_string_value(
                        ws.cell(row=r, column=headers.index('related_items') + 1).value
                    ),
                    related_records = clean_string_value(
                        ws.cell(row=r, column=headers.index('related_records') + 1).value
                    ),
                    vimeo_id = clean_string_value(
                        ws.cell(row=r, column=headers.index('vimeo_id') + 1).value
                    ),
                    status = clean_string_value(
                        ws.cell(row=r, column=headers.index('Status') + 1).value
                    ),
                    post_modified_date = post_modified_date
                )
                item.save()

                # get many to many fields. 
                for v in clean_and_split_string_value(
                    ws.cell(row=r, column=headers.index('URL') + 1).value
                ):
                    item.urls.add(URL.objects.get(value=v))
                for v in clean_and_split_string_value(
                    ws.cell(row=r, column=headers.index('Categories') + 1).value
                ):
                    item.categories.add(Category.objects.get(value=v))
                for v in clean_and_split_string_value(
                    ws.cell(row=r, column=headers.index('Tags') + 1).value
                ):
                    item.tags.add(Tag.objects.get(value=v))
                for v in clean_and_split_string_value(
                    ws.cell(row=r, column=headers.index('Genres') + 1).value
                ):
                    item.genres.add(Genre.objects.get(value=v))
                for v in clean_and_split_string_value(
                    ws.cell(row=r, column=headers.index('Languages') + 1).value
                ):
                    item.languages.add(Language.objects.get(value=v))
                for v in clean_and_split_string_value(
                    ws.cell(row=r, column=headers.index('Producers') + 1).value
                ):
                    item.producers.add(Producer.objects.get(value=v))
                for v in clean_and_split_string_value(
                    ws.cell(row=r, column=headers.index('Collections') + 1).value
                ):
                    item.collections.add(Collection.objects.get(value=v))

                item.save()

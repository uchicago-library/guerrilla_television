from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.search import index

class URL(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    value = models.URLField(
        blank = True,
        null = True
    )
    def __str__(self):
        return self.value

class Category(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    value = models.CharField(
        blank = True,
        max_length = 255
    )
    def __str__(self):
        return self.value
    class Meta:
        verbose_name_plural = 'categories'

class Tag(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    value = models.CharField(
        blank = True,
        max_length = 255
    )
    def __str__(self):
        return self.value

class Genre(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    value = models.CharField(
        blank = True,
        max_length = 255
    )
    def __str__(self):
        return self.value

class Language(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    value = models.CharField(
        blank = True,
        max_length = 255
    )
    def __str__(self):
        return self.value

class Producer(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    value = models.CharField(
        blank = True,
        max_length = 255
    )
    def __str__(self):
        return self.value

class Collection(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    value = models.CharField(
        blank = True,
        max_length = 255
    )
    def __str__(self):
        return self.value

class ProductionDate(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    value = models.CharField(
        blank = True,
        max_length = 255
    )
    def __str__(self):
        return self.value

class VideoTapeFormat(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    value = models.CharField(
        blank = True,
        max_length = 255
    )
    def __str__(self):
        return self.value

class GuerrillaTelevisionItem(models.Model):
    """Guerrilla Television Item"""

    id = models.AutoField(
        primary_key=True
    )
    title = models.TextField(
        blank = True
    )
    content = models.TextField(
        blank = True
    )
    excerpt = models.TextField(
        blank = True
    )
    permalink = models.URLField(
        blank = True
    )
    urls = models.ManyToManyField(
        URL,
        blank = True,
        null = True
    )
    categories = models.ManyToManyField(
        Category,
        blank = True,
        null = True
    )
    tags = models.ManyToManyField(
        Tag,
        blank = True,
        null = True
    )
    genres = models.ManyToManyField(
        Genre,
        blank = True,
        null = True
    )
    languages = models.ManyToManyField(
        Language,
        blank = True,
        null = True
    )
    producers = models.ManyToManyField(
        Producer,
        blank = True,
        null = True
    )
    collections = models.ManyToManyField(
        Collection,
        blank = True,
        null = True
    )
    production_dates = models.ManyToManyField(
        ProductionDate,
        blank = True,
        null = True
    )
    additional_copies = models.TextField(
        blank = True
    )
    color = models.TextField(
        blank = True
    )
    control_number = models.IntegerField(
        blank = True,
        null = True
    )
    date_notation = models.TextField(
        blank = True
    )
    number_of_reels = models.TextField(
        blank = True
    )
    running_time = models.TextField(
        blank = True
    )
    sound = models.IntegerField(
        blank = True,
        null = True
    )
    video_tape_format = models.ForeignKey(
        'VideoTapeFormat',
        blank = True,
        null = True,
        on_delete=models.SET_NULL
    )
    wpzoom_post_embed_code = models.TextField(
        blank = True
    )
    general_note = models.TextField(
        blank = True
    )
    staff_comments = models.TextField(
        blank = True
    )
    old_number = models.TextField(
        blank = True
    )
    alternative_titles = models.TextField(
        blank = True
    )
    titles_on_reel = models.TextField(
        blank = True
    )
    main_credits = models.TextField(
        blank = True
    )
    additional_credits = models.TextField(
        blank = True
    )
    performers = models.TextField(
        blank = True
    )
    location_of_production = models.TextField(
        blank = True
    )
    generation = models.IntegerField(
        blank = True,
        null = True
    ) 
    video_start_point = models.TextField(
        blank = True
    )
    condition = models.TextField(
        blank = True 
    )
    acquisition_source = models.TextField(
        blank = True
    )
    actions = models.TextField(
        blank = True
    )
    main_contributors = models.TextField(
        blank = True
    )
    corporate_names = models.TextField(
        blank = True
    )
    document_assets = models.TextField(
        blank = True
    )
    related_items = models.TextField(
        blank = True
    )
    related_records = models.TextField(
        blank = True
    )
    vimeo_id = models.CharField(
        blank = True,
        max_length = 255,
        null = True
    )
    status = models.CharField(
        blank = True,
        choices = (('publish', 'publish'), ('private', 'private')),
        max_length = 255,
        null = True
    )
    post_modified_date = models.DateTimeField(
        blank = True,
        null = True
    )

    # JEJ TODO return to this. 
    # how to deal with fields that are foreign keys?
    '''
    search_fields = Page.search_fields + [
        index.SearchField('content'),
        index.SearchField('excerpt'),
        index.SearchField('permalink'),
        # URL
        # Categories
        # Tags
        # Genres
        # Languages
        # Producers
        # Collections
        # Production Dates
        index.SearchField('additional_copies'),
        index.SearchField('color'),
        index.SearchField('control_number'),
        index.SearchField('date_notation'),
        index.SearchField('number_of_reels'),
        index.SearchField('running_time'),
        index.SearchField('sound'),
        # Video Tape Format
        index.SearchField('wpzoom_post_embed_code'),
        index.SearchField('general_note'),
        index.SearchField('staff_comments'),
        index.SearchField('old_number'),
        index.SearchField('alternative_titles'),
        index.SearchField('titles_on_reel'),
        index.SearchField('main_credits'),
        index.SearchField('additional_credits'),
        index.SearchField('performers'),
        index.SearchField('location_of_production'),
        index.SearchField('generation'),
        index.SearchField('video_start_point'),
        index.SearchField('condition'),
        index.SearchField('acquisition_source'),
        index.SearchField('actions'),
        index.SearchField('main_contributors'),
        index.SearchField('corporate_names'),
        index.SearchField('document_assets'),
        index.SearchField('related_items'),
        index.SearchField('related_records'),
        index.SearchField('vimeo_id'),
        index.SearchField('status'),
        index.SearchField('post_modified_date')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('content'),
        FieldPanel('excerpt'),
        FieldPanel('permalink'),
        # URL
        # Categories
        # Tags
        # Genres
        # Languges
        # Producers
        # Collections
        # Production Dates
        FieldPanel('additional_copies'),
        FieldPanel('color'),
        FieldPanel('control_number'),
        FieldPanel('date_notation'),
        FieldPanel('number_of_reels'),
        FieldPanel('running_time'),
        FieldPanel('sound'),
        FieldPanel('wpzoom_post_embed_code'),
        FieldPanel('general_note'),
        FieldPanel('staff_comments'),
        FieldPanel('old_number'),
        FieldPanel('alternative_titles'),
        FieldPanel('titles_on_reel'),
        FieldPanel('main_credits'),
        FieldPanel('additional_credits'),
        FieldPanel('performers'),
        FieldPanel('location_of_production'),
        FieldPanel('generation'),
        FieldPanel('video_start_point'),
        FieldPanel('condition'),
        FieldPanel('acquisition_source'),
        FieldPanel('actions'),
        FieldPanel('main_contributors'),
        FieldPanel('corporate_names'),
        FieldPanel('document_assets'),
        FieldPanel('related_items'),
        FieldPanel('related_records'),
        FieldPanel('vimeo_id'),
        FieldPanel('status'),
        FieldPanel('post_modified_date')
    ]
    '''

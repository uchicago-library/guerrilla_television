from .models import (Category, Collection, Genre, GuerrillaTelevisionItem,
                     Language, Producer, ProductionDate, Tag, URL,
                     VideoTapeFormat)

from wagtail.admin.panels import (FieldPanel, MultipleChooserPanel)
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, 
    modeladmin_register,
)

class CategoryAdmin(ModelAdmin):
    """Category admin."""

    model = Category
    menu_label = 'Categories'
    menu_icon = 'doc-full'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'value',
    )
    search_fields = (
        'value',
    )

    panels = (
        FieldPanel('value'),
    )
modeladmin_register(CategoryAdmin)

class CollectionAdmin(ModelAdmin):
    """Collection admin."""

    model = Collection
    menu_label = 'Collections'
    menu_icon = 'doc-full'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'value',
    )
    search_fields = (
        'value',
    )

    panels = (
        FieldPanel('value'),
    )
modeladmin_register(CollectionAdmin)

class GenreAdmin(ModelAdmin):
    """Genre admin."""

    model = Genre
    menu_label = 'Genres'
    menu_icon = 'doc-full'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'value',
    )
    search_fields = (
        'value',
    )

    panels = (
        FieldPanel('value'),
    )
modeladmin_register(GenreAdmin)

class GuerrillaTelevisionItemAdmin(ModelAdmin):
    """GuerrillaTelevisionItem admin."""

    model = GuerrillaTelevisionItem
    menu_label = 'GuerrillaTelevisionItems'
    menu_icon = 'doc-full-inverse'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'id',
        'title',
    )
    search_fields = (
        #'value',
    )

    panels = (
        FieldPanel('title'),
        FieldPanel('content'),
        FieldPanel('excerpt'),
        FieldPanel('permalink'),
        # JEJ return to these.
        FieldPanel('urls'),
        FieldPanel('categories'),
        FieldPanel('tags'),
        FieldPanel('genres'),
        FieldPanel('languages'),
        FieldPanel('producers'),
        FieldPanel('collections'),
        FieldPanel('production_dates'),
        # JEJ end return to these.
        FieldPanel('additional_copies'),
        FieldPanel('color'),
        FieldPanel('control_number'),
        FieldPanel('date_notation'),
        FieldPanel('number_of_reels'),
        FieldPanel('running_time'),
        FieldPanel('sound'),
        # JEJ return to this.
        FieldPanel('video_tape_format'),
        # JEJ end return to this.
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
        FieldPanel('actions'),
        FieldPanel('main_contributors'),
        FieldPanel('corporate_names'),
        FieldPanel('document_assets'),
        FieldPanel('related_items'),
        FieldPanel('related_records'),
        FieldPanel('vimeo_id'),
        # JEJ constrain to a few options? 
        FieldPanel('status'),
        # JEJ date chooser here? 
        FieldPanel('post_modified_date'),
    )
modeladmin_register(GuerrillaTelevisionItemAdmin)

class LanguageAdmin(ModelAdmin):
    """Language admin."""

    model = Language
    menu_label = 'Languages'
    menu_icon = 'doc-full'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'value',
    )
    search_fields = (
        'value',
    )

    panels = (
        FieldPanel('value'),
    )
modeladmin_register(LanguageAdmin)

class ProducerAdmin(ModelAdmin):
    """Producer admin."""

    model = Producer
    menu_label = 'Producers'
    menu_icon = 'doc-full'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'value',
    )
    search_fields = (
        'value',
    )

    panels = (
        FieldPanel('value'),
    )
modeladmin_register(ProducerAdmin)

class ProductionDateAdmin(ModelAdmin):
    """ProductionDate admin."""

    model = ProductionDate
    menu_label = 'ProductionDates'
    menu_icon = 'doc-full'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'value',
    )
    search_fields = (
        'value',
    )

    panels = (
        FieldPanel('value'),
    )
modeladmin_register(ProductionDateAdmin)

class TagAdmin(ModelAdmin):
    """Tag admin."""

    model = Tag
    menu_label = 'Tags'
    menu_icon = 'doc-full'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'value',
    )
    search_fields = (
        'value',
    )

    panels = (
        FieldPanel('value'),
    )
modeladmin_register(TagAdmin)

class URLAdmin(ModelAdmin):
    """URL admin."""

    model = URL
    menu_label = 'URLs'
    menu_icon = 'doc-full'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'value',
    )
    search_fields = (
        'value',
    )

    panels = (
        FieldPanel('value'),
    )
modeladmin_register(URLAdmin)

class VideoTapeFormatAdmin(ModelAdmin):
    """VideoTapeFormat admin."""

    model = VideoTapeFormat
    menu_label = 'VideoTapeFormats'
    menu_icon = 'doc-full'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'value',
    )
    search_fields = (
        'value',
    )

    panels = (
        FieldPanel('value'),
    )
modeladmin_register(VideoTapeFormatAdmin)

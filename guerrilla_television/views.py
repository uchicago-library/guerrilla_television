from django.http import HttpResponse
from django.shortcuts import render
from guerrilla_television.models import GuerrillaTelevisionItem

def object(request, id):
    # look up the GuerrillaTelevisionItem object, use id.
    # this works...

    object = GuerrillaTelevisionItem.objects.get(pk=id)

    vimeo_id = object.vimeo_id
    title = object.title

    creator = ' ; '.join([p.value for p in object.producers.all()])
    if object.main_credits:
        creator = creator + '; ' + object.main_credits
    if object.additional_credits:
        creator = creator + '; ' + object.additional_credits

    production_dates = ' ; '.join([d.value for d in object.production_dates.all()])
    
    video_tape_format = object.video_tape_format.value
    genres = ' ; '.join([g.value for g in object.genres.all()])
    excerpt = object.excerpt
    categories = ' ; '.join([c.value for c in object.categories.all()])
    location_of_production = object.location_of_production

    collections = ' ; '.join([c.value for c in object.collections.all()])
     
    return render(
        request, 
        'object.html', 
        context={
            'id': id,
            'vimeo_id': vimeo_id,
            'title': title,
            'creator': creator,
            'production_dates': production_dates,
            'video_tape_format': video_tape_format,
            'genres': genres,
            'excerpt': excerpt,
            'categories': categories,
            'location_of_production': location_of_production,
            'collections': collections
        }
    )

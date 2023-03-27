from django.http import HttpResponse
from django.shortcuts import render

def object(request, id):
    # look up the GuerrillaTelevisionItem object, use id.
    # this works...

    vimeo_id = 'vimeo id'
    title = 'title'
    main_contributors = 'main contributors'
    date_notation = 'date notation'
    video_tape_format = 'video tape format'
    location_of_production = 'location of production'
    collection = 'collection'
     
    return render(
        request, 
        'object.html', 
        context={
            'id': id,
            'vimeo_id': vimeo_id,
            'title': title,
            'main_contributors': main_contributors,
            'date_notation': date_notation,
            'video_tape_format': video_tape_format,
            'location_of_production': location_of_production,
            'collection': collection
        }
    )

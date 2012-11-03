from django.shortcuts import render
from models import Show, Performer

def index (request):
  shows = Show.objects.all()
  num_shows = len(shows)
  return render(request, 'show/index.html', {'shows':shows,
                                             'num_shows':num_shows,
                                            }, content_type="text/html")

def detail (request, show_id):
  show = Show.objects.get(id=show_id)
  performers = show.performers.all()
  return render(request, 'show/detail.html', {'show':show,
                                              'performers':performers,
                                             }, content_type="text/html")

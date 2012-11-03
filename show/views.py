from django.shortcuts import render
from models import Show, Performer

def index (request):
  shows = Show.objects.all()
  num_shows = len(shows)
  return render(request, 'show/index.html', {'shows':shows,
                                             'num_shows':num_shows,
                                            }, content_type="text/html")

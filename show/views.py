from django.shortcuts import render, HttpResponse
from models import Show, Performer
from datetime import datetime

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
def add (request, date_str):
  try:
    date_object = datetime.strptime(date_str)
    show = Show(date=date_object)
    show.save()

    return HttpResponse(show.id)
  except e:
    print e
    return HttpResponse("ERR")

def add_performer (request, user_id, r, show_id):
  try:
    u = User.get(id=user_id)
    created, p = Performer.get_or_create(user=u, role=r)
    show.performers.add(p)
    return HttpResponse("OK")
  except e:
    print e
    return HttpResponse("ERR")



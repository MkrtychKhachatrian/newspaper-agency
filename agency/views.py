from django.shortcuts import render

from agency.models import Redactor, Newspaper, Topic


def index(request):
    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()

    context = {
       "num_drivers": num_redactors,
       "num_cars": num_newspapers,
       "num_manufacturers": num_topics,
    }

    return render(request, "agency/index.html", context=context)

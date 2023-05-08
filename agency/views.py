from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from agency.models import Redactor, Newspaper, Topic


@login_required
def index(request):
    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()

    context = {
       "num_redactors": num_redactors,
       "num_newspapers": num_newspapers,
       "num_topics": num_topics,
    }

    return render(request, "agency/index.html", context=context)

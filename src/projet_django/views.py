from datetime import datetime
from django.shortcuts import render


def index(request):
    date = datetime.today()

    return render(request, "projet_django/index.html", context={"date": date})
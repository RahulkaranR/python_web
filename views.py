from django.shortcuts import render
import datetime
# Create your views here.
ls = []

for i in range(10):
    ls.append(i)
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear" : now.date != 1 and now.month != 1,
        "loo": ls
    })


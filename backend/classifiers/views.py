from django.shortcuts import render


def classifiers(request):
    return render(request, "classifiers_home.html")

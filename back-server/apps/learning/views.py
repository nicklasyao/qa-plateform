from django.shortcuts import render


# Create your views here.
def leaning_home(request):
    return render(request, "doc_index.html")

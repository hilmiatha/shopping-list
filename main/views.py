from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Hilmi Atha Putra',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
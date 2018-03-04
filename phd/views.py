from django.shortcuts import render

# Create your views here.
def substrat_list(request):
    return render(request, 'phd/substrat_list.html', {})

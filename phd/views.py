from django.shortcuts import render
from django.http import Http404
from django.db.models import Avg

from .models import Substrate, Tensiometrie


# Create your views here.
def substrate_list(request):
    substrates = Substrate.objects.all().order_by('date_treatment')
    return render(
        request, 'phd/substrate_list.html', {'substrates': substrates}
    )


def substrate_detail(request, pk):
    try:
        substrate = Substrate.objects.get(pk=pk)
        t_st = Tensiometrie.objects.filter(
            substrate=substrate, method="st").order_by('serie')
        t_ad = Tensiometrie.objects.filter(
            substrate=substrate, method="ad").order_by('serie')
        t_re = Tensiometrie.objects.filter(
            substrate=substrate, method="re").order_by('serie')
        """
        avg_st = Tensiometrie.objects.filter(
            substrate=substrate, method="st").order_by(
            'serie').aggregrate(Avg('left'))
        avg_ad = Tensiometrie.objects.filter(
            substrate=substrate, method="ad").order_by('serie')
        avg_re = Tensiometrie.objects.filter(
            substrate=substrate, method="re").order_by('serie')
        """
    except Substrate.DoesNotExist:
        raise Http404("substrate does not exit")
    return render(
        request, 'phd/substrate_detail.html',
        {'substrate': substrate, 't_st': t_st, 't_ad': t_ad, 't_re': t_re}
    )

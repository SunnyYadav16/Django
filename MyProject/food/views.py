from django.shortcuts import render
from django.http import HttpResponse
from .models import Items


# Create your views here.
def index(request):
    item_list = Items.objects.all()
    context = {
        "item_list": item_list,
    }
    return render(request, 'food/index.html', context)


def detail_view(request, item_id):
    item = Items.objects.get(id=item_id)
    context = {
        "item": item,
    }
    return render(request, 'food/detail.html', context)

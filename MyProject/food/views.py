from django.shortcuts import render, redirect
from .models import Items
from .forms import ItemForm


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


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    context = {
        "form": form,
    }
    return render(request, 'food/item_form.html', context)


def update_item(request, item_id):
    item = Items.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    context = {
        "form": form,
        "item": item,
    }
    return render(request, 'food/item_form.html', context)


def delete_item(request, item_id):
    item = Items.objects.get(id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    context = {
        "item": item,
    }
    return render(request, 'food/item_delete.html', context)
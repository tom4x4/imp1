from django.shortcuts import render
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .models import Apteki
from .tables import AptekiTable

# class Tabelka(SingleTableView):
#     model = Apteki
#     table_class = AptekiTable
#     template_name = 'app1/tabelka_view.html'

def tabelka_view(request):
    table = AptekiTable(Apteki.objects.all())

    return render(request, 'app1/tabelka_view.html', {
        'table' :table
    })

#def item_edit(self,record):
    #return mark_safe('<a href='+reverse("edit", args=[record.pk])+'>Edit</a>')

def item_edit(record):
    return ('ala'+ record)




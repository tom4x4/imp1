from django.shortcuts import render
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .models import Apteki
from .models import Bloz
from .tables import AptekiTable

# class Tabelka(SingleTableView):
#     model = Apteki
#     table_class = AptekiTable
#     template_name = 'app1/tabelka_view.html'

def client_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    return ip

def index_view(request):
    return render(request, 'app1/index.html', )



def tabelka_view(request):
    table = AptekiTable(Apteki.objects.all())

    return render(request, 'app1/tabelka_view.html', {
        'table' :table, 'IP': client_ip(request),
    })

def search_Bloz(request):
    # if request.method== 'POST':
    #     pass
    lek = Bloz.objects.get(pk='3002551')
    return render(request, 'app1/search_Bloz.html', {'lek':lek})


#def item_edit(self,record):
    #return mark_safe('<a href='+reverse("edit", args=[record.pk])+'>Edit</a>')

def item_edit(record):
    return ('ala'+ record)




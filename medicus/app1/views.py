from django.shortcuts import render
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .models import Apteki
from .models import Bloz
from .tables import AptekiTable
from .forms import Wyszukaj

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
    #lek = Bloz.objects.get(pk='3002551')
    return render(request, 'app1/search_Bloz.html', {'lek':lek})

def wyszukaj(request):
    if request.method == 'POST':
        form = Wyszukaj(request.POST)
        kod077=request.POST.get('kod07')
        form = Wyszukaj()

    else:
        form= Wyszukaj()
        kod077=""

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1


    return render(request,'app1/wyszukaj.html',{'form':form,'kod077':kod077,'num_visits':num_visits})


#def item_edit(self,record):
    #return mark_safe('<a href='+reverse("edit", args=[record.pk])+'>Edit</a>')

def item_edit(record):
    return ('ala'+ record)


#pk='3002551'

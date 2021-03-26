import django_tables2 as tables

from .models import Apteki

class AptekiTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor="pk")
    class Meta:
        model = Apteki



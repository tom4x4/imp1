import django_tables2 as tables
from django_tables2.utils import A # alias for Accessor
import itertools

from .models import Apteki


class AptekiTable(tables.Table):
    #selection = tables.CheckBoxColumn(accessor="pk")
    #apteka = tables.LinkColumn("item_edit", text=lambda record: record.apteka, args=[A("pk")])
    apteka = tables.LinkColumn("item_edit", text=lambda record: record.apteka)
    edit = tables.TemplateColumn('<form action="aaa" method="post"><input type="button" name="gender" value="other"></form>')

    class Meta:
        model = Apteki
        template_name = "django_tables2/bootstrap4.html"



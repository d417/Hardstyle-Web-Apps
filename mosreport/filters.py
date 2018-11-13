from django_filters import filters
from django_filters import FilterSet
from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):
    mon = filters.ChoiceFilter(label='提出月', lookup_expr='contains')
    name = filters.CharFilter(label='氏名', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('mon', '提出月'),
            ('name', '氏名'),            
        ),
        field_labels={
            'mon': '提出年月',
            'name': '氏名',
        },
        label='並び順'
    )

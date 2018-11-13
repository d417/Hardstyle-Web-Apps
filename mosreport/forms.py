from django import forms
from .models import Item
from django.forms import widgets

MON_CHOICES = (
    ('1月', '1月'),
    ('2月', '2月'),
    ('3月', '3月'),
    ('4月', '4月'),
    ('5月', '5月'),
    ('6月', '6月'),
    ('7月', '7月'),
    ('8月', '8月'),
    ('9月', '9月'),
    ('10月', '10月'),
    ('11月', '11月'),
    ('12月', '12月'),
)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('mon', 'name','locale','projectstatus')
        widgets = {
                    'mon': widgets.Select(choices=MON_CHOICES),
                    'name': forms.TextInput(attrs={'placeholder':'記入例：山田　太郎'}),
                    'locale': forms.TextInput(attrs={'placeholder':'記入例：自社/人形町'}),
                    'projectstatus': forms.Textarea(attrs={'rows':4}),
                  }

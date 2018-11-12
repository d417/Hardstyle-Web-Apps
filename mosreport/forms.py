from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name','locale','projectstatus')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'記入例：山田　太郎'}),
                    'locale': forms.TextInput(attrs={'placeholder':'記入例：自社/人形町'}),
                    'projectstatus': forms.Textarea(attrs={'rows':4}),
                  }
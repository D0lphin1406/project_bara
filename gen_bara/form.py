from django import forms


class BaraForm(forms.Form):
    bara = forms.CharField(label='Введите штрих-код', min_length=8, max_length=50)
    name = forms.CharField(label='Введите наименование товара', min_length=0, max_length=50)
    art = forms.CharField(label='Введите артикул товара', min_length=0, max_length=50)



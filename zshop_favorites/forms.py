from django import forms

class FavoritProductForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput(),

    )

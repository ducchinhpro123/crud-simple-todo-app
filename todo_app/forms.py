from django import forms
from .models import Todo


class TodoForm(forms.Form):
    title = forms.CharField(max_length=100, label="Tittle")
    description = forms.CharField(max_length=200, label="Description",
                                  widget=forms.Textarea(attrs={"cols": "20", "rows": "5"}))

from django import forms
from .models import My_pdf

class BookForm(forms.ModelForm):
    class Meta:
        model = My_pdf
        fields = ('semester', 'subject', 'pdf','image')
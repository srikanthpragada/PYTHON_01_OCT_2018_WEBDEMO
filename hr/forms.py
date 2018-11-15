from django import forms
from . models import  Book
# import django.forms as forms


class AddJobForm(forms.Form):
    jobid = forms.CharField(label="Job ID", max_length=10)
    jobtitle = forms.CharField(max_length=20, label="Job Title")
    minsal = forms.IntegerField(label="Minimum Salary")


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','price']



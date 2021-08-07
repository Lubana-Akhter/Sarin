from django import forms
from myapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class EmailForm(forms.Form):
    email = forms.EmailField(max_length = 100, widget = forms.TextInput(attrs={'class':'form-control col-sm-4', 'placeholder':'email'}))
    subject = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'class':'form-control col-sm-4', 'placeholder':'subject'}))
    message = forms.CharField(required = False,max_length = 200, widget = forms.Textarea(attrs={'class':'form-control col-sm-4'}),label = ('  '))
    attach =  forms.FileField(required = False,widget=forms.ClearableFileInput(attrs={'multiple': True}))
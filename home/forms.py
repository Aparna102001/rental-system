from django import forms
from .models import bookdetails
#from django.core import validators

#class SlotForm(forms.ModelForm):
    #time_field = forms.TimeField(validators=[validators.TimeValidator()])
    #class Meta:
        #model = bookdetails
        #fields = ('date1','date2' ,'fro','to','pickup')
        #widgets = {

            #'fro':forms.TextInput(attrs={'type':'text'}),
            #'to': forms.TextInput(attrs={'type':'text'}),
            #'date1': forms.DateInput(attrs={'type': 'date'}),
            #'date2': forms.DateInput(attrs={'type': 'date'}),
            #'pickup': forms.TimeInput(attrs={'type': 'time'}),
    
        #}
from . models import Vehicle
class Travel_view(forms.ModelForm):
    class Meta:
      model = Vehicle
      fields = ['name','number','driver','type','fare','seats','image']
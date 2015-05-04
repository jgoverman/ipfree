from django import forms
from ipfree.models import Machine


class IPSearch(forms.Form):
    ipaddress = forms.GenericIPAddressField(help_text="Please enter the IP Address.") 
   
    #class Meta:
	#model = Machine
	#fields = ('ipaddress',)

class AddIP(forms.ModelForm):
    hostname = forms.CharField(max_length=128, help_text="Hostname")
    description = forms.CharField(help_text="Description")
    ipaddress = forms.GenericIPAddressField(help_text="IP Address")
    #ostype = forms.CharField(widget=forms.CheckboxSelectMultiple, choices=(("Ubuntu_Linux", "Ubuntu Linux"),("Windows", "Windows"),("ACOS", "ACOS")))
    ostype = forms.CharField(widget=forms.HiddenInput(), initial="Ubuntu_Linux")

    #def __unicode__(self):
    #    return self.hostname

    #def __unicode__(self):
    #    return self.description    

    class Meta:
	model = Machine
	fields = ('hostname','description','ipaddress','ostype')



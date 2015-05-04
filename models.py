from django.db import models

class Machine(models.Model):
	hostname = models.CharField(max_length=128, unique=True, blank=False)
        description = models.CharField(max_length=1024, blank=True, null=True)
        ipaddress = models.GenericIPAddressField(unique=True)
	ostype = models.CharField(max_length=128, choices=(("Ubuntu_Linux", "Ubuntu Linux"),("Windows", "Windows"),("ACOS", "ACOS")))

	
        def __unicode__(self):
	    return self.hostname 

        def __unicode__(self):
	    return self.description
	
	def __unicode__(self):
	    return self.ipaddress



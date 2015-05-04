from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import logging
# Debug package
import pdb
from ipfree.models import Machine
from ipfree.forms import IPSearch, AddIP

def search(request):
     # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        # create a form instance and populate with data from the request
        form = IPSearch(request.POST)
	if form.is_valid():
	    myip = form.cleaned_data['ipaddress']
	    ipthere = Machine.objects.filter(ipaddress__exact=myip)
	    if ipthere:
  		return render_to_response('ipfree/ipfree.html', {'form' : form, 'ipthere' : ipthere}, context)
	    	#return HttpResponse(mac)
	    else:
		return render_to_response('ipfree/ipfree.html', {'form' : form, 'myip' : myip}, context)    
	#else:
            # The supplied form contained errors - just print them to the terminal.
        #    print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = IPSearch()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('ipfree/ipfree.html', {'form' : form}, context)    
    

def addip(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        # create a form instance and populate with data from the request
        form = AddIP(request.POST)
        print ('Pre-form')
	#Debug if we need too
	#pdb.set_trace()
	if form.is_valid():
	    # Save the new category to the database.
	    print ('Form is valid')
	    form.save()
	    #formsave == TRUE
	    #hostname = form.cleaned_data['hostname']
	    #description = form.cleaned_data['description']
	    #ostype = form.cleaned_data['ostype']
	    #return render_to_response('ipfree/ipadd.html', {'form' : form}, context)
	    return render_to_response('ipfree/ipadd.html', {'form' : form}, context)
	else:
	    print('Form is invalid')
	    logging.debug('Form is invalid!')
    else:
        # If the request was not a POST, display the form to enter details.
        form = AddIP()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('ipfree/ipadd.html', {'form' : form}, context)



def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}


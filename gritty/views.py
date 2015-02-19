from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.template import Template,Context,RequestContext
from django.core.context_processors import csrf

def home(request):
	d = {} 
	return render_to_response('home.html',d,context_instance=RequestContext(request))

def login(request):
	d = {} 
	return render_to_response('login.html',d,context_instance=RequestContext(request))
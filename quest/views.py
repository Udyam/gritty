from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.template import Template,Context
from django.core.context_processors import csrf

@login_required
def list(request):
	'''
		List all the questions in the db
	'''
	
@login_required
def match_ans(request):
	'''
		Matches the answer of the question from the database
	'''
@login_required
def leaderboard(request):
	'''
		Leaderboard for the tournament
	'''

@login_required
def live_stats(request):
	'''
		Question sucess rate order
	'''

# add the logins




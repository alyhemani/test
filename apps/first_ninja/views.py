from django.shortcuts import render, redirect
import random

# Create your views here.

def index(request):
	if 'gold' not in request.session:
		request.session['gold']=0
	if 'log' not in request.session:
		request.session['log']=''
	return render(request, 'first_ninja/index.html')

def process(request):
	if request.method == "POST":
		if 'farm' in request.POST:
			number= random.randrange(10,21)
			request.session['gold']+= number
			request.session['log'] += 'Earned ' +str(number)+ ' gold from the farm!'
		elif 'cave' in request.POST:
			number= random.randrange(5,11)
			request.session['gold']+= number
			request.session['log'] += 'Earned ' +str(number)+ ' gold from the cave!'
		elif 'house' in request.POST:
			number= random.randrange(2,6)
			request.session['gold']+= number
			request.session['log'] += 'Earned ' +str(number)+ ' gold from the house!'
		elif 'casino' in request.POST:
			number= random.randrange(-50,50)
			request.session['gold']+= number
			if number > 0:
				request.session['log'] += 'Earned ' +str(number)+ ' gold from the casino!'
			elif number == 0:
				request.session['log'] += 'Earned 0 gold from the casino!'
			elif number < 0:
				request.session['log'] += 'OUCH!!! Lost ' +str(abs(number))+ ' gold from the casino!'
		return redirect('/')
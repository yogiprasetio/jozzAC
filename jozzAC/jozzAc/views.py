from django.shortcuts import render

def dasboard(request):
	return render(request, 'client/Home.html')
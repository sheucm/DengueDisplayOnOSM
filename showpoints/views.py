from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from importDengueData.models import Dengue_all

# Create your views here.
def show_points(requests):
	dengue_all = Dengue_all.objects.order_by("date")[:10]
	positions = list()
	for dengue in dengue_all:
		positions.append([dengue.lat,dengue.lon])
	return render(requests,
					'testLeaflet.html',
					{'positions': positions})
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from importDengueData.models import Dengue_all


import requests as requ
import csv
# Create your views here.

@csrf_exempt
def importDengueData(request):
	req= requ.get('http://54.65.74.29/file/dengue_all.csv')
	data = req.text
	if data is None:
		return HttpResponse(status = 400)
	reader = csv.reader(data.splitlines(), delimiter=',')
	for index, row in enumerate(reader):
		if index == 0:
			continue
		# django ORM for inserting row[0]~row[6]
		dengue_all = Dengue_all(no = row[0],
							date = row[1],
							area = row[2],
							zone = row[3],
							road = row[4],
							lat = row[5],
							lon = row[6])
		dengue_all.save()
	return HttpResponse(status = 200)
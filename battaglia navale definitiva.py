import requests
import json 
import time
import random

url = 'http://192.168.1.231:8000/signup'
url1 = 'http://192.168.1.231:8000'

def accreditamento(url):

	accr = requests.post(url, json = {"name" : "soos"})
	print(accr.json())

def colpo(url):

	url_info = 'http://192.168.1.231:8000/info'
	info = requests.get(url_info)
	fields = info.json()
	heigh = fields["field"]["h"]
	weidth = fields["field"]["w"]
	distance = 2

	info_grid = requests.get(url_info)
	grids = info_grid.json()
	grid = grids["field"]["grid"]

	time = 0
	x = 0
	y = 0

	while True:

		info_grid = requests.get(url_info)
		grids = info_grid.json()
		grid = grids["field"]["grid"]

		if time == 3:
			time = 0
			y = random.randint(0,height)
			for i in range(len(grid[y])):

				if grid[y][i] == 2:

					x = i + 1
					attack = requests.post(url, json = { "x" : x, "y" : y})

			x = temp_x
			y = temp_y


		else:

			while grid[y][x] != 0:
				x += distance
				y += distance

			attack = requests.post(url, json = { "x" : x, "y" : y})
			time.sleep(3)
			
			if (x + distance) > weidth:

				if (y+1) < heigh:

					y += 1

				x = 0

			temp_x = x
			temp_y = y
			time += 1


accreditamento(url)
colpo(url1)




from place import Place
import numpy as np
import json

class Places_list():

	def __init__(self):
		self.places = []
		self.creat_place()

	def creat_place(self):
		count = 0
		while(True):
			flag = raw_input("Input new place? (yes/no)")
			if flag == 'yes' or flag == 'Yes' or flag == 'y' or flag == 'Y':

				new_place = Place(count)
				self.add_place(new_place)
				count += 1
			else:
				self.make_place_list()
				break

	def add_place(self, new_place):
		self.places.append(new_place)

	def get_place(self, name):
		result = None
		for place in self.places:
			if place.get_name() == name:
				result = place
		return result

	def make_place_list(self):
		for place in self.places:
			for linked_place in place.get_linked_places():
					linked_place['name'] = self.get_place(linked_place['name'])

	def store_places_list(self):
		filename = 'places_list.npy'
		np.save(filename, self.places)

	def places_list_print(self):
		print("All Places: ")
		for place in self.places:
			place.place_print()

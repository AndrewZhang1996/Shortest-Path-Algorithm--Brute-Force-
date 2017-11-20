

class Place():

	def __init__(self, index):

		self.name = ''
		self.set_name()
		self.index = index
		self.linked_places = []
		self.set_linked_places()

	def set_name(self):
		self.name = raw_input("Place Name: ")

	def get_name(self):
		return self.name

	def set_linked_places(self):
		while(True):
			flag = raw_input("Is there linked place to this place? (yes/no)")
			if flag == 'yes' or flag == 'Yes' or flag == 'y' or flag == 'Y':
				linked_place = {}
				linked_place = self.create_linked_place()
				self.linked_places.append(linked_place)
			else:
				break

	def get_linked_places(self):
		return self.linked_places

	def create_linked_place(self):
		linked_place = {}
		place = raw_input("Place Name: ")
		linked_place['name'] = place
		distance = raw_input("Distance: ")
		linked_place['distance'] = distance
		return linked_place

	def get_index(self):
		return self.index

	def place_print(self):
		print("\tPlace Name: " + self.name)
		print("\t\tLinked Places: ")
		for linked_place in self.linked_places:
			print("\t\t\tName: " + str(linked_place['name']))
			print("\t\t\tDistance: " + linked_place['distance'])
		print("\n")






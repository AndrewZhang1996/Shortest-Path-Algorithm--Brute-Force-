from place import Place

class brute_force():

	global all_paths
	all_paths = []	

	def __init__(self, places_list, start, end):
		self.places = places_list
		self.start = start
		self.end = end
		self.paths = []
		self.path = []
		self.get_paths()

	def get_place_name(self, place):
		return place.get_name()

	def get_place(self, name):
		for place in self.places:
			if place.get_name() == name:
				get_place = place
		return get_place

	def get_start_and_end_places(self):
		start_place = self.get_place(self.start)
		end_place = self.get_place(self.end)
		return start_place, end_place

	def get_linked_places(self, place):
		p = place
		linked_places = []
		for linked_place in p.get_linked_places():
			linked_places.append(linked_place['name'])
		return linked_places

	def isInPath(self, place, path):
		flag = False
		for p in path:
			if p == place:
				flag = True
				break
		return flag


	def get_path(self, current_place, previous_place, start_place, end_place):
		next_place = None
		if previous_place != None and current_place != None and previous_place == current_place:
			return False

		if current_place != None:
			i = 0
			self.path.append(current_place)
			if current_place == end_place:
				self.add_path(self.path)
				return True
			else:
				current_linked_places = self.get_linked_places(current_place)
				next_place = current_linked_places[i]
				while next_place != None:
					if previous_place != None and (next_place == start_place or next_place == previous_place or self.isInPath(next_place, self.path)):
						i += 1
						if i >= len(current_linked_places):
							next_place = None
						else:
							next_place = current_linked_places[i]
						continue
					if self.get_path(next_place, current_place, start_place, end_place):
						self.path.pop()
					i += 1
					current_linked_places = self.get_linked_places(current_place)
					if i >= len(current_linked_places):
						next_place = None
					else:
						next_place = current_linked_places[i]
				self.path.pop()
				return False
		else:
			return False

	def add_path(self, path):
		one_path = []
		for p in path:
			one_path.append(p.get_name())
		all_paths.append(one_path)


	def get_paths(self):
		start_place, end_place = self.get_start_and_end_places()
		start_place_namelist = []
		previous_place = start_place
		current_place = None
		final_paths = []

		for linked_place in start_place.get_linked_places():
				start_place_namelist.append(linked_place['name'])

		for first_place in start_place_namelist:
			current_place = first_place
			self.get_path(current_place, previous_place, start_place, end_place)
		for path in all_paths:
			path.insert(0, previous_place.get_name())

	def calculate_distance(self, route):
		total_distance = 0
		route_places = []
		ins_1 = None
		i = 0
		for place in route:
			if i == 0:
				i += 1
				continue
			else:
				route_places.append(place)
		i = 0
		for place in route_places:
			ins_1 = self.get_place(place)
			for linked_place in ins_1.get_linked_places():
				if linked_place['name'].get_name() == route[i]:

					total_distance += int(linked_place['distance'])
			i += 1
		return total_distance

	def routes(self):
		total_paths = []
		total_distances = []
		for P in all_paths:
			total_path = {}
			total_distance = self.calculate_distance(P)
			total_distances.append(total_distance)
			route = ''
			print("Path :")
			for p in P:
				route += p + " "
				total_path['route'] = route
				total_path['distance'] = total_distance
			total_paths.append(total_path)
			print("\t" + route + " " + str(total_distance))
		print("Shortest Path(s): ")
		for path in total_paths:
			if path['distance'] == min(total_distances):
				print(path['route'] + " " + str(path['distance']))






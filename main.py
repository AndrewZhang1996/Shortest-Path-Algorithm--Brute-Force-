from place import Place
from places_list import Places_list
from BruteForce import brute_force
import numpy as np

# new_places_list = Places_list()
# new_places_list.places_list_print()
# new_places_list.store_places_list()
filename = 'places_list.npy'
places = np.load(filename)

start = raw_input("Start: ")
end = raw_input("End: ")

bruteforce = brute_force(places, start, end)
bruteforce.routes()


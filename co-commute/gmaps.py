import settings
import json
import googlemaps
from datetime import datetime

#Python Google Maps API wrapper. MAPS_API_KEY should be an env variable or in a private.py file
gmaps = googlemaps.Client(key=settings.MAPS_API_KEY)

def check_commutes(listing):
    for key, value in settings.CAN_I_GET_TO.items():
        #NOTE: The traffic_model parameter may only be specified for requests where
        #the travel mode is driving, and where the request includes a
        #departure_time.
        travel_time = gmaps.distance_matrix(origins=key, destinations=listing["geotag"], mode=value[1])
        
        #return FALSE if commute time exceeds max acceptable
        if travel_time["rows"][0]["elements"][0]["duration"]["value"] > 60*value[0] :
            return False

    return True


# Commute locations you want to check against.  Every entry will be checked against each listing
# for acceptable travel time.
# dict key is name of location, associated tuple represents (max travel time in minutes, mode of transport)
# Acceptible modes of transport are “driving”, “walking”, “transit” or “bicycling”
CAN_I_GET_TO = {
    "Queens College, NY": (80, "transit"),
    "Cornell Tech, NY": (45, "transit"),
    "Columbia University": (45, "transit")
}


## Price

# minimum rent / month.
MIN_PRICE = 750

# maximum rent / month.
MAX_PRICE = 1500


## Location preferences

# Craigslist greater area site to search on.
CRAIGSLIST_SITE = "newyork"

# Craigslist local area subpage to search on.
AREAS = ["mnh", "que"]


## Search type preferences

# Craigslist housing subsection. "hhh" for all, "aap" for apartments, "roo" for rooms/shares.
CRAIGSLIST_HOUSING_SUBSECTION = 'roo'

# Private settings and API keys are imported here.
try:
    from private import *
except Exception:
    pass

# co-commute
A simple web application that allows users to easily filter Craigslist housing listings by commute time to multiple locations. Created for the purpose of learning Python, as a mentee in the 3rd edition of Learn IT, Girl! (www.learnitgirl.com)

<hr>

<h3>Running the Demo</h3>
An early demo version of co-commute can be run from the command line by doing the following:  

0. Download a copy of the co-commute folder from this repo, and pip install any missing packages listed in requirements.txt.

1. Get an API key from https://developers.google.com/maps/documentation/distance-matrix/get-api-key and set the variable MAPS_API_KEY in private.py equal to your key.

2. Adjust your search parameters in settings.py. <br> The set of locations that listings will be filtered by is stored as a dict in variable CAN_I_GET_TO, with a string representing the address or name of each location as the key, and a value that is a tuple of the maximum acceptable travel time in minutes paired with the type of transportation ("transit", "driving", "bicycling", "walking"). <br><br> Set MAX_PRICE to the maximum monthly rent that you are willing to pay, and MIN_PRICE to the minimum monthly rent you want to see listings for. <br><br> CRAIGSLIST_SITE gets a string containing the part of the URL for the regional Craigslist site being searched that comes immediately before <i>.craigslist.org/</i> So for https://newyork.craigslist.org/ that's "newyork". <br><br>  AREAS is a list of all the local subareas that you want to search in, represented by three letter strings that are listed at the top of your craigslist site's main page, or immediately after <i>.craigslist.org/</i> in your site's URL. For the Manhattan subarea on the New York City site, that's the "mnh" in https://newyork.craigslist.org/mnh/ <br><br> CRAIGSLIST_HOUSING_SUBSECTION is the three letter string representing the type of listing that you want to see: "hhh" for all housing, "aap" for apartments, "roo" for rooms/shares. 

3. From the command line, use python3 to run main.py


  
 

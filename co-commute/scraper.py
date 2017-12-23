from craigslist import CraigslistHousing
from dateutil.parser import parse
from util import post_listing
from gmaps import check_commutes
import time
import settings


def scrape_area(area):
    """
    Scrapes craigslist for newest listings in area
    :param area:
    :return: A list of results.
    """
    cl = CraigslistHousing(site=settings.CRAIGSLIST_SITE, area=area, category=settings.CRAIGSLIST_HOUSING_SUBSECTION,
                             filters={'max_price': settings.MAX_PRICE, "min_price": settings.MIN_PRICE})

    results = []
    some = cl.get_results(sort_by='newest', geotagged=True, limit=50)
    while True:
        try:
            result = next(some)
        except StopIteration:
            break
        except Exception:
            continue

        if result["geotag"] is None:
            continue

        # Parse the price.
        price = 0
        try:
            price = float(result["price"].replace("$", ""))
        except Exception:
            pass

        if check_commutes(result) :
            results.append(result)
    
    return results

def do_scrape():
    """
    Runs the craigslist scraper and posts results.
    """

    # Get all the results from craigslist
    all_results = []
    for area in settings.AREAS:
        all_results += scrape_area(area)

    print("{}: Got {} results".format(time.ctime(), len(all_results)))

    # Post each result
    for result in all_results:
        post_listing(result)

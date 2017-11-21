def post_listing(listing):
    """
    Prints the listing.
    :param listing
    """
    desc = "{0} | {1} | {2} | <{3}>".format(listing["where"], listing["price"], listing["name"], listing["url"])
    
    print(desc)

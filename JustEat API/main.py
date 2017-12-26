from JustEatApiCaller  import JustEatApiCaller

postocde = "SE17"

def start():

    caller = JustEatApiCaller()
    caller.get_restaurants(postocde)


start()
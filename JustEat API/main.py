from JustEatApiCaller  import JustEatApiCaller

postocde = "SE17"

def start():

    caller = JustEatApiCaller()
    restaurants = caller.get_restaurants(postocde)

    print("Found {0} restaurants".format(len(restaurants))) # print the number of found restaurants

    # print the headers
    print("Name             | Rating | Menu ID")
    for restaurant in restaurants:
        print("{0} | {1} | {2}".format(restaurant.name, restaurant.rating, restaurant.menu_id))

        

start()
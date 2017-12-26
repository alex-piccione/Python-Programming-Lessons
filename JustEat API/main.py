from JustEatApiCaller  import JustEatApiCaller

postocde = "SE17"

def start():

    caller = JustEatApiCaller()
    restaurants = caller.get_restaurants(postocde)

    # \n add a "new line" character (it creates an empty line)
    print("Found {0} restaurants:\n".format(len(restaurants))) # print the number of found restaurants

    # print the headers
    print("Name                                               | Rating | Menu ID")
    print("-" * 70) # print "-" 70 times
    for restaurant in restaurants:
        # str.ljust(size) justify the text on the left and fill the extra space (to reach the "size") with the "dot" character 
        print("{0} | {1}    | {2}".format(restaurant.name.ljust(50, "."), restaurant.rating, restaurant.menu.id))

        

start()
from JustEatApiCaller  import JustEatApiCaller

postocde = "SE17"

def start():
    caller = JustEatApiCaller()
    restaurants = caller.get_restaurants(postocde)

    # \n add a "new line" character (it creates an empty line)
    print("Found {0} restaurants:\n".format(len(restaurants))) # print the number of found restaurants

    # print the headers
    print("Name                                               | Rating                         | Menu ID")
    print("-" * 100) # print "-" 70 times
    for restaurant in restaurants:
        # str.ljust(size) justify the text on the left and fill the extra space (to reach the "size") with the "dot" character 
        # rating is a value in the range 0-6 with 0.5 step, so we double it to ahve integer values and cast to int to print from 0 to 12 stars
        # the extra logic to have a precise lenght is because seems like ljust does not work properly witth Uniocode symbols/characters
        # then we nedd to "fill" the 10 spaces with another Unicode character that take the same space
        stars = int(restaurant.rating * 2)
        print("{0} | {1} | {2}".format(
            restaurant.name.ljust(50, "."),
            #( "*" * int(restaurant.rating*2) ).ljust(12),    # Python 2
            "{0}{1}".format( "\u2B50" * stars, "\u2B55" * (12-stars)), # that is nice but 
            restaurant.menu.id))
        

start()
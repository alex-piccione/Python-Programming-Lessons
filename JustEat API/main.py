from JustEatApiCaller import JustEatApiCaller

postcode = "SE17"


def start():
    caller = JustEatApiCaller()
    restaurants = caller.get_restaurants(postcode)

    # \n add a "new line" character (it creates an empty line)
    print("Found {0} restaurants:\n".format(len(restaurants)))  # print the number of found restaurants

    # print the headers
    print("  # | Name                                               | Rating                         | Menus")
    print("-" * 120)  # print "-" 70 times
    count = 1
    for restaurant in restaurants:
        # str.ljust(size) justify the text on the left and fill the extra space (to reach the "size") with the "dot" character 
        # rating is a value in the range 0-6 with 0.5 step, so we double it to ahve integer values and cast to int to print from 0 to 12 stars
        # the extra logic to have a precise lenght is because seems like ljust does not work properly witth Uniocode symbols/characters
        # then we need to "fill" the 10 spaces with another Unicode character that take the same space
        stars = int(restaurant.rating * 2)

        menus = _format_menus(restaurant.menus)

        print("{0} | {1} | {2} | {3}".format(
            str(count).rjust(3, "0"),
            restaurant.name.ljust(50, "."),
            # ( "*" * int(restaurant.rating*2) ).ljust(12),    # Python 2
            "{0}{1}".format("\u2B50" * stars, "\u2B55" * (12-stars)),
            menus
            ))
            
        count += 1


def _format_menus(menus):
    if len(menus) == 0:
        return "(no menus)"

    menu_text = []
    for menu in menus:
        menu_text.append("{0} ({1})".format(menu.title, menu.type))
    return ", ".join(menu_text)
    

start()

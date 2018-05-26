import requests # we import this 3rd party package to manage HTTP requests/response

# from "filename" import "class" and "class"
from Restaurant import Restaurant
from Menu import Menu   

api_key = "Basic VGVjaFRlc3RBUEk6dXNlcjI="  # obtained from public recruitment test repository
api_key = "Basic a2luZ3MtaGFjazpqNHlrN3ljb3Q1MHRmMng="

# store the template out of the class, note the placeholder for the postcode
url_GET_restaurants = "https://public.je-apis.com/restaurants?q={0}"
url_GET_restaurant_menus = "https://public.je-apis.com/restaurants/{0}/menus"

menu_requests_limit = 10  # we don't need to make so many requests, just limit to the first 10 restaurants


class JustEatApiCaller:

    def get_restaurants(self, postcode):

        # print("run get_restaurants for postcode {0}".format(postcode))
   
        url = url_GET_restaurants.format(postcode)  # format the string template "injecting" the postcode
        headers = self._create_headers()
        # make a request with GET verb (passing the headers) and store the response
        response = requests.get(url, headers=headers)

        restaurants = []
        
        menu_requests_count = 0

        if response.status_code == 200:  # check if OK
            response_object = response.json()  # convert the JSON content to a Python object
            # the object is actually a dict so we can use the key to obtain is child, ex. item["subitem"]
            # because Restaurants is an JavaScript array it is converted in something "iterable" (probably a list)
            # so we can use a "for-in" loop 
            for restaurant in response_object["Restaurants"]:
                # we can look to the obtained JSON to find the "keys" of the data we want to read
                id = restaurant["Id"]
                name = restaurant["Name"]  # get the restaurant name using the "Name" key
                rating = restaurant["RatingStars"]
                #menu_id = restaurant["DeliveryMenuId"]
                
                # we get the menus only for the first 10 restaurants
                if menu_requests_count <= menu_requests_limit: 
                    menus = self._get_menus(id)  # get the menus for this restaurant
                    menu_requests_count += 1   # increment of 1
                else:  # skip it
                    menus = []  # empty list

                # create an instance of Restaurant
                restaurant = Restaurant(id, name, rating, menus)  # pass it a list of Menu objects instead of the menu_id

                # ass it to the list
                restaurants.append(restaurant)


        else:  # we have an error...
            print("... something got wrong. Response status code: {0}. Reason: {1}".format(response.status_code, response.reason))
               
        return restaurants # returns the list

    
    def _get_menus(self, restaurant_id):

        url = url_GET_restaurant_menus.format(restaurant_id)  # format the string template "injecting" the restaurant ID
        headers = self._create_headers()
        # make a request with GET verb (passing the headers) and store the response
        response = requests.get(url, headers=headers)

        menus = []

        if response.status_code == 200:  # check if OK
            data = response.json()  # convert the JSON content to a Python object

            # print(data.content) # to get the json string returned by the server

            for menu in data["Menus"]:
                id = menu["Id"]
                title = menu["Title"]
                description = menu["Description"]
                type_ = menu["Type"]["Name"]
                menu = Menu(id, title, description, type_)  # create an instance of Menu
                menus.append(menu)

        else:
            print("_get_menu... something got wrong. Restaurant Id: {0}. Response status code: {1}. Reason: {2}"
                .format(restaurant_id, response.status_code, response.reason))

        return menus


    def _create_headers(self):

        # create the collection of HTTP headers that the server require
        # it is a collection of key/value objects
        headers = {
            "Accept-Tenant": "uk",
            "Accept-Language": "en-GB",
            "Authorization": api_key,
            "Host": "public.je-apis.com"
        }

        return headers

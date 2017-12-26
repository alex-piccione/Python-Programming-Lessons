import requests # we import this 3rd party package to manage HTTP requests/response

# from "filemame" import "class"
from Restaurant import Restaurant   

api_key = "Basic VGVjaFRlc3RBUEk6dXNlcjI="  # obtained from public recruitment test repository

# store the template out of the class, note the placeholder for the postcode
url_api_for_GET_restaurants = "https://public.je-apis.com/restaurants?q={0}"


class JustEatApiCaller:

    def get_restaurants(self, postcode):

        print("run get_restaurants for postcode {0}".format(postcode))
   
        url = url_api_for_GET_restaurants.format(postcode) # format the strin template "injecting" the postcode

        # create the collection of HTTP headers that the server require
        # it is a collection of key/value objects
        headers = {
            "Accept-Tenant": "uk",
            "Accept-Language": "en-GB",
            "Authorization": api_key,
            "Host": "public.je-apis.com"
        }

        response = requests.get(url, headers=headers) # make a request with GET verb (passing the headers) and store the response 

        restaurants = []

        if (response.status_code == 200): # check if OK
            response_object = response.json()  # convert the JSON content to a Python object
            # the object is actually a dict so we can use the key to obtain is child, ex. item["subitem"]
            # because Restaurants is an JavaScript array it is converted in something "iterable" (probably a list)
            # so we can use a "for-in" loop 
            for restaurant in response_object["Restaurants"]:
                # we can look to the obtained JSON to find the "keys" of the data we want to read
                name = restaurant["Name"]  # get the restaurant name using the "Name" key
                rating = restaurant["RatingStars"]
                rating = restaurant["RatingStars"]
                menu_id = restaurant["DeliveryMenuId"]
                
                # create an instance of Restaurant
                restaurant = Restaurant(name, rating, menu_id)

                # ass it to the list
                restaurants.append(restaurant)


        else: # we have an error...
            print("... something got wrong. Response status code: {0}. Reason: {1}".format(response.status_code, response.reason))
               
        return restaurants # returns the list

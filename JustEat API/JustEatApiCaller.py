
api_url = "https://public.je-apis.com/restaurants?q=se17"


import requests

class JustEatApiCaller:

    def get_restaurants(self, postcode): # page 307

        print(f"get_restaurants({postcode})") # string f

        url = "http://www.google.com?q={0}".format(postcode)
        response = requests.get(url)

   

    def _get_distance(point_a, point_b):
        '''Returns the distance from a to b'''


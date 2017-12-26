'''Accept-Tenant: uk
Accept-Language: en-GB
Authorization: Basic VGVjaFRlc3RBUEk6dXNlcjI=
Host: public.je-apis.com'''

'''https://public.je-apis.com/restaurants?q=se19'''

import requests

class JustEastApiCaller:

    def get_restaurants(self, postcode):  #page 307

        print("{0}".format(postcode))  #string formatting

   

        url = "https://public.je-apis.com/restaurants?q={0}".format(postcode)

        headers = {
"Accept-Tenant":"uk",
"Accept-Language":"en-GB",
"Authorization":"Basic VGVjaFRlc3RBUEk6dXNlcjI=",
"Host":"public.je-apis.com"

        }
        response = requests.get(url, headers=headers)    #requests is a library

        print (response)
        print (response.status_code)
        #print (response.text) 
        for restaurant in response.content.Restaurants:
            print(restaurant.Name)
        
        print ("end") 

    def _get_distance(point_a, point_b):
        '''Returns the distance from a to b'''
        pass
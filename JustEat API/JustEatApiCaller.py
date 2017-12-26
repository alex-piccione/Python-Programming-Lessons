import requests

api_key = "Basic VGVjaFRlc3RBUEk6dXNlcjI="  # obtained from public recruitment test repository

url_api_for_GET_restaurants = "https://public.je-apis.com/restaurants?q={0}"

class JustEatApiCaller:

    def get_restaurants(self, postcode):

        print("run get_restaurants for postcode {0}".format(postcode))
   
        url = url_api_for_GET_restaurants.format(postcode)

        headers = {
            "Accept-Tenant":"uk",
            "Accept-Language":"en-GB",
            "Authorization": api_key,
            "Host":"public.je-apis.com"
        }

        response = requests.get(url, headers=headers)

        if (response.status_code == 200):
            response_object = response.json()
            for restaurant in response_object["Restaurants"]:
                print(restaurant["Name"])                

        else:
            print("... something got wrong. Response status code: {0}. Reason: {1}".format(response.status_code, response.reason))
       
        print ("\n\nend") 

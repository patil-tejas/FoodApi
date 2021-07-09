#API CODE---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#This api limits the no of requests a server can make i.e 5000 per/her
# there is a max limit of request for every 30 mins and then the counter resets 
# 
# a try except block should be used in below get_iamge_list() to avoid an unexpected response 
# It is recommended to cache requests for 24 hours

#Returned image URLs may be used for temporarily displaying search results, thats what this project does.
#permanent hotlinking is not allowed
#If you intend to use the images, please download them to your server first.

#-------python modules
import requests
import random
from urllib.parse import quote

#API Parameters 
q = "food"                                      #query parameter
per_page = "20"                                 #images per page
page = str(random.randint(1,25))                #chooses random page out of 25 pages                                    #
                                                #max totalhits = 500 and 20 images per page ,so total no of pages 25

image_type = "photo"                            #type of image ("vector , photo etc")

API_KEY = "XXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXX"  #Please use your own api key


#API URL ENDPOINT  urllib.parse.quote() to encode the query parameter
URL = "https://pixabay.com/api/?key="+API_KEY+"&q="+quote(q)+"&page="+page+"&per_page="+per_page+"&image_type="+image_type



def get_image_list():
    #Manage API response
    response = requests.get(url=URL)

    api_data = response.json()

    api_hits = api_data["hits"]

    #key to fetch from pixabay api
    largeImageURL = "largeImageURL"

    #url data from the api response with 
    api_image_list = [temp[largeImageURL] for temp in api_hits]

    #this should be displayed on website
    image_list = random.sample(api_image_list, k = 10)
    return image_list
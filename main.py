import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv('.env')

token: str = os.getenv('TOKEN')
my_username: str = os.getenv('MY_USERNAME')
graph_id = os.getenv('GRAPH_ID')

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': token,
    'username': my_username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{my_username}/graphs'

graph_config = {
    'id': graph_id,
    "name": "Coding Graph",
    "unit": "Min",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": token,
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

today = datetime.now()
formatted_today_date = today.strftime("%Y%m%d")

pixel_creation_endpoint = f'{pixela_endpoint}/{my_username}/graphs/{graph_id}'
pixel_data = {
    "date": formatted_today_date,
    "quantity": "60",
}

# pixel_response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(pixel_response.text)


pixela_update_endpoint = f"{pixela_endpoint}/{my_username}/graphs/{graph_id}/{formatted_today_date}"

pixela_update_config = {
    "quantity": "0",
}

# pixela_update_response = requests.put(url=pixela_update_endpoint, json=pixela_update_config, headers=headers)
# print(pixela_update_response.text)

pixela_delete_endpoint = f"{pixela_endpoint}/{my_username}/graphs/{graph_id}/{formatted_today_date}"

# pixel_delete_response = requests.delete(url=pixela_delete_endpoint, headers=headers)
# print(pixel_delete_response.text)

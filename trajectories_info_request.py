import traj_pb2 as Traj
import requests
from credentials import Credentials

headers = {
    'accept': 'application/json',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

# response = requests.post('https://openpositioning.org/api/live/users/trajectories/', headers=headers)
response = requests.get(f'https://openpositioning.org/api/live/users/trajectories/{Credentials.user_key}?key={Credentials.master_key}', headers=headers)

print(response.content)

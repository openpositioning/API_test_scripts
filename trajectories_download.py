from io import BytesIO
import traj_pb2 as Traj
import requests
from credentials import Credentials

import zipfile

headers = {
    'accept': 'application/json',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

n_skip = 0
limit = 30
# response = requests.post('https://openpositioning.org/api/live/trajectory/download/', headers=headers)
response = requests.get(f'https://openpositioning.org/api/live/trajectory/download/{Credentials.user_key}?skip={n_skip}&limit={limit}&key={Credentials.master_key}', headers=headers)

trajectories = []

with zipfile.ZipFile(BytesIO(response.content)) as zip_archive:
    for item in zip_archive.filelist:
        print(item.filename)
        if item.filename.endswith(".pkt"):
            trajectory = Traj.Trajectory()
            try:
                trajectory.ParseFromString(zip_archive.read(item.filename))
                trajectories.append(trajectory)
                print(str(trajectory)[:100])
            except Exception as ex:
                print(ex)


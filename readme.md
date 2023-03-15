# Test the restful API and proto file
Using python 3.7+ define a python virtual environment
```
python -m venv venv
source venv/bin/activate    # unix
./venv/Scripts/Activate.ps1 # powershell
pip install -r requirements.txt
```

Install [Proto Buffers](https://protobuf.dev/downloads/) and add it to the path

Compile the proto file to create the libraries
```
protoc -I=./ --python_out=./ ./traj.proto
```

Get the user key from the web API at https://openpositioning.org/docs

Change the user and master key in the `credentials.py` file

Send a trajectory to the API:
```
python trajectory_submit.py
```

Request the submited trajectories info from the API:
```
python trajectories_info_request.py
```

Download previously submited trajectories from the API:
```
python trajectories_download.py
```
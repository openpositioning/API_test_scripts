# Test the restful API and proto file
Using python 3.7+ (tested in 3.10.8) define a python virtual environment
```
python -m venv venv
source venv/bin/activate    # unix
./venv/Scripts/Activate.ps1 # powershell
pip install --upgrade pip
pip install -r requirements.txt
```

Install [Proto Buffers](https://protobuf.dev/downloads/) (tested with [version 22.0](https://github.com/protocolbuffers/protobuf/releases/tag/v22.0)) and add it to the path

Compile the proto file to create the libraries
```
protoc -I="." --python_out="." ./traj.proto
```

Get the user key from the web API at https://openpositioning.org/docs

Change the user and master key in the [`credentials.py`](./credentials.py) file

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

Submit a positioning requests:
```
jupyter lab     # Start a notebook
```
and open [`openpositioning_fp_positioning.ipynb`](./openpositioning_fp_positioning.ipynb):
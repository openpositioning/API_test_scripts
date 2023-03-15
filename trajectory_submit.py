import os
import pandas as pd
from credentials import Credentials
import traj_pb2 as Traj
import requests
import json
import time


raw_path = './data/test_trajectory/'

def load_wifi(filepath):
    wifi = {}
    names = {}
    with open(filepath) as f:
        for idx, line in enumerate(f):
            if idx > 0:
                info = line.split(",")
                wifitime = info[1]
                fpinfo = info[3:]
                if len(fpinfo) % 5 != 0:
                    continue
                fp = {int(ap.replace(":",""),16):[int(rssi),int(time)] for ap,rssi,time in zip(fpinfo[1::5],fpinfo[2::5],fpinfo[0::5])}
                wifi[int(wifitime)] = fp
                these_names = {int(ap.replace(":",""),16):[name,freq] for ap,name,freq in zip(fpinfo[1::5],fpinfo[3::5],fpinfo[4::5])}
                for ap in these_names:
                    names[ap] = these_names[ap]

    return wifi, names

combined_imu = pd.read_csv(os.path.join(raw_path,'combined_imu_data_7.csv'))

start_time_unix = int(time.time() * 1000) - 1000*60*60*24

# pdr, TODO, implement your own PDR
pdr = pd.DataFrame(combined_imu[['timestamp_global[ms]','timestampImu[ms]']])
pdr = pdr.rename(columns=
    {
    'timestamp_global[ms]':'timestamp',
    'timestampImu[ms]':'timestamp_imu'
    }
)
real_time_offset = - pdr.timestamp_imu.iloc[0] + pdr.timestamp.iloc[0]
pdr = pdr.drop(['timestamp_imu'],axis=1)
pdr['x'] = 0.0
pdr['y'] = 1.0

mf = pd.read_csv(os.path.join(raw_path,'magnetic_field_uncalibrated_6.csv'),skiprows=1)
mf = mf.rename(columns=
    {
    'imuTimestamp':'timestamp',
    }
)
mf.timestamp = mf.timestamp + real_time_offset

pressure = pd.read_csv(os.path.join(raw_path,'pressure_11.csv'),skiprows=1)
pressure = pressure.rename(columns=
    {
    'imuTimestamp':'timestamp',
    }
)
pressure.timestamp = pressure.timestamp + real_time_offset

light = pd.read_csv(os.path.join(raw_path,'light_10.csv'),skiprows=1)
light = light.rename(columns=
    {
    'imuTimestamp':'timestamp',
    }
)
light.timestamp = light.timestamp + real_time_offset

location = pd.read_csv(os.path.join(raw_path,'location_9.csv'),skiprows=1)
location.time = location.time + real_time_offset

wifi, names = load_wifi(os.path.join(raw_path,'wifi_8.csv'))

traj = Traj.Trajectory()
traj.start_timestamp = int(start_time_unix)

for _, row in pdr.iterrows():
    pdr_data = Traj.Pdr_Sample()
    pdr_data.x = row.x
    pdr_data.y = row.y
    pdr_data.relative_timestamp = int(row.timestamp)
    traj.pdr_data.extend([pdr_data])

for _, row in combined_imu.iterrows():
    imu_data = Traj.Motion_Sample()
    imu_data.relative_timestamp = int(row['timestamp_global[ms]'])
    imu_data.acc_x = row['acc_uncal_x[m/s^2]']
    imu_data.acc_y = row['acc_uncal_y[m/s^2]']
    imu_data.acc_z = row['acc_uncal_z[m/s^2]']

    imu_data.gyr_x = row['ang_vel_uncal_x[rad/s]']
    imu_data.gyr_y = row['ang_vel_uncal_y[rad/s]']
    imu_data.gyr_z = row['ang_vel_uncal_z[rad/s]']
    
    # Note rotation vectors are not avilable in this test set
    imu_data.rotation_vector_x = 0
    imu_data.rotation_vector_y = 0
    imu_data.rotation_vector_z = 0
    imu_data.rotation_vector_w = 1

    imu_data.step_count = 400
    traj.imu_data.extend([imu_data])

for _, row in mf.iterrows():
    position_sample = Traj.Position_Sample()
    position_sample.relative_timestamp = int(row.timestamp)
    position_sample.mag_x = float(row['mfield_uncal_x[uT]'])
    position_sample.mag_y = float(row['mfield_uncal_y[uT]'])
    position_sample.mag_z = float(row['mfield_uncal_z[uT]'])
    traj.position_data.extend([position_sample])

for _,row in pressure.iterrows():
    #continue
    pressure_data = Traj.Pressure_Sample()
    pressure_data.relative_timestamp = int(row.timestamp)
    pressure_data.pressure = row['pressure[millibar]']
    traj.pressure_data.extend([pressure_data])

for _,row in light.iterrows():
    light_data = Traj.Light_Sample()
    light_data.relative_timestamp = int(row.timestamp)
    light_data.light = row["ambient_brightness[lux]"]
    traj.light_data.extend([light_data])

for _,row in location.iterrows():
    gnss_data = Traj.GNSS_Sample()
    gnss_data.relative_timestamp = int(row.time)
    gnss_data.latitude = float(row['lat (deg)'])
    gnss_data.longitude = float(row['long (deg)'])
    gnss_data.altitude = float(row['altitude (m above sea level)'])
    gnss_data.accuracy = float(row['accuracy (m)'])
    gnss_data.speed = float(row['speed (m/s over ground)'])
    gnss_data.provider = row['provider']
    traj.gnss_data.extend([gnss_data])

for time in wifi:
    wifi_data = Traj.WiFi_Sample()
    wifi_data.relative_timestamp = time + real_time_offset
    fp = wifi[time]
    for ap in fp:
        scan_rssi = fp[ap][0]
        scan_time = fp[ap][1]
        mac_scan = Traj.Mac_Scan()
        mac_scan.relative_timestamp = scan_time + real_time_offset
        mac_scan.mac = int(ap)
        mac_scan.rssi = scan_rssi
        wifi_data.mac_scans.extend([mac_scan])
    traj.wifi_data.extend([wifi_data])

for ap in names:
    aps_data = Traj.AP_Data()
    aps_data.mac = int(ap)
    aps_data.ssid = names[ap][0]
    aps_data.frequency = int(names[ap][1])
    traj.aps_data.extend([aps_data])

bin = traj.SerializeToString()

os.makedirs("traj_data", exist_ok=True)
outpath = 'traj_data/proto_packet.pkt'
with open(outpath, "wb") as f:
    f.write(bin)

with open(outpath[:-4] + ".json", "w") as f:
    traj_string= json.dumps(str(traj))
    f.write(traj_string)


headers = {
    'accept': 'application/json',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}
files = {
    'file': open('traj_data/proto_packet.pkt', 'rb'),
}

# response = requests.post('https://openpositioning.org/api/dummy/trajectory/upload/', headers=headers, files=files)
response = requests.post(f'https://openpositioning.org/api/live/trajectory/upload/{Credentials.user_key}/?key={Credentials.master_key}', headers=headers, files=files )


print(response.content)


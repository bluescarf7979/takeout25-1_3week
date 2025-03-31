# takeout25-1_3week
```bash
# 1. 환경설정
sudo apt update
sudo apt install git
pip install open3d scikit-learn
sudo apt install ros-humble-sensor-msgs-py
```

```bash
# 2. 저장소 git clone
cs
git clone https://github.com/bluescarf7979/takeout3week.git
cb
source install/setup.bash

ros2 pkg list | grep takeout3week
```
---
```md
📦 takeout3week
 ┣ 📂 launch
 ┃ ┣ 📜 lidar_bag_rviz.launch.py
 ┃ ┣ 📜 cluster.launch.py
 ┃ ┣ 📜 voxel.launch.py
 ┃ ┣ 📜 roi.launch.py
 ┃ ┣ 📜 pointcloud_processing.launch.py
 ┣ 📂 takeout3week
 ┃ ┣ 📜 pointcloud_cluster.py
 ┃ ┣ 📜 pointcloud_roi.py
 ┃ ┗ 📜 pointcloud_voxel.py
 ┣ 📂 takeout3week
 ┃ ┣ 📜 cluster.yaml
 ┃ ┣ 📜 roi.yaml
 ┃ ┣ 📜 voxel.yaml
 ┃ ┣ 📜 pointcloud_params.yaml
 ┣ 📜 README.md
 ┗ 📜 requirements.txt
```

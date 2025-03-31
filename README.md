# takeout25-1_3week
```bash
# 1. 환경설정
sudo apt update
sudo apt install python3-pip
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
 ┣ 📂 config
 ┃ ┣ 📜 cluster.yaml
 ┃ ┣ 📜 roi.yaml
 ┃ ┣ 📜 voxel.yaml
 ┃ ┣ 📜 pointcloud_params.yaml
 ┣ 📜 README.md
 ┗ 📜 requirements.txt
```

```bash
# 3. 코드 실행

# rosbag 및 rviz 실행
ros2 launch takeout3week lidar_bag_rviz.launch.py

# rosbag 및 cluster 실행
ros2 launch takeout3week cluster.launch.py

# rosbag 및 voxel 실행
ros2 launch takeout3week voxel.launch.py

# rosbag 및 roi 실행
ros2 launch takeout3week roi.launch.py

# 전체 실행
ros2 launch takeout3week pointcloud_processing.launch.py
```

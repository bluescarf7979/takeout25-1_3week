# takeout25-1_3week
https://drive.google.com/file/d/14Vk9Hf1qeFQexdE45aPBasvfFrqzxzb2/view?usp=drive_link

```bash
# 0. 단축어 설정
echo "alias cs='cd ~/ws/src'" >> ~/.bashrc
echo "alias cw='cd ~/ws'" >> ~/.bashrc
echo "alias cb='cd ~/ws && colcon build && source install/setup.bash'" >> ~/.bashrc
source ~/.bashrc
```

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
# numpy and pandas setting
pip install numpy==1.21.5
pip install pandas==1.3.3
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
---
---
## YD LiDAR 실습
```bash
# 종속성 설치
sudo apt install cmake pkg-config
sudo apt-get install python swig
sudo apt-get install python-pip
```
```bash
# YDLiDAR SDK 설치
cd
git clone https://github.com/YDLIDAR/YDLidar-SDK.git
mkdir YDLidar-SDK/build
cd YDLidar-SDK/build
cmake ..
make
sudo make install
```
```bash
# YDLiDAR ROS2 패키지 설치
cs
git clone https://github.com/YDLIDAR/ydlidar_ros2_driver.git
cb
```
```bash
# YDLiDAR 실행
ros2 launch takeout3week yd_lidar.launch.py
```

# ROS_Basic

[Virtuoso_Ultrasonic_Protocal_Table]

https://docs.google.com/spreadsheets/d/1F-PG_jJVft8dY5kM7koMyuJRI3mmQSoqqGzsMUzwCVs/edit?usp=sharing

[~/.bashrc]
+ source ~/catkin_ws/devel/setup.bash
+ export ROS_MASTER_URI=http://192.168.41.100:11311
+ export ROS_IP=$(ip route get 1.2.3.4 | awk '{print $7}')

#!/bin/bash

source /opt/ros/$ROS_DISTRO/setup.bash
source /home/$USER/catkin_ws/devel/setup.bash

export ROS_IP=$(ip route get 1.2.3.4 | awk '{print $7}')
export ROS_MASTER_URI=http://${1}:11311/ 

rostopic pub ${2} ${3} "data: ${4}" -r${5:-10}


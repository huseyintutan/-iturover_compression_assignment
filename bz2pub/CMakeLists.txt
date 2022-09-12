cmake_minimum_required(VERSION 3.0.2)
project(bz2pub)


find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_package(
#  LIBRARIES bz2pub
 CATKIN_DEPENDS  rospy std_msgs 
#  DEPENDS system_lib
)


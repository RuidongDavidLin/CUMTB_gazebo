# CUMTB_gazebo
这是第十六届全国大学生智能车竞赛迅飞智慧餐厅组的线上仿真代码

- 一共有两个分支
|——main分支：安装了cartographer和cartographer_ros
|——master分支：没有做定位要求，采用gazebo给出的坐标信息，为当初线上赛上传的版本

## How to use
* 配置环境 

首先按照Cartographer的官方文档配置环境
```
sudo apt-get update
sudo apt-get install -y python-wstool python-rosdep ninja-build stow
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
sudo apt-get remove ros-${ROS_DISTRO}-abseil-cpp
```
运行以下文件
`sh src/cartographer/scripts/install_abseil.sh`

* 编译功能包

将代码放置于工作空间的src文件夹下面，并在工作空间打开终端，运行下面的指令
`catkin_make_isolated --use-ninja`

* 按照src中的reademe.pdf操作

* 打开/gazebo_pkg/launch/
launch文件的运行方式：在终端中输入以下指令
`roslaunch filename.launch`

* launch 文件的介绍
###### race.launch :启动gazebo的仿真环境
###### ucar_slam.launch :启动Cartographer建图算法
###### ucar_localization.launch : 启动cartographer纯定位
###### navi.launch :启动导航算法
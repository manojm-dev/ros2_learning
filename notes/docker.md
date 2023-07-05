# pull image:
podman pull osrf/ros:humble-desktop

# create container:
podman run -d -it --name rosdev_container -v /home/<user-name>/ros2_ws:/root/ --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" osrf/ros:humble-desktop

# post-creation tasks:

## update and upgrade
apt update & apt upgrade 

## Tools and Software installation:

## basic tools 
apt install nano 
apt install git
apt install wget
apt install curl
apt install tmux
apt install python3-pip

## ros2:
apt install ros-humble-turtlesim 
apt install ~nros-humble-rqt* 
apt install python3-colcon-common-extensions

## urdf & rviz:
apt install ros-humble-xacro & apt install ros-humble-joint-state-publisher 

## Gazebo:
https://gazebosim.org/docs

## Configuration

### colcon autocomplete
echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bash_user
echo "source /root/.bash_user" >> ~/.bashrc

### ros sourceing
echo "source /opt/ros/humble/setup.bash" >> ~/.bash_user

### *** $ source ~/.bashrc ***


# development tools

## vscode 
//install repository dependencies
sudo apt install software-properties-common apt-transport-https wget
//import microsoft pgp key
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
//enable vscode repo
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"

 
*****fixes*******
# Error and fixes

1)Setup tool depreciated

cause: ???

solution:
Install the setuptools 58.2.0 version using the following command
pip install setuptools==58.2.0

2)rviz blackscreen problem

cause: these packages are old in ubuntu but rviz requires newer version so enabling a repository to download newer version
solution:
apt install -y software-properties-common && add-apt-repository ppa:kisak/kisak-mesa && apt install libegl-mesa0 libegl1-mesa-dev libgbm-dev libgbm1 libgl1-mesa-dev libgl1-mesa-dri libglapi-mesa libglx-mesa0 -y


























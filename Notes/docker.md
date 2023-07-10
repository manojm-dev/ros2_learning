# Running ros2 in docker image using podman

## Podman Setup

### 1) Pull image:
podman pull osrf/ros:humble-desktop

### 2) Create container:
podman run -d -it --name humble_con -v /home/(username)/ros2_ws:/root/ --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" osrf/ros:humble-desktop

### 3) Starting container
podman start humble_con

### 4) Enter into container/
podman exec -it humble_con /bin/bash

### 5) Saving container into image
podman commit humble_con humble-desktop:latest

### 6) Pushing image to docker hub
                 (image name:tag)               (dockerhub username)  (dockerhub reponame:tag) <br>
podman push humble_destop/:latest docker:docker.io/manojmdev/humble-desktop:latest

## Post-creation tasks:

### 1) update and upgrade
apt update <br>
apt upgrade 

### 2) Tools and Software installation:

#### i) basic tools 
apt install nano <br>
apt install git <br>
apt install wget <br>
apt install curl <br>
apt install tmux <br>
apt install python3-pip <br>
apt install evince <br>
apt install tmux <br>
apt install tree <br>

#### ii) ros2:
apt install ros-humble-turtlesim <br>
apt install ~nros-humble-rqt* <br>
apt install python3-colcon-common-extensions <br>

#### iii) urdf & rviz:
apt install ros-humble-xacro <br>
apt install ros-humble-joint-state-publisher <br>
apt install ros-humble-joint-state-publihser-gui <br>

#### iv) Gazebo:
* classic gazebo: <br> apt install ros-humble-ros-gz <br> apt install ros-humble-gazebo-ros
* igition gazeob: <br> https://gazebosim.org/docs

### 3) Configuration

#### 1) ros sourceing
echo "source /opt/ros/humble/setup.bash" >> ~/.bash_user

#### 2) colcon autocomplete
echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bash_user <br>
echo "source /root/.bash_user" >> ~/.bashrc <br>

#### 3) workspace sourceing
echo "alias sws="source /install/setup.bash"" >> ~/.bash_user

Don't forge to source before working$ source ~/.bashrc

### 4)development tools

### 1)VSCode 

#### i) install
//install repository dependencies <br>
sudo apt install software-properties-common apt-transport-https wget<br>

//import microsoft pgp key <br>
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add - <br>

//enable vscode repo <br>
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" <br>

//install vscode <br>
apt install vscode -y

#### ii) configure
echo "alias vsc="code --no-sandbox --user-data-dir=/root/.config/vscode/VSCodeData/"" >> ~/.bash_user

### 5) Error and fixes

* 1)Setup tool depreciated <br> cause: ?? <br> solution: <br> Install the setuptools 58.2.0 version using the following command <br> pip install setuptools==58.2.0 <br>

* 2)rviz blackscreen problem <br> cause: these packages are old in ubuntu but rviz requires newer version so enabling a repository to download newer version <br> solution: <br> apt install -y software-properties-common && add-apt-repository ppa:kisak/kisak-mesa && apt install libegl-mesa0 libegl1-mesa-dev libgbm-dev libgbm1 libgl1-mesa-dev libgl1-mesa-dri libglapi-mesa libglx-mesa0 -y


























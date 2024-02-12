# Connecting Machines

1) Local Nework
* export ROS_DOMAIN_ID=<your_domain_id>
  * By default, the Linux kernel uses ports 32768-60999 for ephemeral ports. This means that domain IDs 0-101 and 215-232 can be safely used without colliding with ephemeral ports
* ufw block unauthorised connections so topic transfer through network only when the ufw is disabled.
* To fix this we have to allow the host ip network or the specific ip of the device you want to connect.
  * command: sudo ufw allow from host ip (or) sudo ufw allow from host ip/25[eg.102.168.1.(1 to 244)]
2) Setting up DDS
* sources: https://answers.ros.org/question/413513/is-it-possible-to-run-ros2-via-wireguard/

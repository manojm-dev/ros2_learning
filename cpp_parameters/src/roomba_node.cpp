#include <chrono>
#include <functional>
#include <string>

#include <rclcpp/rclcpp.hpp>

using namespace std::chrono_literals;

class RoombaRobot : public rclcpp::Node
{
public:
  RoombaRobot()
  : Node("roomba_node")
  {
    this->declare_parameter("roomba_mode", "idle");

    timer_ = this->create_wall_timer(
      1000ms, std::bind(&RoombaRobot::timer_callback, this));
  }

  void timer_callback()
  {
    std::string my_param = this->get_parameter("my_parameter").as_string();

    RCLCPP_INFO(this->get_logger(), "Roomba is %s!", my_param.c_str());
  }

private:
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<RoombaRobot>());
  rclcpp::shutdown();
  return 0;
}
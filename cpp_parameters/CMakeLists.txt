cmake_minimum_required(VERSION 3.8)
project(cpp_parameters)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(minimal_param_node src/parameters_node.cpp)
ament_target_dependencies(minimal_param_node rclcpp)

add_executable(roomba_node src/roomba_node.cpp)
ament_target_dependencies(roomba_node rclcpp)

install(TARGETS
  minimal_param_node
  roomba_node
  DESTINATION lib/${PROJECT_NAME}
)

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

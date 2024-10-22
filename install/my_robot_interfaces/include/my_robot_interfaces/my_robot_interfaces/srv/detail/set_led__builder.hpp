// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interfaces:srv/SetLed.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__SET_LED__BUILDER_HPP_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__SET_LED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_interfaces/srv/detail/set_led__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_SetLed_Request_turn_on_off
{
public:
  Init_SetLed_Request_turn_on_off()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_robot_interfaces::srv::SetLed_Request turn_on_off(::my_robot_interfaces::srv::SetLed_Request::_turn_on_off_type arg)
  {
    msg_.turn_on_off = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::SetLed_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::SetLed_Request>()
{
  return my_robot_interfaces::srv::builder::Init_SetLed_Request_turn_on_off();
}

}  // namespace my_robot_interfaces


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_SetLed_Response_status
{
public:
  Init_SetLed_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_robot_interfaces::srv::SetLed_Response status(::my_robot_interfaces::srv::SetLed_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::SetLed_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::SetLed_Response>()
{
  return my_robot_interfaces::srv::builder::Init_SetLed_Response_status();
}

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__SET_LED__BUILDER_HPP_

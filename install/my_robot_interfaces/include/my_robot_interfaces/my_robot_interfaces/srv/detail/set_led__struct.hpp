// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_robot_interfaces:srv/SetLed.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__SET_LED__STRUCT_HPP_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__SET_LED__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_robot_interfaces__srv__SetLed_Request __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_interfaces__srv__SetLed_Request __declspec(deprecated)
#endif

namespace my_robot_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetLed_Request_
{
  using Type = SetLed_Request_<ContainerAllocator>;

  explicit SetLed_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->turn_on_off = false;
    }
  }

  explicit SetLed_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->turn_on_off = false;
    }
  }

  // field types and members
  using _turn_on_off_type =
    bool;
  _turn_on_off_type turn_on_off;

  // setters for named parameter idiom
  Type & set__turn_on_off(
    const bool & _arg)
  {
    this->turn_on_off = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_robot_interfaces::srv::SetLed_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_interfaces::srv::SetLed_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::SetLed_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::SetLed_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::SetLed_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::SetLed_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::SetLed_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::SetLed_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::SetLed_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::SetLed_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_interfaces__srv__SetLed_Request
    std::shared_ptr<my_robot_interfaces::srv::SetLed_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_interfaces__srv__SetLed_Request
    std::shared_ptr<my_robot_interfaces::srv::SetLed_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetLed_Request_ & other) const
  {
    if (this->turn_on_off != other.turn_on_off) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetLed_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetLed_Request_

// alias to use template instance with default allocator
using SetLed_Request =
  my_robot_interfaces::srv::SetLed_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_robot_interfaces


#ifndef _WIN32
# define DEPRECATED__my_robot_interfaces__srv__SetLed_Response __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_interfaces__srv__SetLed_Response __declspec(deprecated)
#endif

namespace my_robot_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetLed_Response_
{
  using Type = SetLed_Response_<ContainerAllocator>;

  explicit SetLed_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = false;
    }
  }

  explicit SetLed_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = false;
    }
  }

  // field types and members
  using _status_type =
    bool;
  _status_type status;

  // setters for named parameter idiom
  Type & set__status(
    const bool & _arg)
  {
    this->status = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_robot_interfaces::srv::SetLed_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_interfaces::srv::SetLed_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::SetLed_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::SetLed_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::SetLed_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::SetLed_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::SetLed_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::SetLed_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::SetLed_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::SetLed_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_interfaces__srv__SetLed_Response
    std::shared_ptr<my_robot_interfaces::srv::SetLed_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_interfaces__srv__SetLed_Response
    std::shared_ptr<my_robot_interfaces::srv::SetLed_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetLed_Response_ & other) const
  {
    if (this->status != other.status) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetLed_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetLed_Response_

// alias to use template instance with default allocator
using SetLed_Response =
  my_robot_interfaces::srv::SetLed_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_robot_interfaces

namespace my_robot_interfaces
{

namespace srv
{

struct SetLed
{
  using Request = my_robot_interfaces::srv::SetLed_Request;
  using Response = my_robot_interfaces::srv::SetLed_Response;
};

}  // namespace srv

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__SET_LED__STRUCT_HPP_
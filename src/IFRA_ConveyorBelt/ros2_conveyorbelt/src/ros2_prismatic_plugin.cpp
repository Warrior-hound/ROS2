#include <gazebo/physics/Model.hh>
#include <gazebo/physics/World.hh>
#include <gazebo/physics/Joint.hh>
#include <gazebo_ros/node.hpp>
#include <rclcpp/rclcpp.hpp>

#include "ros2_prismatic/ros2_prismatic_plugin.hpp"     // Header file.

#include <conveyorbelt_msgs/msg/conveyor_belt_state.hpp>      // ROS2 Message.
#include <conveyorbelt_msgs/srv/conveyor_belt_control.hpp> 
#include <memory>

namespace gazebo_ros
{

class ROS2PrismaticPluginPrivate
{
public:

  // ROS node for communication, managed by gazebo_ros.
  gazebo_ros::Node::SharedPtr ros_node_;

  // The joint that controls the movement of the prismatic joint:
  gazebo::physics::JointPtr prismatic_joint_;

  // Additional parameters:
  double joint_position_;
  double max_position_;
  double speed_;
  double limit_;
  bool moving_forward_;
  
  // PUBLISH Prismatic joint status:
  void PublishStatus();                                                                     // Method to publish status.
  rclcpp::Publisher<conveyorbelt_msgs::msg::ConveyorBeltState>::SharedPtr status_pub_;      // Publisher.
  conveyorbelt_msgs::msg::ConveyorBeltState status_msg_;                                    // Prismatic joint status.

  // ROS2 Service
    // SET Joint Velocity:
  void SetJointVelocity(
    conveyorbelt_msgs::srv::ConveyorBeltControl::Request::SharedPtr,    
    conveyorbelt_msgs::srv::ConveyorBeltControl::Response::SharedPtr);                      // Method to execute service.
  rclcpp::Service<conveyorbelt_msgs::srv::ConveyorBeltControl>::SharedPtr enable_service_;  // ROS2 Service.

  // WORLD UPDATE event:
  void OnUpdate();
  rclcpp::Time last_publish_time_;
  int update_ns_;
  gazebo::event::ConnectionPtr update_connection_;  // Connection to world update event. Callback is called while this is alive.

};

ROS2PrismaticPlugin::ROS2PrismaticPlugin()
: impl_(std::make_unique<ROS2PrismaticPluginPrivate>())
{
}

ROS2PrismaticPlugin::~ROS2PrismaticPlugin()
{
}

void ROS2PrismaticPlugin::Load(gazebo::physics::ModelPtr _model, sdf::ElementPtr _sdf)
{
  
  // Create ROS2 node:
  impl_->ros_node_ = gazebo_ros::Node::Get(_sdf);

  // OBTAIN -> PRISMATIC JOINT:
  impl_->prismatic_joint_ = _model->GetJoint("prismatic_joint");

  if (!impl_->prismatic_joint_) {
    RCLCPP_ERROR(impl_->ros_node_->get_logger(), "Prismatic joint not found, unable to start prismatic plugin.");
    return;
  }

  // Set max position (m)
  impl_->max_position_ = _sdf->GetElement("max_position")->Get<double>();

  // Set speed (m/s)
  impl_->speed_ = _sdf->GetElement("speed")->Get<double>();

  // Set limit (m)
  impl_->limit_ = impl_->prismatic_joint_->UpperLimit();

  // Initialize direction
  impl_->moving_forward_ = true;

  // Create status publisher
  impl_->status_pub_ = impl_->ros_node_->create_publisher<conveyorbelt_msgs::msg::ConveyorBeltState>("PRISMATICSTATE", 10);
  impl_->status_msg_.enabled = true;
  impl_->status_msg_.power = impl_->speed_;

  impl_->enable_service_ =
    impl_->ros_node_->create_service<conveyorbelt_msgs::srv::ConveyorBeltControl>(
    "perform_stroke", std::bind(
      &ROS2PrismaticPluginPrivate::SetJointVelocity, impl_.get(),
      std::placeholders::_1, std::placeholders::_2));

  double publish_rate = _sdf->GetElement("publish_rate")->Get<double>();
  impl_->update_ns_ = int((1/publish_rate) * 1e9);

  impl_->last_publish_time_ = impl_->ros_node_->get_clock()->now();

  // Create a connection so the OnUpdate function is called at every simulation iteration. 
  impl_->update_connection_ = gazebo::event::Events::ConnectWorldUpdateBegin(
    std::bind(&ROS2PrismaticPluginPrivate::OnUpdate, impl_.get()));

  RCLCPP_INFO(impl_->ros_node_->get_logger(), "GAZEBO Prismatic joint plugin loaded successfully.");
}

void ROS2PrismaticPluginPrivate::OnUpdate()
{
  double joint_current_position = prismatic_joint_->Position(0);

  if (moving_forward_) {
    joint_position_ += speed_ * 0.001;  // Assuming OnUpdate is called every 1 ms
    if ((max_position_ >= 0 && joint_current_position >= max_position_) ||
        (max_position_ < 0 && joint_current_position <= max_position_)) {
      moving_forward_ = false;
    }
  } else {
    joint_position_ -= speed_ * 0.001;
    if ((max_position_ >= 0 && joint_current_position <= 0) ||
        (max_position_ < 0 && joint_current_position >= 0)) {
      moving_forward_ = true;
      speed_ = 0.0;

    }
  }

  prismatic_joint_->SetPosition(0, joint_position_);

  // Publish status at rate
  rclcpp::Time now = ros_node_->get_clock()->now();
  if (now - last_publish_time_ >= rclcpp::Duration(0, update_ns_)) {
    PublishStatus();
    last_publish_time_ = now;
  }
}

void ROS2PrismaticPluginPrivate::SetJointVelocity(
  conveyorbelt_msgs::srv::ConveyorBeltControl::Request::SharedPtr req,
  conveyorbelt_msgs::srv::ConveyorBeltControl::Response::SharedPtr res)
{
  res->success = false;
  if (req->power >= 0 && req->power <= 100) {
    speed_ = req->power;
    res->success = true;
  }
  else{
    RCLCPP_WARN(ros_node_->get_logger(), "Joint speed must be between 0 and 100.");
  }
}

void ROS2PrismaticPluginPrivate::PublishStatus(){
  status_msg_.power = speed_;
  status_msg_.enabled = true;
  status_pub_->publish(status_msg_);
}

GZ_REGISTER_MODEL_PLUGIN(ROS2PrismaticPlugin)
}  // namespace gazebo_ros


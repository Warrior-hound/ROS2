#include "rclcpp/rclcpp.hpp"
#include "my_robot_interfaces/msg/hardware_status.hpp"

class HardwareStatusPublisher : public rclcpp::Node
{
public:
  HardwareStatusPublisher()
  : Node("hw_status_publisher")
  {
    publisher_ = this->create_publisher<my_robot_interfaces::msg::HardwareStatus>("hw_status", 10);
    timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&HardwareStatusPublisher::publish_number, this));
    RCLCPP_INFO(this->get_logger(), "Number Publisher has been started.");
  }

private:
    void publish_number()
    {
        auto message = my_robot_interfaces::msg::HardwareStatus();
        message.temperature = 45;
        message.are_motors_ready = true;
        message.debug_message = "All systems go!";      
        publisher_->publish(message);
    }
    
    rclcpp::Publisher<my_robot_interfaces::msg::HardwareStatus>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    };

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<HardwareStatusPublisher>());
  rclcpp::shutdown();
  return 0;
}
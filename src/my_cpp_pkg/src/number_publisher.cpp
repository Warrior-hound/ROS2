#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int64.hpp"


class NumberPublisher : public rclcpp::Node
{
public:
  NumberPublisher()
  : Node("number_publisher")
  {
    publisher_ = this->create_publisher<std_msgs::msg::Int64>("number", 10);
    timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&NumberPublisher::publish_number, this));
    RCLCPP_INFO(this->get_logger(), "Number Publisher has been started.");
  }

private:
    void publish_number()
    {
        auto message = std_msgs::msg::Int64();
        message.data = number_;
        publisher_->publish(message);
        number_ = number_ + 1;
    }
    
    rclcpp::Publisher<std_msgs::msg::Int64>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    int number_ = 0;
    };

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<NumberPublisher>());
  rclcpp::shutdown();
  return 0;
}
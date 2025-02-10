#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include <memory>

class RobotNewsListener: public rclcpp::Node {
public:
    RobotNewsListener(): Node("robot_news_listener") {
        RCLCPP_INFO(this->get_logger(), "Putting my headphones on");
        this->declare_parameter("robot_name", "Bender");
        robot_name_ = this->get_parameter("robot_name").as_string();
        subscription_ = this->create_subscription<std_msgs::msg::String>(
            "robot_news", 10, std::bind(&RobotNewsListener::handleMessage, this, std::placeholders::_1));
    }

private:
    void handleMessage(const std_msgs::msg::String::SharedPtr msg) {
        RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
    }

    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
    std::string robot_name_;
};

int main(int argsc, char **argsv) {
    rclcpp::init(argsc, argsv);
    auto node = std::make_shared<RobotNewsListener>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
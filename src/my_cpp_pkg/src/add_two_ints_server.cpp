#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"  

using std::placeholders::_1;
using std::placeholders::_2;

class AddTwoIntsServerNode: public rclcpp::Node {
public:
    AddTwoIntsServerNode(): Node("add_two_ints_server") {
        server_  = this->create_service<example_interfaces::srv::AddTwoInts>(
            "add_two_ints", std::bind(&AddTwoIntsServerNode::callback, this, _1, _2));
        RCLCPP_INFO(this->get_logger(), "Add Two Ints Server has been started.");

    }
private:
    rclcpp::Service<example_interfaces::srv::AddTwoInts>::SharedPtr server_;
    void callback(const std::shared_ptr<example_interfaces::srv::AddTwoInts::Request> request,
                  std::shared_ptr<example_interfaces::srv::AddTwoInts::Response> response) {
        response->sum = request->a + request->b;
        RCLCPP_INFO(this->get_logger(), "Incoming request\na: %ld" " b: %ld", request->a, request->b);
        RCLCPP_INFO(this->get_logger(), "Sending back response: %ld", response->sum);
    }

};

int main(int argsc, char **argsv) {
    rclcpp::init(argsc, argsv);
    auto node = std::make_shared<AddTwoIntsServerNode>();
    rclcpp::spin(node); 
    rclcpp::shutdown();
    return 0;
}
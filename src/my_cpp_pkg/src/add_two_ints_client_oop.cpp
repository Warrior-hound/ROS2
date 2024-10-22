#include "rclcpp/rclcpp.hpp"

#include "example_interfaces/srv/add_two_ints.hpp"

class AddTwoIntsClientNode : public rclcpp::Node {
    public:
        AddTwoIntsClientNode(): Node("add_two_ints_client") {
                threads_.push_back(std::thread(std::bind(&AddTwoIntsClientNode::callAddTwoIntsService, this, 3, 4)));
        }
        void callAddTwoIntsService(int a, int b) {
            auto client = this->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");

             while (!client->wait_for_service(std::chrono::seconds(1))) {
                if (!rclcpp::ok()) {
                    RCLCPP_ERROR(this->get_logger(), "Interrupted while waiting for the service. Exiting.");
                    
            }
            RCLCPP_INFO(this->get_logger(), "service not available, waiting again...");
    }
         auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
            request->a = a;
            request->b = b;
            auto future = client->async_send_request(request);

            try {
                auto response = future.get();
                RCLCPP_INFO(this->get_logger(), "Result of %ld + %ld = %ld", request->a, request->b, response->sum);
            } catch (const std::exception &e) {
                RCLCPP_ERROR(this->get_logger(), "Service call failed");
            }

        }
private:
    std::vector<std::thread> threads_;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<AddTwoIntsClientNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
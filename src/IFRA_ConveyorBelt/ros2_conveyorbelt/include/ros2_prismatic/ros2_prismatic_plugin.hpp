// ros2_prismatic_plugin.hpp
#ifndef ROS2_PRISMATIC_PLUGIN_HPP
#define ROS2_PRISMATIC_PLUGIN_HPP

#include <gazebo/common/Plugin.hh>
#include <memory>

namespace gazebo_ros
{
  class ROS2PrismaticPluginPrivate;

  class ROS2PrismaticPlugin : public gazebo::ModelPlugin
  {
  public:
    ROS2PrismaticPlugin();
    virtual ~ROS2PrismaticPlugin();
    void Load(gazebo::physics::ModelPtr _model, sdf::ElementPtr _sdf) override;

  private:
    std::unique_ptr<ROS2PrismaticPluginPrivate> impl_;
  };
}

#endif // ROS2_PRISMATIC_PLUGIN_HPP
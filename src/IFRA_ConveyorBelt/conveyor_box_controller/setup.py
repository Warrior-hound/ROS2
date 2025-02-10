from setuptools import find_packages, setup

package_name = 'conveyor_box_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='meditab',
    maintainer_email='meditab@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'spawn_boxes = conveyor_box_controller.spawn_boxes:main',
            'conveyor_starter = conveyor_box_controller.power_conveyors:main',
            'read_image = conveyor_box_controller.read_image:main',
            'control_medium_conveyor = conveyor_box_controller.control_medium_conveyor:main',
            'spawn_stickers = conveyor_box_controller.spawn_stickers:main',
        ],
    },
)

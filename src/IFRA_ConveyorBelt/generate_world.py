import xml.etree.ElementTree as ET
import os

def modify_ir_sdf(namespace):
    tree = ET.parse('/home/meditab/Desktop/ROS2/src/IFRA_ConveyorBelt/conveyorbelt_gazebo/models/ir/ir.sdf')
    root = tree.getroot()

    for plugin in root.iter('plugin'):
        for ros in plugin.iter('ros'):
            for ns in ros.iter('namespace'):
                ns.text = namespace

    model_dir = f'/home/meditab/Desktop/ROS2/src/IFRA_ConveyorBelt/conveyorbelt_gazebo/models/ir/ir_{namespace}'
    os.makedirs(model_dir, exist_ok=True)
    modified_sdf_path = os.path.join(model_dir, f'ir_{namespace}.sdf')
    tree.write(modified_sdf_path)
    
    model_config_content = f"""<?xml version="1.0"?>
<model>
  <name>IR Sensor {namespace}</name>
  <version>1.0</version>
  <sdf version='1.6'>ir_{namespace}.sdf</sdf>
  <author>
    <name>Mikel Bueno Viso</name>
    <email>Mikel.Bueno-Viso@cranfield.ac.uk</email>
  </author>
  <description>
    IR Sensor model for {namespace}.
  </description>
</model>
"""
    with open(os.path.join(model_dir, 'model.config'), 'w') as f:
        f.write(model_config_content)
    
    return f'model://ir_{namespace}'


def modify_secondary_line_sdf(namespace):
    tree = ET.parse('/home/meditab/Desktop/ROS2/src/IFRA_ConveyorBelt/conveyorbelt_gazebo/models/secondary_line/secondary_line.sdf')
    root = tree.getroot()

    for plugin in root.iter('plugin'):
        for ros in plugin.iter('ros'):
            for ns in ros.iter('namespace'):
                ns.text = namespace

    model_dir = f'/home/meditab/Desktop/ROS2/src/IFRA_ConveyorBelt/conveyorbelt_gazebo/models/secondary_line/secondary_line_{namespace}'
    os.makedirs(model_dir, exist_ok=True)
    modified_sdf_path = os.path.join(model_dir, f'secondary_line_{namespace}.sdf')
    tree.write(modified_sdf_path)
    
    model_config_content = f"""<?xml version="1.0"?>
<model>
  <name>Secondary Line 2 {namespace}</name>
  <version>1.0</version>
  <sdf version='1.6'>secondary_line_{namespace}.sdf</sdf>
  <author>
    <name>Mikel Bueno Viso</name>
    <email>Mikel.Bueno-Viso@cranfield.ac.uk</email>
  </author>
  <description>
    Secondary line 2 for {namespace}.
  </description>
</model>
"""
    with open(os.path.join(model_dir, 'model.config'), 'w') as f:
        f.write(model_config_content)
    
    return f'model://secondary_line_{namespace}'

def modify_secondary_line_2_sdf(namespace):
    tree = ET.parse('/home/meditab/Desktop/ROS2/src/IFRA_ConveyorBelt/conveyorbelt_gazebo/models/secondary_line_2/secondary_line_2.sdf')
    root = tree.getroot()

    for plugin in root.iter('plugin'):
        for ros in plugin.iter('ros'):
            for ns in ros.iter('namespace'):
                ns.text = namespace

    model_dir = f'/home/meditab/Desktop/ROS2/src/IFRA_ConveyorBelt/conveyorbelt_gazebo/models/secondary_line_2/secondary_line_2_{namespace}'
    os.makedirs(model_dir, exist_ok=True)
    modified_sdf_path = os.path.join(model_dir, f'secondary_line_2_{namespace}.sdf')
    tree.write(modified_sdf_path)
    
    model_config_content = f"""<?xml version="1.0"?>
<model>
  <name>Secondary Line 2 {namespace}</name>
  <version>1.0</version>
  <sdf version='1.6'>secondary_line_2_{namespace}.sdf</sdf>
  <author>
    <name>Mikel Bueno Viso</name>
    <email>Mikel.Bueno-Viso@cranfield.ac.uk</email>
  </author>
  <description>
    Secondary line 2 for {namespace}.
  </description>
</model>
"""
    with open(os.path.join(model_dir, 'model.config'), 'w') as f:
        f.write(model_config_content)
    
    return f'model://secondary_line_2_{namespace}'

def modify_medium_conveyor_sdf(namespace):
    tree = ET.parse('/home/meditab/Desktop/ROS2/src/IFRA_ConveyorBelt/conveyorbelt_gazebo/models/medium_line/medium_line.sdf')
    root = tree.getroot()

    for plugin in root.iter('plugin'):
        for ros in plugin.iter('ros'):
            for ns in ros.iter('namespace'):
                ns.text = namespace

    model_dir = f'/home/meditab/Desktop/ROS2/src/IFRA_ConveyorBelt/conveyorbelt_gazebo/models/medium_line/medium_line_{namespace}'
    os.makedirs(model_dir, exist_ok=True)
    modified_sdf_path = os.path.join(model_dir, f'medium_line_{namespace}.sdf')
    tree.write(modified_sdf_path)
    
    model_config_content = f"""<?xml version="1.0"?>
<model>
  <name>Conveyor Belt {namespace}</name>
  <version>1.0</version>
  <sdf version='1.6'>medium_line_{namespace}.sdf</sdf>
  <author>
    <name>Krishil Patel</name>
    <email>krishilpatel61@gmail.com</email>
  </author>
  <description>
    Medium conveyor model for {namespace}.
  </description>
</model>
"""
    with open(os.path.join(model_dir, 'model.config'), 'w') as f:
        f.write(model_config_content)
    
    return f'model://medium_line_{namespace}'

def modify_pusher_sdf(namespace):
    tree = ET.parse('/home/meditab/Desktop/ROS2/src/IFRA_ConveyorBelt/conveyorbelt_gazebo/models/pusher/pusher.sdf')
    root = tree.getroot()

    for plugin in root.iter('plugin'):
        for ros in plugin.iter('ros'):
            for ns in ros.iter('namespace'):
                ns.text = namespace

    model_dir = f'/home/meditab/Desktop/ROS2/src/IFRA_ConveyorBelt/conveyorbelt_gazebo/models/pusher/pusher_{namespace}'
    os.makedirs(model_dir, exist_ok=True)
    modified_sdf_path = os.path.join(model_dir, f'pusher_{namespace}.sdf')
    tree.write(modified_sdf_path)
    
    model_config_content = f"""<?xml version="1.0"?>
<model>
  <name>Pusher {namespace}</name>
  <version>1.0</version>
  <sdf version='1.6'>pusher_{namespace}.sdf</sdf>
  <author>
    <name>Krishil Patel</name>
    <email>krishilpatel61@gmail.com</email>
  </author>
  <description>
    Medium conveyor model for {namespace}.
  </description>
</model>
"""
    with open(os.path.join(model_dir, 'model.config'), 'w') as f:
        f.write(model_config_content)
    
    return f'model://pusher_{namespace}'

def modify_scanner_sdf(namespace):
    tree = ET.parse('/home/meditab/Desktop/ROS2/src/IFRA_ConveyorBelt/conveyorbelt_gazebo/models/scanner/scanner.sdf')
    root = tree.getroot()

    for plugin in root.iter('plugin'):
        for ros in plugin.iter('ros'):
            for ns in ros.iter('namespace'):
                ns.text = namespace

    model_dir = f'/home/meditab/Desktop/ROS2/src/IFRA_ConveyorBelt/conveyorbelt_gazebo/models/scanner/scanner_{namespace}'
    os.makedirs(model_dir, exist_ok=True)
    modified_sdf_path = os.path.join(model_dir, f'scanner_{namespace}.sdf')
    tree.write(modified_sdf_path)
    
    model_config_content = f"""<?xml version="1.0"?>
<model>
    <name>Scanner {namespace}</name>
    <version>1.0</version>
    <sdf version='1.6'>scanner_{namespace}.sdf</sdf>
    <author>
        <name>Mikel Bueno Viso</name>
       <email>krishilpatel61@gmail.com</email>
  </author>
  <description>
    Scanner for {namespace}.
  </description>
</model>
"""
    with open(os.path.join(model_dir, 'model.config'), 'w') as f:
        f.write(model_config_content)
    
    return f'model://scanner_{namespace}'


    

def create_include_element(name, pose, uri):
    include = ET.Element('include')
    
    name_elem = ET.SubElement(include, 'name')
    name_elem.text = name
    
    pose_elem = ET.SubElement(include, 'pose')
    pose_elem.text = pose
    
    uri_elem = ET.SubElement(include, 'uri')
    uri_elem.text = uri
    
    return include

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def generate_world_file():
    root = ET.Element('sdf', version="1.6")
    world = ET.SubElement(root, 'world', name="default")
    
    # Add other elements to the world as needed
    # ...

    # Add IR sensor instances
    ir_poses = [
        "-12.555 -3.08 0 0 0 0",
        "-10.495 -3.08 0 0 0 0",
        "-6.637 -3.08 0 0 0 0",
        "-4.577 -3.08 0 0 0 0",
        "-2.517 -3.08 0 0 0 0",
        "-0.457 -3.08 0 0 0 0",
        "-12.555 -3.08 0 0 0 0",
        "-10.495 -3.08 0 0 0 0",
        "-6.637 -3.08 0 0 0 0",
        "-4.577 -3.08 0 0 0 0",
        "-2.517 -3.08 0 0 0 0",
        "-0.457 -3.08 0 0 0 0",
        "-12.555 -3.08 0 0 0 0",
        "-10.495 -3.08 0 0 0 0",
        "-6.637 -3.08 0 0 0 0",
        "-4.577 -3.08 0 0 0 0",
        "-2.517 -3.08 0 0 0 0",
        "-0.457 -3.08 0 0 0 0",
        "-12.555 -3.08 0 0 0 0",
        "-10.495 -3.08 0 0 0 0",
        "-6.637 -3.08 0 0 0 0",
        "-4.577 -3.08 0 0 0 0",
        "-2.517 -3.08 0 0 0 0",
        "-0.457 -3.08 0 0 0 0",
         "-12.555 -3.08 0 0 0 0",
        "-10.495 -3.08 0 0 0 0",
        "-6.637 -3.08 0 0 0 0",
        "-4.577 -3.08 0 0 0 0",
        "-2.517 -3.08 0 0 0 0",
        "-0.457 -3.08 0 0 0 0",
    ]

    medium_poses = [
        '-12.555 -3.08 0 0 0 0',
        '-10.495 -3.08 0 0 0 0',
        '-6.637 -3.08 0 0 0 0',
        '-4.577 -3.08 0 0 0 0',
         '-4.577 -3.08 0 0 0 0',
    ]

    secondary_line_2_poses = [
        '-12.555 -3.08 0 0 0 0',
        '-10.495 -3.08 0 0 0 0',
        '-6.637 -3.08 0 0 0 0',
        '-4.577 -3.08 0 0 0 0',
        '-12.555 -3.08 0 0 0 0',
        '-10.495 -3.08 0 0 0 0',
        '-6.637 -3.08 0 0 0 0',
        '-4.577 -3.08 0 0 0 0'
        
    ]

    secondary_line_poses = [
        '-12.555 -3.08 0 0 0 0',
        '-10.495 -3.08 0 0 0 0',
        '-6.637 -3.08 0 0 0 0',
        '-4.577 -3.08 0 0 0 0',
        '-12.555 -3.08 0 0 0 0',
        '-10.495 -3.08 0 0 0 0',
        '-6.637 -3.08 0 0 0 0',
        '-4.577 -3.08 0 0 0 0'
    ]
    
    for i, pose in enumerate(ir_poses, start=1):
        namespace = f'ir{i}'
        print(namespace)
        uri = modify_ir_sdf(namespace)
        include = create_include_element(f'ir_{i}', pose, uri)
        world.append(include)

    for i, pose in enumerate(medium_poses, start=1):
        namespace = f'medium_line{i}'
        print(namespace)
        uri = modify_medium_conveyor_sdf(namespace)
       
        include = create_include_element(f'medium_line_{i}', pose, uri)
        world.append(include)
    
    for i, pose in enumerate(medium_poses, start=1):
        namespace = f'pusher_{i}'
        print(namespace)
        uri = modify_pusher_sdf(namespace)
       
        include = create_include_element(f'pusher_{i}', pose, uri)
        world.append(include)

    for i, pose in enumerate(medium_poses, start=1):
        namespace = f'scanner_{i}'
        print(namespace)
        uri = modify_scanner_sdf(namespace)
       
        include = create_include_element(f'scanner_{i}', pose, uri)
        world.append(include)

    for i, pose in enumerate(secondary_line_2_poses, start=1):
        namespace = f'secondary_line_2_{i}'
        print(namespace)
        uri = modify_secondary_line_2_sdf(namespace)
        include = create_include_element(f'secondary_line_2_{i}', pose, uri)
        world.append(include)

    for i, pose in enumerate(secondary_line_poses, start=1):
        namespace = f'secondary_line_{i}'
        print(namespace)
        uri = modify_secondary_line_sdf(namespace)
        include = create_include_element(f'secondary_line_{i}', pose, uri)
        world.append(include)
    
    indent(root)
    tree = ET.ElementTree(root)
    # tree.write('/home/meditab/Desktop/ROS2/src/IFRA_ConveyorBelt/conveyorbelt_gazebo/worlds/conveyorbelt_generated.world', xml_declaration=True, encoding='utf-8', method="xml")

if __name__ == "__main__":
    generate_world_file()
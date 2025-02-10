initial_poses = [[-29.945, -1.36, 0, 0, 0, 0],
                 [-42.5, -1.02 ,0 ,0 ,0 ,0],
                 [-36.575, -2.03 ,0 ,0 ,0 ,0],
                 [-42.5, 0.6 ,0 ,0 ,0 ,0],
                 [-42.955, -1.66 ,0 ,0 ,0 ,1.393102],
                 [-42.5 ,-3.08 ,0 ,0 ,0 ,0],
                 [-40.44 ,-3.08 ,0 ,0 ,0 ,0],
                 [-36.582, -3.08 ,0 ,0 ,0 ,0],
                 [-33.603, -3.08 ,0 ,0 ,0 ,0],
                 [-31.54 ,-3.08 ,0 ,0 ,0 ,0],
                 [-29.945, -3.08 ,0 ,0 ,0 ,0]
                ]

add_pose = [17.8, 0, 0, 0, 0, 0]

def generate_zone_poses(initial_poses, add_pose, zone_number):
    zone_poses = []
    for pose in initial_poses:
        new_pose = [pose[i] + add_pose[i] * (zone_number - 1) for i in range(len(pose))]
        zone_poses.append(new_pose)
    return zone_poses

def generate_zone_uris(names, uris, zone_number):
    new_names = []
    new_uris = []
    for i, name in enumerate(names):
        new_name = name.replace("zone1", f"zone{zone_number}")
        if "ir" in name:
            new_name = f"ir_{i + 2 + ((zone_number - 2) * 6)}"
        elif "medium" in name:
            new_name = f"medium_{zone_number}"
        elif "pusher" in name:
            new_name = f"pusher_{zone_number}"
        elif "scanner" in name:
            new_name = f"scanner_{zone_number}"
        elif "secondary_belt_2" in name:
            new_name = f"secondary_belt_2_{zone_number}"
        elif "sb_zone" in name:
            new_name = f"sb_zone{zone_number}"
        new_names.append(new_name)

        
        new_uri = uris[i]
        if "secondary_line_secondary_line_1" in new_uri:
            new_uri = new_uri.replace("secondary_line_secondary_line_1", f"secondary_line_secondary_line_{zone_number}")
        elif "secondary_line_2_secondary_line_2_1" in new_uri:
            new_uri = new_uri.replace("secondary_line_2_secondary_line_2_1", f"secondary_line_2_secondary_line_2_{zone_number}")
        elif "medium_line" in new_uri:
            new_uri = new_uri.replace("medium_line_medium_line1", f"medium_line_medium_line{zone_number}")
        elif "pusher" in new_uri:
            new_uri = new_uri.replace("pusher_pusher_1", f"pusher_pusher_{zone_number}")
        elif "scanner" in new_uri:
            new_uri = new_uri.replace("scanner_scanner_1", f"scanner_scanner_{zone_number}")
        elif "ir" in new_uri:
            new_uri = f"model://ir/ir_ir{i + 2 + ((zone_number - 2) * 6)}"
        new_uris.append(new_uri)
    return new_names, new_uris

zone_number = 5  # Change this to the desired zone number

zone_poses = generate_zone_poses(initial_poses, add_pose, zone_number)

names = ["sb_zone1", "secondary_belt_2", "medium", "pusher_1", "scanner_1", "ir_1", "ir_2", "ir_3", "ir_4", "ir_5", "ir_6"]
uris = ["model://secondary_line/secondary_line_secondary_line_1",
        "model://secondary_line_2/secondary_line_2_secondary_line_2_1",
        "model://medium_line/medium_line_medium_line1",
        "model://pusher/pusher_pusher_1",
        "model://scanner/scanner_scanner_1",
        "model://ir/ir_ir1",
        "model://ir/ir_ir2",
        "model://ir/ir_ir3",
        "model://ir/ir_ir4",
        "model://ir/ir_ir5",
        "model://ir/ir_ir6"]

new_names, new_uris = generate_zone_uris(names, uris, zone_number)

for i, pose in enumerate(zone_poses):
    print(f"    <include>")
    print(f"      <name>{new_names[i]}</name>")
    print(f"      <pose>{' '.join(map(str, pose))}</pose>")
    print(f"      <uri>{new_uris[i]}</uri>")
    if "ir" in new_names[i]:
        print(f"      <namespace>{new_names[i]}</namespace>")
    print(f"    </include>")
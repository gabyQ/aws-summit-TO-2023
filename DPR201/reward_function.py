def reward_function(params):

    # Read input parameters
    track_width = params['track_width']
    progress = params['progress']
    distance_from_center = params['distance_from_center']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints'] # indices of closest_waypoints
    
    # Parse input params
    waypoint1 = waypoints[closest_waypoints[0]]
    waypoint2 = waypoints[closest_waypoints[1]]
    
    x = params['x']
    y = params['y']
    
    waypoint1_x_distance = x - waypoint1[0]
    waypoint1_y_distance = y - waypoint1[1]
    waypoint2_x_distance = x - waypoint2[0]
    waypoint2_y_distance = y - waypoint2[1]
    
    # Give higher reward if the car is close to the farther waypoints
    if waypoint2_x_distance == 0 and waypoint2_y_distance == 0:
        reward = 1.0
    elif waypoint2_x_distance < 0.3 or waypoint2_y_distance < 0.3:
        reward = 0.5
    elif waypoint2_x_distance < 0.6 or waypoint2_y_distance < 0.6:
        reward = 0.3
    elif waypoint2_x_distance < 0.9 or waypoint2_y_distance < 0.9:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    return float(reward)
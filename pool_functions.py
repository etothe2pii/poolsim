from pool_objects import Ball, Table, Collision
import math



def collide(b1: Ball, b2: Ball, time) -> None:
    # Calculate the difference in position and velocity
    b1_position = b1.get_position(time)
    b2_position = b2.get_position(time)
    b1_velocity = b1.get_velocity(time)
    b2_velocity = b2.get_velocity(time)

    dp = (b1_position[0] - b2_position[0], b1_position[1] - b2_position[1])
    dv = (b1_velocity[0] - b2_velocity[0], b1_velocity[1] - b2_velocity[1])
    
    # Calculate the unit normal vector
    distance = math.sqrt(dp[0]**2 + dp[1]**2)
    n = (dp[0] / distance, dp[1] / distance)
    
    # Calculate the relative velocity along the line of collision
    v_rel = dv[0]*n[0] + dv[1]*n[1]
    
    # Check if balls are moving towards each other
    if v_rel > 0:
        # Calculate the impulse
        J = 2 * b1.mass * b2.mass * v_rel / (b1.mass + b2.mass)
        
        # Calculate the change in velocity due to the impulse for each ball
        delta_v1 = (J / b1.mass * n[0], J / b1.mass * n[1])
        delta_v2 = (-J / b2.mass * n[0], -J / b2.mass * n[1])
        
        # Update the velocities of the balls
        b1.velocity = (b1.velocity[0] - delta_v1[0], b1.velocity[1] - delta_v1[1])
        b2.velocity = (b2.velocity[0] - delta_v2[0], b2.velocity[1] - delta_v2[1])

        b1.start_position = b1_position
        b2.start_position = b2_position

        b1.start_time = time
        b2.start_time = time
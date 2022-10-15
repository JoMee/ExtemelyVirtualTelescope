from datetime import datetime
import math

###
# We assume a datetime format of "%Y-%m-%d %H:%M:%S.%f"
# A string can be converted into and from this format by the following commands
# datetime.strptime(input_string, '%Y-%m-%d %H:%M:%S.%f')                           ## convert string to datetime object
# datetime_object.strftime('%Y-%m-%d %H:%M:%S.%f')                                  ## convert datetime object to string

def get_initial_state(): 

    initial_state = {
                'timestamp': '2000-01-01 00:00:00.000000',
                'altitude': 0.0,
                'azimuth': 0.0,
                'door_open': True,
                'door_state': 1.0
            }

    telescope_properties = {
            'azimuthal_velocity': 2.0,
            'altitudal_velocity': 2.0,
            'min_altitudal_angle': 0.0,
            'max_altitudal_angle': 90.0,
            'min_door_state': 0.0,
            'max_door_state': 1.0,
            'door_velocity': 0.1,
            }

    return {'old_state': initial_state, 'updated_state': initial_state, 'properties': telescope_properties} 


# helper function for compute_current_state function
def interpolate_to_new_state(old_value, value_difference, time_difference, transition_speed):

    if (math.fabs(value_difference) < 0.00001):
        return old_value


    transition_time = math.fabs(value_difference) / transition_speed
    print(time_difference)
    print(transition_time)
    
    transition_fraction = min(time_difference / transition_time, 1.0)
    
    return old_value + transition_fraction * value_difference

def compute_current_state(stored_object):

    timestamp_now = datetime.now()
    timestamp_old = datetime.strptime(stored_object['updated_state']['timestamp'], '%Y-%m-%d %H:%M:%S.%f')

    time_difference = (timestamp_now - timestamp_old).total_seconds()

   
    #compute current altitude from two states
    current_altitude = interpolate_to_new_state(stored_object['old_state']['altitude'],
                                                stored_object['updated_state']['altitude'] - stored_object['old_state']['altitude'],
                                                time_difference,
                                                stored_object['properties']['altitudal_velocity'])

    current_altitude = max(stored_object['properties']['min_altitudal_angle'], current_altitude)
    current_altitude = min(stored_object['properties']['max_altitudal_angle'], current_altitude)


    #compute current door state from two states
    current_door_state = interpolate_to_new_state(stored_object['old_state']['door_state'],
                                                stored_object['updated_state']['door_state'] - stored_object['old_state']['door_state'],
                                                time_difference,
                                                stored_object['properties']['door_velocity'])
    
    current_door_state = max(stored_object['properties']['min_door_state'], current_door_state)
    current_door_state = min(stored_object['properties']['max_door_state'], current_door_state)


    #compute current azimuth from two states (kinda ugly but i hope understandable, also in degrees - ew)
    azimuth_difference = stored_object['updated_state']['azimuth'] - stored_object['old_state']['azimuth']

    if (azimuth_difference < 0.0):
        #make difference positive
        azimuth_difference += 360.0

    if (azimuth_difference > 180.0):
        #go the other way
        azimuth_difference = azimuth_difference - 360.0

    current_azimuth = interpolate_to_new_state(stored_object['old_state']['azimuth'],
                                            azimuth_difference,
                                            time_difference,
                                            stored_object['properties']['azimuthal_velocity']) 
        
    # make current_azimuth into range of [0, 360]
    factor = current_azimuth / 360.0
    current_azimuth = current_azimuth + (-1) * math.floor(factor) * 360

    

    timestamp_string = timestamp_now.strftime('%Y-%m-%d %H:%M:%S.%f') 
    door_open = stored_object['updated_state']['door_open']

    current_state= {
                'timestamp': timestamp_string, 
                'altitude': current_altitude, 
                'azimuth': current_azimuth, 
                'door_open': door_open,
                'door_state': current_door_state 
            }

    return current_state 

def update_state(state_file, new_state):
    new_state_file = state_file

    current_state = compute_current_state(state_file)

    new_state_file['old_state'] = current_state

    new_state['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    new_state_file['updated_state'] = new_state

    return new_state_file

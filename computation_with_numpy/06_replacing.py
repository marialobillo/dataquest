is_value_empty = world_alcohol[:, 4] == ''

world_alcohol[:,4][world_alcohol[:, 4] == ''] = 0

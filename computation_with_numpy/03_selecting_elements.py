country_is_algeria = (world_alcohol[:, 2] == "Algeria" )

country_algeria = world_alcohol[country_is_algeria, :]

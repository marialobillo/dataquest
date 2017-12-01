is_algeria_and_1986 = (world_alcohol[:, 2] == "Algeria") & (world_alcohol[:,0] == "1986")

rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

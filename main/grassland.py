for i in range(get_world_size()):
	for j in range(get_world_size()):
		if get_entity_type()!=None:
			while can_harvest()==False:
				continue
			harvest()
		if get_ground_type()==Grounds.Soil:
			till()
		move(North)
	move(East)
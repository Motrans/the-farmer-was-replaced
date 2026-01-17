for i in range(get_world_size()):
	for j in range(get_world_size()):
		if get_entity_type()!=None:
			while can_harvest()==False:
				continue
			harvest()
		if get_ground_type()==Grounds.Grassland:
			till()
		plant(Entities.Sunflower)
		move(North)
	move(East)
while True:
	for i in range(get_world_size()):
		while can_harvest()==False:
			continue
		harvest()
		plant(Entities.Sunflower)
		move(North)
	move(East)
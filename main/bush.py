for i in range(get_world_size()):
	for j in range(get_world_size()):
		if get_entity_type()!=None:
			while can_harvest()==False:
				continue
			harvest()
		plant(Entities.Bush)
		move(North)
	move(East)
while True:
	for i in range(get_world_size()):
		while can_harvest()==False:
			continue
		harvest()
		plant(Entities.Bush)
		move(North)
	move(East)
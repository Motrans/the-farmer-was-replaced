for i in range(get_world_size()):
	for j in range(get_world_size()/2):
		if get_entity_type()!=None:
			while can_harvest()==False:
				continue
			harvest()
		plant(Entities.Tree)
		move(North)
		move(North)
	move(East)
	move(North)
while True:
	for i in range(get_world_size()/2):
		while can_harvest()==False:
			continue
		harvest()
		plant(Entities.Tree)
		move(North)
		move(North)
	move(East)
	move(North)
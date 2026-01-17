list=[Entities.Grass,Entities.Bush,Entities.Carrot]
for i in range(get_world_size()):
	for j in range(get_world_size()):
		if get_entity_type()!=None:
			while can_harvest()==False:
				continue
			harvest()
		if get_ground_type()==Grounds.Grassland:
			till()
		plant(list[j%3])
		move(North)
	move(East)
while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(list[i%3])
		move(North)
	move(East)
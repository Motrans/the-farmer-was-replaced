clear()
while can_harvest()==False:
	continue
for i in range(get_world_size()):
	for j in range(get_world_size()):
		harvest()
		till()
		plant(Entities.Carrot)
		move(North)
	move(East)
while True:
	for i in range(get_world_size()):
		while can_harvest()==False:
			continue
		harvest()
		plant(Entities.Carrot)
		move(North)
	move(East)
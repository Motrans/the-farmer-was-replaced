clear()
while True:
	for i in range(get_world_size()):
		while can_harvest()==False:
			continue
		harvest()
		move(North)
	move(East)
def single(size=5):
	move(South)
	for i in range(size):
		for j in range(size):
			if i%2==0:
				move(North)
				if get_ground_type()==Grounds.Grassland:
					till()
				plant(Entities.Pumpkin)
			else:
				if get_ground_type()==Grounds.Grassland:
					till()
				plant(Entities.Pumpkin)
				move(South)
		move(East)
	move(West)
	if size%2==0:
		move(North)
		for i in range(size-1):
			move(West)
	else:
		for i in range(size-1):
			move(South)
			move(West)
	# 查找坏南瓜
	k=1
	while k>0:
		k=1
		move(South)
		for i in range(size):
			for j in range(size):
				if i%2==0:
					move(North)
					if not can_harvest():
						k+=1
						if get_entity_type()==Entities.Dead_Pumpkin:
							plant(Entities.Pumpkin)
				else:
					if not can_harvest():
						k+=1
						if get_entity_type()==Entities.Dead_Pumpkin:
							plant(Entities.Pumpkin)
					move(South)
			move(East)
		move(West)
		if size%2==0:
			move(North)
			for i in range(size-1):
				move(West)
		else:
			for i in range(size-1):
				move(South)
				move(West)
		k-=1
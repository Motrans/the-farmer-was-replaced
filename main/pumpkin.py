def single(size=5):
	x=get_pos_x()
	y=get_pos_y()
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
	while get_pos_x()!=x:
		move(West)
	while get_pos_y()!=y:
		move(South)
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
		while get_pos_x()!=x:
			move(West)
		while get_pos_y()!=y:
			move(South)
		k-=1


while __name__=="__main__":
	single(3)
	harvest()
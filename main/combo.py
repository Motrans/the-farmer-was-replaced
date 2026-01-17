# 此文件中的函数用于多种作物依规律种植

# 多种作物从下到上、从左到右依次种植
# 每向右一列，向上错开 offset 行
# 调用前需要先为 combo.list 赋值
# 对于不种植作物的空置地块，请赋值为 None
def simple(offset=0):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_entity_type()!=None:
				while can_harvest()==False:
					continue
				harvest()
			if get_ground_type()==Grounds.Grassland:
				till()
			if list[j%len(list)]!=None:
				plant(list[j%len(list)])
			move(North)
		move(East)
		for j in range(offset):
			move(North)
	while True:
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				if list[j%len(list)]!=None:
					plant(list[i%len(list)])
			move(North)
		move(East)
		for i in range(offset):
			move(North)
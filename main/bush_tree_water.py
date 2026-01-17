list=[Entities.Bush,Entities.Tree]
for i in range(get_world_size()):
	for j in range(get_world_size()):
		if get_entity_type()!=None:
			while can_harvest()==False:
				continue
			harvest()
		plant(list[j%2])
		if j%2==0:
			use_item(Items.Water)
			quick_print("当前地块含水量：",get_water())
		move(North)
	move(East)
	move(North)
while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(list[i%2])
		if i%2==0:
			use_item(Items.Water)
			quick_print("当前地块含水量：",get_water())
		move(North)
	move(East)
	move(North)
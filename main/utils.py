# Utility Functions Library

# Harvest all crops and remove all dead pumpkins
# Wait in place if the crop is not fully grown
def gather():
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			reap()
			move(North)
		move(East)

# Move to the grid coordinates (x, y)
# Both x and y default to 0
# Error on out-of-range values
# Floor any decimal inputs for x and y
def goto(x=0,y=0):
	if 0<=x<=get_world_size()-1 and 0<=y<=get_world_size()-1:
		while get_pos_x()<x:
			move(East)
		while get_pos_x()>x:
			move(West)
		while get_pos_y()<y:
			move(North)
		while get_pos_y()>y:
			move(South)
	else:
		print("ERROR: Out of bounds. Both x and y should be non-negative integers no greater than",get_world_size()-1,".")

# Set all tiles to grassland when type = 0
# Set all tiles to soil when type = 1
# Type defaults to 1
# Error on out-of-range values
# Wait in place if the crop is not fully grown
def pave(type=1):
	if type not in {0,1}:
		print("ERROR: Invalid Type. Only 0 or 1 are allowed.")
	else:
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				reap()
				if type==0 and get_ground_type()==Grounds.Soil:
					till()
				elif type==1 and get_ground_type()==Grounds.Grassland:
					till()
				move(North)
			move(East)

# Harvest the crop or remove the dead pumpkin from the current tile
# Wait in place if the crop is not fully grown
def reap():
	while can_harvest()==False and get_entity_type() not in {None, Entities.Dead_Pumpkin}:
		continue
	harvest()
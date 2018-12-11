def loc_min_max(func):
	if func == 1: #sphere
		return 5.0,5.0
	elif func == 2: #ackley
		return 16.0,32.0
	elif func == 3: #rosebrock
		return 15.0,30.0
	elif func == 4: #ras
		return 2.56,5.12


def vel_min_max(func):
	if func == 1: #sphere
		return 5.0,5.0
	elif func == 2: #ackley
		return -2.0,4.0
	elif func == 3: #rosebrock
		return -2.0,2.0
	elif func == 4: #ras
		return -2.0,4.0

class Function(IntEnum):
    Sphere = 1
    Ackley = 2
    Rosenbrock = 3
    Rastrigin = 4

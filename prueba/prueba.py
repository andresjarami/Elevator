import random
import pygame
import simpy

from Rider 		import Rider
from Elevator	import Elevator
from building	import Building

"""
This is the main run file. It creates an enviorment for simpy and then attaches that to each elevator and rider. 
Then starts up pygame. The elevator has sprites which are connected to pygame
"""

RANDOM_SEED		 = 42 #TODO Implement
NUM_OF_ELEVATORS = 3 #How many elevators
NUM_OF_RIDERS	 = 2 #How many Riders

env = simpy.RealtimeEnvironment(initial_time=0, factor=0.9, strict=False)


def f1():
    while True:
        yield (x*2 for x in range(3))



q=(x*2 for x in range(3))
env.process(q)
for elevator in elevators:
	env.process(elevator.run())
env.process(matrix.run())

#Length of runtime(In intervals but not accurate due to concurrency and speed of computer)
env.run(until= 9000)

from simulation.speedLimits import *
from simulation.trafficGenerators import * 

maxFps= 40
size = width, heigth = 1280, 800
# in miliseconds
updateFrame = 500

lanes = 14
length = 190

maxSpeed = 5
maxLength = 1000

speedLimits = [ SpeedLimit(range=((50, y), (100, y+1)), limit=0, ticks=0) for y in range(0, lanes, 4)] + [SpeedLimit(range=((20, y), (50,y)), limit=0, ticks=0) for y in [0, lanes-1]]
trafficGenerator = SimpleTrafficGenerator(2)
slowDownProbability, laneChangeProbability = 0.3, 0.2

import pygame
from RRTbasePy import RRTGraph
from RRTbasePy import RRTMap
import time

def main():
    dimensions = (600, 1000)
    start = (50, 50)
    goal = (510, 510)
    obsdim = 30
    obsnum = 50
    iterations = 0
    initialtime = 0

    pygame.init()
    map = RRTMap(start, goal, dimensions, obsdim, obsnum)
    graph = RRTGraph(start, goal, dimensions, obsdim, obsnum)

    obstacles = graph.makeobs()
    map.drawMap(obstacles)

    initialtime = time.time()
    while not graph.path_to_goal():
        elapsedTime = time.time() - initialtime
        initialtime = time.time()
        if elapsedTime > 10:
            raise Exception("Elapsed Time limit exceeded")

        if iterations % 10 == 0:
            X, Y, Parent = graph.bias(goal)
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad+2, 0)
            pygame.draw.line(map.map, map.Blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]), map.edgeThickness)
        else:
            X, Y, Parent = graph.expand()
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad+2, 0)
            pygame.draw.line(map.map, map.Blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]), map.edgeThickness)

        if iterations % 5 == 0:
            pygame.display.update()
        iterations += 1

    map.drawPath(graph.getPathCoords())
    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait(0)

if __name__ == '__main__':
    result = False
    while not result:
        try:
            main()
            result = True
        except:
            result = False

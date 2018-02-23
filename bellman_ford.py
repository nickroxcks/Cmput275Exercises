#Nicholas Serrano 1508361
#Cmput 275 Exercise 3
#bellman_ford: assumes no negative cycles
import math
infin = math.inf

vertest = {1, 2, 3, 4, 5, 6}
edgetest = {(1,2):10, (3,2):1, (4,3):-2, (5,4):-1, (6,5):1, (1,6):8, (5,2):-4, (2,4):2}

def bellman_ford(vertices, edges, start):
	'''
	Test 1(example given):
	>>> vertice = {1, 2, 3, 4, 5, 6}
	>>> edg = {(1,2):5, (2,5):-7, (3,2):2, (4,1):-2, (5,1):3, (5,3):6, (5,4):4, (6,3):2, (6,5):-10}
	>>> bellman_ford(vertice,edg,1)
	({1: 0, 2: 5, 3: 4, 4: 2, 5: -2}, {1: 1, 2: 1, 3: 5, 4: 5, 5: 2})
	
	test2:
	>>> vertest = {1, 2, 3, 4, 5, 6}
	>>> edgetest = {(1,2):10, (3,2):1, (4,3):-2, (5,4):-1, (6,5):1, (1,6):8, (5,2):-4, (2,4):2}
	>>> bellman_ford(vertest,edgetest,1)
	({1: 0, 2: 5, 3: 5, 4: 7, 5: 9, 6: 8}, {1: 1, 2: 5, 3: 4, 4: 2, 5: 6, 6: 1})
	
	test3:
	>>> vertice = {1, 2, 3, 4, 5, 6}
	>>> edg = {(1,2):5, (1,2):-2, (3,2):7, (2,4):1, (4,5):7, (4,3):2, (3,5):3, (4,6):3, (5,6):10}
	>>> bellman_ford(vertice,edg,1)
	({1: 0, 2: -2, 3: 1, 4: -1, 5: 4, 6: 2}, {1: 1, 2: 1, 3: 4, 4: 2, 5: 3, 6: 4})
	'''
	numedge = len(edges)
	numvertices = len(vertices)
	dist = {}
	reached = {}
	dist[start] = 0
	reached[start] = start
	
	#initially all values in dist are inf. start is 0
	for curvert in vertices:
		if curvert != start:
			dist[curvert] = infin
	
	itnum = 1

	while itnum <= (numvertices-1):
		for eachedge in edges:
			if dist[eachedge[1]] > (dist[eachedge[0]] + edges[eachedge]):
				dist[eachedge[1]] = dist[eachedge[0]] + edges[eachedge]
				reached[eachedge[1]] = eachedge[0]
            

		itnum = itnum + 1
	
	# remove infin vertices in dist
	for v in vertices:
		if dist[v] == infin:
			del dist[v]
	return dist, reached

def find_potential(vertices, edges):
	'''
	Test 1(example given):
	>>> vertice = {1, 2, 3, 4, 5, 6}
	>>> edg = {(1,2):5, (2,5):-7, (3,2):2, (4,1):-2, (5,1):3, (5,3):6, (5,4):4, (6,3):2, (6,5):-10}
	>>> find_potential(vertice,edg)
	{1: 8, 2: 3, 3: 4, 4: 6, 5: 10, 6: 0}
	
	Test2(negative cycle):
	>>> edg[(5,4)] = 3
	>>> find_potential(vertice,edg)
	
	Test3
	>>> edg[(2,5)] = 0
	>>> find_potential(vertice,edg)
	{1: 9, 2: 4, 3: 4, 4: 7, 5: 10, 6: 0}
	'''



	numedge = len(edges)
	numvertices = len(vertices)
	dist = {}
	
	#initially all values in dist are inf. start is 0
	for curvert in vertices:
		dist[curvert] = 0
	
	itnum = 1

	while itnum <= (numvertices-1):
		for eachedge in edges:
			if dist[eachedge[1]] > (dist[eachedge[0]] + edges[eachedge]):
				dist[eachedge[1]] = dist[eachedge[0]] + edges[eachedge]
            

		itnum = itnum + 1
	
	# remove infin vertices in dist and multiply by -1
	for v in vertices:
		if dist[v] == infin:
			del dist[v]
		dist[v] = dist[v]*(-1)
	
	#check for negative cycles
	for test in edges:
		if (dist[test[1]] + edges[test]) < dist[test[0]]:
			return None 
	return dist



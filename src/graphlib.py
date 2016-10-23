
from __future__ import print_function
import networkx as nx

class Statistics:
    """docstring for node."""
    


    def __init__(self, graph):
        self.graph = graph

    def create_statistics():
    	self.degrees_array = get_degrees(self.adj)
    	max_degree = get_max_degree(self.degrees_array)
    	self.histogram = create_histogram(self.degrees_array, max_degree)
    	self.cum_degree = create_cum_degree(self.histogram)

    def print_statistics():


	def create_histogram(degrees_array, max_degree):
		histogram = [0 for j in range(max_degree+1)]
		n = len(degrees_array)
		for i in range(n):
			histogram[degrees_array[i]]+=1
		return histogram

	def create_cum_degree(histogram):
		n = len(histogram)
		cum_degree_array = [0 for j in range(n)]
		for i in range(n):
			for j in range (i, n):
				cum_degree_array[i] += histogram[j]
		return cum_degree_array

	def get_max_degree(degrees_array):
		n = len(degrees_array)
		max_value = degrees_array[0]
		for i in range(1, n):
			if(degrees_array[i]>max_value):
				max_value = degrees_array[i]
		return max_value

	def get_degrees(adjacency_matrix):
		n = len(adjacency_matrix)
		degrees_array = []
		for i in range(n):
			aux_count = 0 
			for j in range(n):
				if(adjacency_matrix[i][j] == 1):
					aux_count = aux_count + 1

			degrees_array.append(aux_count)
		return degrees_array



def print_3d_array(array):
	print("[print_3d_array]")
	n = len(array)
	for i in range (n):
		for j in range (n):
			print (array[i][j], end=" ")
		print ("")	

def print_2d_array(array):
	print("[print_2d_array]")
	n = len(array)
	for i in range(n):
		print(array[i], end=" ")
	print("")

def main():
	#define adjacency_matrix test and its size
	#adjacency_matrix = [[0,1,1],[1,0,1],[1,1,0]]
	#n = 3;

	adj = read_file()

	statistics = Statistics(adj)
	statistics.create_statistics()
	statistics.print_statistics()


def read_file():
    g = nx.read_gml('input/adjnoun.gml')
    nodes = nx.nodes(g)
    size = nx.number_of_nodes(g)
    adj = [[0 for x in range(size)] for y in range(size)]
    for node in nodes:
        edges = nx.edges(g, node)
        for edge in edges:
            adj[ nodes.index(edge[0]) ][ nodes.index(edge[1]) ] = 1
    return adj


if __name__ == "__main__":
    main()

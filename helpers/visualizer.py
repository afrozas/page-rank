import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from helpers.matrix_handler import MatrixHandler
import random

class Visualizer:
	""" The class is responsible for giving a visualization for a directed graph with each node having a rank.
	"""
	
	def __init__(self, nodes, pagerank_list=None):
		""" Initializes the nodes to be drawn, size of the nodes depending on its pagerank and other attributes.
		"""
		self.nodes = nodes
		#self.sizes = pagerank_list
		self.edges = self.filterGraph()
		self.show_time = 10000
		
	def filterGraph(self):
		""" Filters out the edges that have both ends among the relevant nodes that are to be drawn and returns the list of tuples.
		
		A tuple ('A', 'B') among the list of edges denotes a dircted edge from A to B.
		"""
		adjacency_list_outgoing = MatrixHandler.load_adjacency_list_outgoing()
		edges = []

		for node in adjacency_list_outgoing:
			if int(node) in self.nodes:
				for adj_node in adjacency_list_outgoing[node]:
					if int(adj_node) in self.nodes:
						edges.append((node, adj_node))

		return edges
		
	def drawGraph(self):
		""" The main method to draw the graph and show the plot on the canvas. The plot is shown only for a duration of time.
		"""
		G = nx.DiGraph()
		G.add_edges_from(self.edges)
		colors = [random.uniform(0,1) for i in range(len(G.nodes()))]
		# self.sizes = [int(i*10000) for i in self.sizes]
		print(G.nodes())
		fig = plt.figure()
		timer = fig.canvas.new_timer(interval = self.show_time)
		timer.add_callback(plt.close)
		
		nx.draw(G, cmap = plt.get_cmap('jet'), node_size = 5000, node_color = colors, with_labels = True)# node_size = self.sizes)
		plt.show()
		
		

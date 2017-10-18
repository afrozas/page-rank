import json


class MatrixHandler:
	"""
	:provides functions to convert Web Graph to PageRank matrix
	:matrix to be used in power method
	:reads graph as list of edges
	:writes the adjacency matrix for the graph to adjaceny_list.txt
	"""
	def read_dataset_and_generate_matrix():
		"""
		reads dataset from data/web-Stanford.txt and converts to an adjacency matrix
		"""
		adjaceny_list = []

		# given number of nodes = 281903
		# initializing adjacency_list
		for node in range(0,281904):
			connected_nodes = []
			adjaceny_list.append(connected_nodes)

		with open('data/web-Stanford.txt') as dataset:
			# skipping first four lines from the text file as comments
			data = dataset.readlines()[4:]

		for edge in data:
			# each line in read data is a graph edge 
			u,v = edge.split()
			u = int(u)
			v = int(v)
			adjaceny_list[u].append(v)	

		for node in range(0,281904):
			""" update list to the form
			  [node1: [connected_node_1, connected_node_2,.. ],
			  [node2 : [connected_node_1, connected_node_2,.. ], ...] 
			  This is done to be able to convert the list to dict for storing in JSON
			"""	
			row = adjaceny_list[node]
			adjaceny_list[node] = [node, row]																																																																																																																																																																																																																																																																																																																																																																																																


		# convert the list of lists to python dict
		json_dict = dict(adjaceny_list)

		# dump dict as json in file 'data/adjaceny_list.json'
		with open('data/adjaceny_list.json', 'w') as outfile:
			json.dump(json_dict, outfile, sort_keys=True, indent=4)	


	def load_adjacency_list_into_dict():
		"""
		reads JSON data from data/adjacency_list.txt and loads into a dict
		: return: python dict of the format
			{ node1 : {connected_node_1, connected_node_2,.. },
			  node2 : {connected_node_1, connected_node_2,.. }, ...}
		"""
		with open('data/adjaceny_list.json', 'r') as infile:
			return(json.load(infile))



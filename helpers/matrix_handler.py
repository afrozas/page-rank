import json


class MatrixHandler:
	"""
	:provides functions to convert Web Graph to PageRank matrix
	:matrix to be used in power method
	:reads graph as list of edges
	:writes the adjacency matrix for the graph to adjacency_list_outgoing.txt
	"""

	def generate_adjaceny_lists():
		"""
		reads dataset from data/web-stanford.txt and converts to an adjacency list of outgoing links
		"""
		adjacency_list_outgoing = []
		adjacency_list_incoming = []

		# given number of nodes = 281903
		# initializing adjacency_list
		for node in range(0,281904):
			connected_nodes_out = []
			adjacency_list_outgoing.append(connected_nodes_out)

			connected_nodes_in = []
			adjacency_list_incoming.append(connected_nodes_in)

		with open('data/web-stanford.txt') as dataset:
			# skipping first four lines from the text file as comments
			data = dataset.readlines()[4:]

		for edge in data:
			# each line in read data is a graph edge 
			u,v = edge.split()
			u = int(u)
			v = int(v)
			adjacency_list_outgoing[u].append(v)
			adjacency_list_incoming[v].append(u)	

		for node in range(0,281904):
			""" update list to the form
			  [node1: [connected_node_1, connected_node_2,.. ],
			  [node2 : [connected_node_1, connected_node_2,.. ], ...] 
			  This is done to be able to convert the list to dict for storing in JSON
			"""	
			row = adjacency_list_outgoing[node]
			adjacency_list_outgoing[node] = [node, row]	

			row = adjacency_list_incoming[node]
			adjacency_list_incoming[node] = [node, row]																																																																																																																																																																																																																																																																																																																																																																																																

		# convert the list of lists to python dict
		json_dict_out = dict(adjacency_list_outgoing)
		json_dict_in = dict(adjacency_list_incoming)

		# dump dict as json in file 'data/adjacency_list_outgoing.json'
		with open('data/adjacency_list_outgoing.json', 'w') as outfile:
			json.dump(json_dict_out, outfile, sort_keys=True, indent=4)	

		with open('data/adjacency_list_incoming.json', 'w') as outfile:
			json.dump(json_dict_in, outfile, sort_keys=True, indent=4)	


	def load_adjacency_list_outgoing():
		"""
		reads JSON data from data/adjacency_list_outgoing.json and loads into a dict
		: return: python dict of the format
			{ node1 : {connected_node_1, connected_node_2,.. },
			  node2 : {connected_node_1, connected_node_2,.. }, ...}
		"""
		with open('data/adjacency_list_outgoing.json', 'r') as infile:
			return(json.load(infile))


	def load_adjacency_list_incoming():
		"""
		reads JSON data from data/adjacency_list_incoming.json and loads into a dict
		: return: python dict of the format
			{ node1 : {connected_node_1, connected_node_2,.. },
			  node2 : {connected_node_1, connected_node_2,.. }, ...}
		"""
		with open('data/adjacency_list_incoming.json', 'r') as infile:
			return(json.load(infile))

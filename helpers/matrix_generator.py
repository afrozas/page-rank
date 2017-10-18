import json


class MatrixGenerator:
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
			u,v = edge.split()
			u = int(u)
			v = int(v)
			adjaceny_list[u].append(v)	

		for node in range(0,281904):
			row = adjaceny_list[node]
			adjaceny_list[node] = [node, row]																																																																																																																																																																																																																																																																																																																																																																																																


		json_dict = dict(adjaceny_list)
		print(json_dict)
		with open('data/adjaceny_list.txt', 'w') as outfile:
			json.dump(json_dict, outfile, sort_keys=True, indent=4)																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																										


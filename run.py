from helpers.matrix_handler import MatrixHandler


def run():
	"""
	driver function for page rank implementation
	"""

	# uncomment this line if adjacency list is to be regenerated
	MatrixHandler.generate_adjaceny_lists()

	adjacency_list_outgoing = MatrixHandler.load_adjacency_list_outgoing()
	adjacency_list_incoming = MatrixHandler.load_adjacency_list_incoming()

	print(adjacency_list_outgoing['2'])
	print(adjacency_list_incoming['2'])

if __name__ == '__main__':
	run()
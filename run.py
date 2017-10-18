from helpers.matrix_handler import MatrixHandler


def run():
	"""
	driver function for page rank implementation
	"""
	MatrixHandler.read_dataset_and_generate_matrix()

	adjacency_list = MatrixHandler.load_adjacency_list_into_dict()
	#print(adjacency_list)

if __name__ == '__main__':
	run()
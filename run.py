from helpers.matrix_generator import MatrixGenerator


def run():
	"""
	driver function for page rank implementation
	"""
	MatrixGenerator.read_dataset_and_generate_matrix()


if __name__ == '__main__':
	run()
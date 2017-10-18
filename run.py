from helpers.matrix_handler import MatrixHandler
from helpers.page_rank import PageRank
from helpers.trust_rank import TrustRank

def run():
	"""
	driver function for page rank implementation
	"""

	# uncomment this line if adjacency list is to be regenerated
	# MatrixHandler.generate_adjaceny_lists()

	# PageRank.calculate_PageRank()
	TrustRank.calculate_TrustRank()


if __name__ == '__main__':
	run()
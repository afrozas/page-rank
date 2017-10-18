from helpers.matrix_handler import MatrixHandler
from helpers.page_rank import PageRank

class TrustRank:
	"""
	Provides implementation of Google's TrustRank algorithm
	: Teleport set is taken as top 100 pages from PageRank
	"""

	def calculate_TrustRank():
		"""
		provides TrustRank core implementation
		"""
		N = 281904
		trust_rank_t = []
		trust_rank_t1 = []
		iteration = 10
		itr = 0
		beta = 0.85

		pageRank = PageRank()
		trusted_set = pageRank.get_top_page_ranks()
		# print(trusted_set)

		for node in range(0, 281904):
			trust_rank_t.append(0)
			trust_rank_t1.append(0)
			if node in trusted_set:
				trust_rank_t[node] = 1

		adjacency_list_outgoing = MatrixHandler.load_adjacency_list_outgoing()
		adjacency_list_incoming = MatrixHandler.load_adjacency_list_incoming()

		print("TrustRank for 10 iterations")
		while itr <= iteration:
			# run power method for 'iteration' times
			print("iteration: ", str(itr))
			print(trust_rank_t[1:1001])

			for page in range(1, 281904):
				trust_from_each_page = 0
				trust_rank_sum = 0
				for linked_page in adjacency_list_incoming[str(page)]:
					trust_from_each_page = trust_rank_t[linked_page]/len(adjacency_list_outgoing[str(linked_page)])
					trust_rank_sum = trust_rank_sum + beta*trust_from_each_page

				if page in trusted_set:
					trust_rank_t1[page] = trust_rank_sum + (1-beta)/len(trusted_set)
				else:
					trust_rank_t1[page] = trust_rank_sum

			trust_rank_t = trust_rank_t1
			itr = itr + 1

		print("Top 100 results")
		print(sorted(trust_rank_t, reverse=True)[1:100])
		
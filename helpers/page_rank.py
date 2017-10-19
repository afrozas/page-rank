from helpers.matrix_handler import MatrixHandler


class PageRank:
	"""
	Provides implementation of Google's PageRank algorithm
	- Make the graph stochastic, irreducible and aperiodic (Markov Chains)
	- PageRank Power Method
	- Teleportation (handling spider traps and sink pages)
	"""

	def follow_Markov_Chain():
		"""
		preprocessor function to make the graph stochastic, irreducible and aperiodic 
		"""
		pass


	def calculate_PageRank():
		"""
		provides PageRank core implementation
		"""
		N = 281903
		page_rank_t = []
		page_rank_t1 = []
		iteration = 10
		itr = 0
		beta = 0.85

		for node in range(0, N+1):
			if node == 0:
				page_rank_t.append(0)
			else:
				page_rank_t.append(1./N)
			page_rank_t1.append(0)

		#print(page_rank_t)

		adjacency_list_outgoing = MatrixHandler.load_adjacency_list_outgoing()
		adjacency_list_incoming = MatrixHandler.load_adjacency_list_incoming()

		# run power method for 'iteration' times
		while itr <= iteration:

			# uncomment for writing the results to file/console
			# print("iteration: ", str(itr))
			# print(page_rank_t[1:1001])

			for page in range(1, N+1):
				pr_from_each_page = 0
				page_rank_sum = 0
				for linked_page in adjacency_list_incoming[str(page)]:
					pr_from_each_page = page_rank_t[linked_page]/len(adjacency_list_outgoing[str(linked_page)])
					page_rank_sum = page_rank_sum + beta*pr_from_each_page
				page_rank_t1[page] = page_rank_sum

			# avoids any leakage of rank
			summation = round(sum(page_rank_t1),5)
			for page in range(1, N+1):
				page_rank_t1[page] += (1-summation)/N
			
			page_rank_t = page_rank_t1
			itr = itr + 1

		return page_rank_t


	def allow_Teleports():
		"""
		adds teleportation factor to the PageRank equation
		"""
		pass
		

	def get_top_page_ranks(self, n=100):
		"""
		@param n : top n page rank nodes to be returned
		:returns list of top n page ranks 
		"""
		page_ranks = self.calculate_PageRank()
		return sorted(range(len(page_ranks)), key=lambda k: page_ranks[k])[1:n]

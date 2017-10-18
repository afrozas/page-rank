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
		N = 281904
		page_rank_t = []
		page_rank_t1 = []
		iteration = 10
		itr = 0

		for node in range(0, 281904):
			page_rank_t.append(1/N)
			page_rank_t1.append(0)

		adjacency_list_outgoing = MatrixHandler.load_adjacency_list_outgoing()
		adjacency_list_incoming = MatrixHandler.load_adjacency_list_incoming()

		print("Page Rank for nodes numbered 1 through 10")
		while itr <= iteration:
			# run power method for 'iteration' times
			print("iteration: ", str(itr))
			print(page_rank_t[1:11])

			for page in range(1, 281904):
				pr_from_each_page = 0
				page_rank_sum = 0
				# if str(page) in adjacency_list_incoming:
				for linked_page in adjacency_list_incoming[str(page)]:
					#if str(linked_page) in adjacency_list_outgoing and linked_page in page_rank_t:
					pr_from_each_page = page_rank_t[linked_page]/len(adjacency_list_outgoing[str(linked_page)])
					# print("pr_from_each_page ", pr_from_each_page)
					page_rank_sum = page_rank_sum + pr_from_each_page
					# print(page_rank_sum)
				# print("page_rank for page ", str(page), " is ", str(page_rank_sum))
				page_rank_t1[page] = page_rank_sum

			page_rank_t = page_rank_t1
			itr = itr + 1


	def allow_Teleports():
		"""
		adds teleportation factor to the PageRank equation
		"""
		pass
		
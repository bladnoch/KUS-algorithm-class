""" Given a chain of n matrices, fully parenthesize the product
in a way that minimizes the number of scalar multiplications. 
"""

import numpy as np
import time
from print_table import print_table

def matrix_chain_order(p, n):
	"""Determine the optimal number of scalar multiplications needed
	to compute the matrix chain product A[1] * A[2] * ... * A[n].

	Arguments: 
	p -- list of dimensions of matrices in which matrix i has dimensions p[i - 1] x p[i]
	n -- p has entries indexed 0 to n

	Returns:
	m -- array with m[i, j] as the lowest number of scalar multiplications
	to compute A(i..j). Entries used are m[1:n+1, 1:n+1].
	s -- array that records which position to split an optimal solution 
	to a subproblem of m[i, j]. Entries used are s[1:n, 2:n+1].
	"""
	m = np.zeros(shape=[n+1, n+1])           # using indices 1:n+1, 1:n+1
	s = np.zeros(shape=[n, n+1], dtype=int)  # using indices 1:n, 2:n+1

    ### ...TO BE COMPLETED ... ###
	### ...WRITE YOUR CODE ... ###
	return m, s


def print_optimal_parens(s, i, j):
	"""Print an optimal parenthesization of the matrix chain from A[i] to A[j].

	Assumption:
	Matrix A[i] has dimensions p[i-1] x p[i]
	"""
	if i == j:
		print("A[" + str(i), end = "]")
	else:
		print("(", end = "")
		print_optimal_parens(s, i, s[i, j])      # left side
		print_optimal_parens(s, s[i, j] + 1, j)  # right side
		print(")", end = "")


def recursive_matrix_chain(p, i, j):
	"""Determine recursively optimal number of scalar multiplications
	needed to compute the matrix chain product from A[i] to A[j].

	Arguments: 
	p -- array of dimensions of matrices in which matrix i has dimensions p[i - 1] x p[i]
	i -- index of the beginning matrix in the matrix subchain
	j -- index of the end matrix in the matrix subchain
	"""
	if i == j:
		return 0
	m[i, j] = float('inf')
	### ...TO BE COMPLETED ... ###
	### ...WRITE YOUR CODE ... ###
	return int(m[i, j])


def memoized_matrix_chain(p, n):
	"""Determine recursively optimal number of scalar multiplications
	needed to compute the matrix chain product for whole chain, using memoization.

	Arguments:
	p -- array of dimensions of matrices in which matrix i has dimensions p[i - 1] x p[i]
	n -- p has entries indexed 0 to n
	"""
	m = np.empty(shape=[n + 1, n + 1])
	m.fill(float('inf'))  # fill array elements with infinity
	return lookup_chain(m, p, 1, n)


def lookup_chain(m, p, i, j):
	"""Look up value for m[i, j] if it is already computed.  If not, compute the value and store it.

	Arguments: 
	m -- array with m[i, j] as the lowest number of scalar multiplications
	to compute A(i..j). Entries used are m[1:n+1, 1:n+1].
	p -- array of dimensions of matrices in which matrix i has dimensions p[i - 1] x p[i]
	i -- index of the beginning matrix in the matrix subchain
	j -- index of the end matrix in the matrix subchain
	"""
	if m[i, j] < float('inf'):
		return m[i, j]  # return previously computed m[i, j]
	if i == j:
		m[i, j] = 0
	else:
		### ...TO BE COMPLETED ... ###
		pass
		### ...WRITE YOUR CODE ... ###
	return int(m[i, j])


def print_m(m, n):
	"""Format and print m table.

	Arguments:
	m -- array with m[i, j] as the lowest number of scalar multiplications
	to compute A(i:j). Entries used are m[1:n+1, 1:n+1].
	n -- size of m
	"""
	print_table(m, 1, n, 1, n, int)


def print_s(s, n):
	"""Print the values of s that are used.

	Arguments:
	s -- array that records which position to split an optimal solution 
	to a subproblem of m[i, j]. Entries used are s[1:n, 2:n+1].
	n -- size of s
	"""
	print_table(s, 1, n-1, 2, n, int)


# Testing
if __name__ == "__main__":

	# Matrix chain multiply example from textbook.
	p = [30, 35, 15, 5, 10, 20, 25]
	n = len(p)-1
	m, s = matrix_chain_order(p, n)
	print_optimal_parens(s, 1, n)  # should print ((A[1](A[2]A[3]))((A[4]A[5])A[6]))
	print()
	print_m(m, n)
	print_s(s, n)
	print(int(m[1, n]))

	# Recursive. 
	m = np.zeros(shape=[n + 1, n + 1])
	print(recursive_matrix_chain(p, 1, n))

	# Memoized. Same answer.
	m = np.zeros(shape=[n + 1, n + 1])
	print(memoized_matrix_chain(p, n))

	# Random example.
	n = 15
	p = np.random.randint(2, 100, size=n+1)
	m, s = matrix_chain_order(p, n)
	print_optimal_parens(s, 1, n)
	print()
	print_m(m, n)
	print_s(s, n)
	print(int(m[1, n]))

	# Recursive.
	m = np.zeros(shape=[n + 1, n + 1])
	print(recursive_matrix_chain(p, 1, n))

	# Memoized. Same answer.
	print(memoized_matrix_chain(p, n))

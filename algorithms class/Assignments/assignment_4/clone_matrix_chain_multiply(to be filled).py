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
    m = np.zeros(shape=[n + 1, n + 1])  # using indices 1:n+1, 1:n+1
    s = np.zeros(shape=[n, n + 1], dtype=int)  # using indices 1:n, 2:n+1

    ### ...TO BE COMPLETED ... ##############################################################################............1

    for chain_length in range(2, n + 1):  # chain_length = len(matrix chain)
        for i in range(1, n - chain_length + 2):  # i = starting matrix of the subchain
            j = i + chain_length - 1  # j = ending matrix of the subchain
            m[i, j] = float('inf')
            for k in range(i, j):  # k = splitting point of the subchain
                # Compute cost
                cost = m[i, k] + m[k + 1, j] + p[i - 1] * p[k] * p[j]
                if cost < m[i, j]:  # 더 적은걸 찾으면 Update m and s
                    m[i, j] = cost
                    s[i, j] = k

    ### ...WRITE YOUR CODE ... ###
    return m, s


def print_optimal_parens(s, i, j):
    """Print an optimal parenthesization of the matrix chain from A[i] to A[j].

	Assumption:
	Matrix A[i] has dimensions p[i-1] x p[i]
	"""
    if i == j:
        print("A[" + str(i), end="]")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i, j])  # left side
        print_optimal_parens(s, s[i, j] + 1, j)  # right side
        print(")", end="")


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
    ### ...TO BE COMPLETED ... ##############################################################################............2
    # Compute the minimum cost for all possible splits of the chain
    for k in range(i, j):
        # cost를 구하기 위해 recursive 하게 호출
        cost = (recursive_matrix_chain(p, i, k) +
                recursive_matrix_chain(p, k + 1, j) +
                p[i - 1] * p[k] * p[j])

        # 더 적은걸 찾으면 Update
        if cost < m[i, j]:
            m[i, j] = cost

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
        ### ...TO BE COMPLETED ... ##############################################################################........3

        # calls lookup_chain to compute subchain's minimum cost
        for k in range(i, j):
            # lookup minimum cost
            cost = lookup_chain(m, p, i, k) + lookup_chain(m, p, k + 1, j) + p[i - 1] * p[k] * p[j]
            if cost < m[i, j]:
                m[i, j] = cost

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
    print_table(s, 1, n - 1, 2, n, int)


# Testing
if __name__ == "__main__":
    # Matrix chain multiply example from textbook.
    p = [30, 35, 15, 5, 10, 20, 25]
    n = len(p) - 1
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
    p = np.random.randint(2, 100, size=n + 1)
    m, s = matrix_chain_order(p, n)
    print_optimal_parens(s, 1, n)
    print()
    print_m(m, n)
    print_s(s, n)

    # Q4 bottom-up
    start_time = time.time()  # Start timer
    m, s = matrix_chain_order(p, n)
    bottom_up_time = time.time() - start_time  # Calculate elapsed time
    print(int(m[1, n]))
    print("Bottom-Up:", bottom_up_time)
    print()

    # Recursive.
    m = np.zeros(shape=[n + 1, n + 1])
    # Q4 recursive
    start_time = time.time()  # Start timer
    min_multiplications_recursive = recursive_matrix_chain(p, 1, n)
    recursive_time = time.time() - start_time  # Calculate elapsed time
    print(recursive_matrix_chain(p, 1, n))
    print("Recursive:", recursive_time)
    print()

    # Memoized. Same answer.
    # Q4 memoized
    start_time = time.time()  # Start timer
    min_multiplications_memoized = memoized_matrix_chain(p, n)
    memoized_time = time.time() - start_time  # Calculate elapsed time
    print(memoized_matrix_chain(p, n))
    print("Memoized:", memoized_time)
    print()

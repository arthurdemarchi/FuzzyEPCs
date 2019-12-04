import numpy

class Relations:
	def __init__(self, constructor_type = 'random', nlines=None, ncols=None, list_matrix=None, matrix=None):

		self.constructor_type = constructor_type

		if self.constructor_type == 'random':
			self.nlines = nlines
			self.ncols = ncols
			numbers = numpy.random.uniform(0, 1, ncols*nlines)
			self.matrix = numpy.zeros((nlines, ncols))

			for x in range (0, nlines):
				for y in range (0, ncols):
					self.matrix[x][y] = round(numbers[x*ncols+y],  2)

		if self.constructor_type == 'list_matrix':
			self.nlines = len(list_matrix[0])
			self.ncols = len(list_matrix)
			self.matrix = numpy.array([numpy.array(element) for element in list_matrix])

		if self.constructor_type == 'matrix':
			self.nlines = matrix.shape[0]
			self.ncols = matrix.shape[1]
			self.matrix = matrix

	def print(self):
		print("[", end='')
		for line in range(0, self.nlines):
			for col in range(0, self.ncols):
				print(self.matrix[line][col], end=' ')
			if not line == self.nlines - 1:
				print('\n', end='')
		print("] \n")
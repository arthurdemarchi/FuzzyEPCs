import numpy
from ..MyLibs.relations import Relations
class RelationOperator():

	def __init__(self):
		pass

	def __close__(self):
		pass

	def max_min(self, relation_1, relation_2):
		if not relation_1.ncols == relation_2.nlines:
			print('Error: Relations must have compatible size')
			return False
		else:
			ncomum = relation_1.ncols

		result = numpy.zeros((relation_1.nlines, relation_2.ncols))
		for x in range(0, relation_1.nlines):
			for y in range(0, relation_2.ncols):
				for comum in range (0, ncomum):
					result[x][y] = max(min(relation_1.matrix[x][comum], relation_2.matrix[comum][y]), result[x][y])

		return Relations('matrix', matrix=result)

	def max_prod(self, relation_1, relation_2):
		if not relation_1.ncols == relation_2.nlines:
			print('Error: Relations must have compatible size')
			return False
		else:
			ncomum = relation_1.ncols

		result = numpy.zeros((relation_1.nlines, relation_2.ncols))
		for x in range(0, relation_1.nlines):
			for y in range(0, relation_2.ncols):
				for comum in range (0, ncomum):
					result[x][y] = round(max((relation_1.matrix[x][comum]*relation_2.matrix[comum][y]), result[x][y]), 2)

		return Relations('matrix', matrix=result)

	def max_media(self, relation_1, relation_2):
		if not relation_1.ncols == relation_2.nlines:
			print('Error: Relations must have compatible size')
			return False
		else:
			ncomum = relation_1.ncols

		result = numpy.zeros((relation_1.nlines, relation_2.ncols))
		for x in range(0, relation_1.nlines):
			for y in range(0, relation_2.ncols):
				for comum in range (0, ncomum):
					result[x][y] = round(max(0.5*(relation_1.matrix[x][comum]+relation_2.matrix[comum][y]), result[x][y]), 2)
		return Relations('matrix', matrix=result)
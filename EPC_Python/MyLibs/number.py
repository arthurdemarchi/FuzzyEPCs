from region import Region
from operators import  Operators

class Number:
	def __init__(self, npoints, universe_size, region_min, region_max, number):
		self.number = Region(name='number_'+str(number), npoints=npoints, universe_size=universe_size, region_min=region_min, region_max=region_max, region_type='triangular')

	def add(self, number):
		new_min_region = self.number.region_min + number.number.region_min
		new_max_region = self.number.region_max + number.number.region_max
		new_number = (new_min_region + new_max_region)/2
		return Number(npoints = self.number.npoints, universe_size = self.number.universe_size, region_min = new_min_region, region_max=new_max_region, number=new_number)

	def subtract(self, number):
		new_min_region = self.number.region_min - number.number.region_max
		new_max_region = self.number.region_max - number.number.region_min
		new_number = (new_min_region + new_max_region)/2
		return Number(npoints = self.number.npoints, universe_size = self.number.universe_size, region_min = new_min_region, region_max=new_max_region, number=new_number)

	def product(self, number):
		new_min_region = self.number.region_min*number.number.region_min
		new_max_region = self.number.region_max*number.number.region_max
		new_number = (new_min_region + new_max_region)/2
		return Number(npoints = self.number.npoints, universe_size = self.number.universe_size, region_min = new_min_region, region_max=new_max_region, number=new_number)

	def division(self, number):
		new_min_region = self.number.region_min/number.number.region_max
		new_max_region = self.number.region_max/number.number.region_min
		new_number = (new_min_region + new_max_region)/2
		return Number(npoints = self.number.npoints, universe_size = self.number.universe_size, region_min = new_min_region, region_max=new_max_region, number=new_number)

	def min(self, number):
		operator = Operators()
		new_region = operator.union(self.number, number.number)
		return new_region

	def max(self, number):
		operator = Operators()
		new_region = operator.intersection(self.number, number.number)
		return new_region
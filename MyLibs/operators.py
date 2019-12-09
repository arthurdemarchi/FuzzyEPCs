from copy import deepcopy
from .region import Region
from .utils import plot

class Operators:
	def __inti__(self):
		pass

	def __close__(self):
		pass

	def union(self, regions, union_type='max'):
		if not self.__check_universe(regions):
			return False

		result = Region(name='Região União', npoints=regions[0].npoints, universe_init=regions[0].universe_init, universe_size=regions[0].universe_size, region_min=regions[0].universe_init, region_max=0, region_type='blank')
		for region in regions:
			for i, item in enumerate(region.fuzzy):
				if union_type == 'algebric_sum':
					result.fuzzy[i]['u'] = item['u'] + result.fuzzy[i]['u'] - item['u']*result.fuzzy[i]['u']
				else:
					result.fuzzy[i]['u'] = max(item['u'], result.fuzzy[i]['u'])
		result.update()
		result.region_type = 'union'
		return result

	def intersection(self, regions, intersection_type='min'):
		if not self.__check_universe(regions):
			return False

		result = Region(name='Região União', npoints=regions[0].npoints, universe_init=regions[0].universe_init, universe_size=regions[0].universe_size, region_min=regions[0].universe_init, region_max=0, region_type='blank_filled')
		for region in regions:
			for i, item in enumerate(region.fuzzy):
				if intersection_type == 'algebric_product':
					result.fuzzy[i]['u'] = item['u']*result.fuzzy[i]['u']
				else:
					result.fuzzy[i]['u'] = min(item['u'], result.fuzzy[i]['u'])

		result.update()
		result.region_type = 'intersection'
		return result

	def complement(self, regions):
		regions_complement = regions
		if type(regions) is list:
			for region in regions_complement:
				for item in region.fuzzy:
					item['u'] = 1 - item['u']
		else:
			for item in regions_complement.fuzzy:
					item['u'] = 1 - item['u']

		return regions_complement


	def is_active(self, regions, x):
		if not self.__check_universe(regions):
			return None

		result = []
		if type(regions) is Region:
			if regions.is_active(x):
				result.append(regions)

		if type(regions) is list:
			for region in regions:
				if region.is_active(x):
					result.append(region)

		return result


	def get_alfa_cut(self, region, alfa):
		alfa_cut = region.get_alfa_cut(alfa)
		alfa_cut_region = Region(region.name+'_'+str(alfa), region.npoints, region.universe_size, region.region_min, region.region_min, region_type='alfa_cut', alfa_cut_fuzzy=alfa_cut)
		return alfa_cut_region

	def get_output(self, in_regions, x, rule_function, function_inputs=1, implication='mandani', agregation='max'):
		if function_inputs == 1:
			active_in_regions = self.is_active(in_regions, x)
			output_regions = []
			for active_region in active_in_regions:
				treshold = active_region.get_u(x)
				output_region = deepcopy(rule_function(active_region))
				if implication == 'mandani':
					output_region.mandani(treshold)
				elif implication == 'zadeh':
					output_region.zadeh(treshold)
				elif implication == 'larsen':
					output_region.larsen(treshold)
				output_regions.append(output_region)
			if agregation == 'max':
				final_output = self.union(output_regions)
			if agregation == 'no_agregation':
				final_output = output_regions

		elif function_inputs == 2:
			#Encontrando todas as regiões ativas nos dois inputs
			active_in_regions_a = self.is_active(in_regions[0], x[0])
			active_in_regions_b = self.is_active(in_regions[1], x[1])
			#criando lista de saida
			output_regions = []
			#Para cada combinação Possível de Entradas Ativas dos Inputs
			for active_in_a in active_in_regions_a:
				for active_in_b in active_in_regions_b:
					#encontra o treshold baseado na regra do min (E)
					treshold = min(active_in_a.get_u(x[0]), active_in_b.get_u(x[1]))
					#econtra região de saída a partir do set de regras
					output_region = deepcopy(rule_function(active_in_a, active_in_b))
					#Aplica função de implicação na região encontrada com o treshold definido
					if implication == 'mandani':
						output_region.mandani(treshold)
					elif implication == 'zadeh':
						output_region.zadeh(treshold)
					elif implication == 'larsen':
						output_region.larsen(treshold)
					#Adiciona a região de saída contabilizada à lista de regiões de saída ativas
					output_regions.append(output_region)
			if agregation == 'max':
				final_output = self.union(output_regions)
			if agregation == 'no_agregation':
				final_output = output_regions

		return final_output

	def defuzzyficate(self, out_region, defuzzy_rule='cda'):
		if defuzzy_rule == 'cda':
			return out_region.cda()
		if defuzzy_rule == 'mdm':
			return out_region.mdm()
		if defuzzy_rule == 'mpm':
			return out_region.mpm()

	def classificate(self, classes, universe_init, universe_size, output):
		#normalizando
		normalized_output = (output-universe_init)/universe_size
		pertinence = 0
		for each_class in classes:
			u = each_class.get_u(normalized_output)
			if u >= pertinence:
				if u == pertinence:
					result = None
				else:
					pertinence = u
					result = each_class
		return result

	def __check_universe(self, regions):
		universe_size = regions[0].universe_size
		npoints = regions[0].npoints
		universe_init = regions[0].universe_init
		for region in regions:
			if not region.universe_size == universe_size:
				print('Error: Fuzzy regions are not in the same universe!')
				return False
			if not region.npoints == npoints:
				print('Error: Fuzzy regions are not equaly discretized!')
			if not region.universe_init == universe_init:
				print('Error: Fuzzy regions do no have the same universe!')
		return True

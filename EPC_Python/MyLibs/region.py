"""
EXercício: TODOS
Aluno: Arthur Denarchi
nUSP: 7992894

"Biblioteca" desenvolvida pelo aluno com objetivo de ser utilizada nos EPCs da Matéria Fuzzy
o desenvolvimento deste arquivo tem como objetivo colocar sob a óptica da programação orientada
objetos as regiões Fuzzy de um sistema.

Para seu funcionamento é necessário determinar o tamanho do universo, parte-se do pressusposto
de universos que se iniciam em zero, tipo de região Fuzzy, sua descritização e alguns
pontos de interesse da função (dependendo do tipo de função).
"""


import math
class Region:
	def __init__(self, name, npoints, universe_size, region_min, region_max, region_type, trap_init=None, trap_end=None, alfa_cut_fuzzy=None, universe_init=0):
		"""Constructor

		Arguments:
			npoints {integer} -- Número de pontos na discretização da região fuzzy
			universe_size {integer} -- Tamanho máximo do universo, considera-se que todo universo se inicia em 0(zero)
			region_min {float} -- Ponto de intersecção inicial entre a região e a absissa
			region_max {float} -- Ponto de intersecção final entre a região e a absissa
			region_type {string} -- Tipo da Região

		Keyword Arguments:
			trap_init {float} -- Ponto inicial do teto do trapézio (default: {None})
			trap_end {float} -- Ponto final do teto do trapézio (default: {None})
		"""

		self.name = name
		self.npoints = npoints
		self.universe_size = universe_size
		self.universe_init = universe_init
		self.fuzzy = []
		self.region_min = region_min
		self.region_max = region_max
		self.region_type = region_type
		self.region_size = region_max - region_min
		self.region_center = self.region_min + self.region_size/2

		if self.region_type == 'trapezoid':
			self.trap_init = trap_init
			self.trap_end = trap_end

		if self.region_type == 'blank':
			for x in range (0, self.npoints):
				x = self.__get_x(x)
				u = 0
				region_item = {'x': x, 'u': u}
				self.fuzzy.append(region_item)

		elif self.region_type == 'blank_filled':
			for x in range (0, self.npoints):
				x = self.__get_x(x)
				u = 1
				region_item = {'x': x, 'u': u}
				self.fuzzy.append(region_item)

		elif self.region_type == 'alfa_cut':
			for x in range(0, self.npoints):
				x = self.__get_x(x)
				for item in alfa_cut_fuzzy:
					if x == item['x']:
						u = item['u']
						region_item = {'x': x, 'u': u}
						self.fuzzy.append(region_item)
				u = 0
				region_item = {'x': x, 'u': u}
				self.fuzzy.append(region_item)
			self.update()

		else:
			for x in range (0, self.npoints):
				x = self.__get_x(x)
				u = self.__get_u(x)
				region_item = {'x': x, 'u': u}
				self.fuzzy.append(region_item)

		self.update_active()

	def __close__(self):
		"""Destructor
		"""
		self.npoints = None
		self.universe_size = None
		self.fuzzy = None
		self.region_min = None
		self.region_max = None
		self.region_type = None
		self.region_size = None
		self.region_center = None

		if self.region_type == 'trapezoid':
			self.trap_init = None
			self.trap_end = None

	def __get_x(self, x):
		"""get_x - Função para o construtor - Acha um elemento do universo discretizado

		Arguments:
			x {integer} -- Índice entre 0 e npoints

		Returns:
			float -- elemento do universo relativo ao índice de discretização de entrada

		"""
		return round((x/self.npoints)*self.universe_size, int(math.log(self.npoints, 10)+1))+self.universe_init

	def __get_u(self, x):
		"""get_u  - Função para o construtor - acha o grau de pertinência de um elemento do universo

		Arguments:
			x {float} -- elemento do universo da região fuzzy

		Returns:
			float -- pertinencia do elemento de entrada na região fuzzy
		"""
		if x < self.region_min or x > self.region_max:
			return 0

		if self.region_type == 'trapezoid':
			if self.trap_init == None or self.trap_end == None:
				print('Error: please specify trapezoid characteristics.')
			if x <= self.trap_init and self.trap_init != self.region_min:
				delta_y = 1
				delta_x = self.trap_init - self.region_min
				slope = delta_y/delta_x
				u = slope*(x-self.region_min)
			if x >= self.trap_init <= self.trap_end:
				u = 1
			if x > self.trap_end:
				delta_y = -1
				delta_x = self.region_max - self.trap_end
				slope = delta_y/delta_x
				u = 1 + slope*(x-self.trap_end)

		if self.region_type == 'triangular':
			if x <= self.region_center:
				delta_y = 1
				delta_x = self.region_center - self.region_min
				slope = delta_y/delta_x
				u = slope*(x-self.region_min)
			if x > self.region_center:
				delta_y = -1
				delta_x = self.region_max - self.region_center
				slope = delta_y/delta_x
				u = 1+slope*(x-self.region_center)
		return u

	def get_u(self, x):
		"""get_u - Funçao para o usuário encontrar pertinência de um elemento qualquer

		Arguments:
			x {float} -- elemento do universo da região fuzzy

		Returns:
			float -- grau de pertinencia do elemento escolhido do universo
		"""
		for i, item in enumerate(self.fuzzy):
			if x == item['x']:
				return item['u']
			if x < item['x']:
				return self.fuzzy[i-1]['u']

	def update_active(self):
		active = []
		for item in self.fuzzy:
			if self.get_u(item['x']) > 0:
				active.append(item)
		self.active = active


	def is_active(self, x):
		for i, item in enumerate(self.fuzzy):
			if x == item['x']:
				if item['u'] > 0:
					return True
				else:
					return False
			if x < item['x']:
				if self.fuzzy[i-1]['u'] > 0:
					return True
				else:
					return False
		return False

	def get_alfa_cut(self, alfa):
		alfa_cut = []
		for item in self.fuzzy:
			if item['u'] >= alfa:
				alfa_cut.append(item)
		return alfa_cut

	def mandani(self, treshold):
		for item in self.fuzzy:
			item['u'] = min(item['u'], treshold)
		self.update()

	def zadeh(self, treshold):
		for item in self.fuzzy:
			item['u'] = max(1-treshold, min(item['u'], treshold))
		self.update()

	def larsen(self, treshold):
		for item in self.fuzzy:
			item['u'] = item['u']*treshold
		self.update()

	def cda(self):
		u_times_x = 0
		u = 0
		for item in self.fuzzy:
			u_times_x = u_times_x + item['u']*item['x']
			u = u + item['u']
		return round(u_times_x/u, 2)

	def mdm(self):
		max_u = 0
		for item in self.fuzzy:
			max_u = max(item['u'], max_u)

		sum_x = 0
		number_of_x = 0
		for item in self.fuzzy:
			if item['u'] == max_u:
				sum_x = sum_x + item['x']
				number_of_x = number_of_x + 1

		return round(sum_x/number_of_x, 2)

	def mpm(self):
		max_u = 0
		for item in self.fuzzy:
			max_u = max(item['u'], max_u)

		for item in self.fuzzy:
			if item['u'] == max_u:
				return round(item['x'], 2)

	def update(self):
		"""update
			Função que atualiza alguns atributos da região, deve ser utilizada após alterar-se diretamente os elementos
			do atributo fuzzy.
		"""
		for item in self.fuzzy:
			if item['u'] == 0:
				self.region_min = item['x']
			else:
				break

		for item in reversed(self.fuzzy):
			if item['u'] == 0:
				self.region_max = item['x']
			else:
				break

		self.region_size = self.region_max - self.region_min
		self.region_center = self.region_min + self.region_size/2
		self.update_active()
import matplotlib.pyplot as plt
from math import sqrt, ceil
from .region import Region

def plot(region, title, x_label='X', y_label='u(x)', write=False, file='figura.png'):
		if type(region) == Region:
			x = []
			y = []
			delta_x = region.universe_init
			for item in region.fuzzy:
				x.append(item['x'])
				y.append(item['u'])
			plt.scatter(x, y, s=0.1, alpha=1)

		if type(region) == list:
			delta_x = region[0].universe_init
			for each_region in region:
				x = []
				y = []
				for item in each_region.fuzzy:
					x.append(item['x'])
					y.append(item['u'])
				plt.scatter(x, y, s=0.1, alpha=1)

		plt.title(title)
		plt.xlabel(x_label)
		plt.ylabel(y_label)
		plt.xlim(left=delta_x)
		plt.ylim(bottom=0)

		if write:
			plt.savefig(file)
			plt.close()

		else:
			plt.show(block=False)
			plt.pause(1)
			plt.close()

def subplot(sets_of_regions, titles, write=False, file='figura.png'):
	number_of_plots = len(sets_of_regions)
	number_of_titles = len(titles)
	frame = ceil(sqrt(number_of_plots))

	if not number_of_plots == number_of_titles:
		print('Error: in subplot number of titles must be the number of sets of regions.')
		return False

	for i, regions in enumerate(sets_of_regions):
		plt.subplot(frame, frame, i+1)
		if type(regions) == Region:
			x = []
			y = []
			delta_x = regions.universe_init
			for item in regions.fuzzy:
				x.append(item['x'])
				y.append(item['u'])
			plt.scatter(x, y, s=0.1, alpha=1)

		if type(regions) == list:
			delta_x = regions[0].universe_init
			for each_region in regions:
				x = []
				y = []
				for item in each_region.fuzzy:
					x.append(item['x'])
					y.append(item['u'])
				plt.scatter(x, y, s=0.1, alpha=1)

		plt.title(titles[i])
		plt.xlim(left=delta_x)
		plt.ylim(bottom=0, top = 1.1)
		plt.xlabel('x')
		plt.ylabel('u(x)')
		plt.tight_layout()

	if write:
		plt.savefig(file)
		plt.close()
	else:
		plt.show(block=False)
		plt.pause(5)
		plt.close()

# def plot_individual(regions, title, write=False, file='figura.png'):
# 		if type(regions) == Region:
# 			plot(regions, title, write=write, file=file)

# 		number_of_plots = len(regions)
# 		frame = ceil(sqrt(number_of_plots))

# 		if type(regions) == list:
# 			for each_region in region:
# 				x = []
# 				y = []
# 				for item in each_region.fuzzy:
# 					x.append(item['x'])
# 					y.append(item['u'])
# 				plt.scatter(x, y, s=0.1, alpha=1)

# 		plt.title(title)
# 		plt.xlabel(x_label)
# 		plt.ylabel(y_label)
# 		plt.xlim(left=0)
# 		plt.ylim(bottom=0)

# 		if write:
# 			plt.savefig(file)
# 			plt.close()

# 		else:
# 			plt.show(block=False)
# 			plt.pause(5)
# 			plt.close()

def print_names(regions):
	for region in regions:
		print(region.name, end=', ')
"""
EXercício: EPC3
Aluno: Arthur Denarchi
nUSP: 7992894
"""

"""
AVISO: TODOS OS IMPORTS SÃO DE ''BILBIOTECAS'' IMPLEMENTADAS PELO PŔOPRIO ALUNO
ESTÃO EM OUTROS ARQUIVOS APENAS POR ORGANIZAÇÃO E REUTILIZAÇÃO DE SOFTWARE.
BIBLIOTECAS JUNTOS EM ANEXO PARA CORREÇÃO.
"""

from ..MyLibs.region import Region
from ..MyLibs.operators import Operators
from ..MyLibs.utils import plot, subplot, print_names

""" ####################################################################################################

0. Considere a função de pertinência abaixa a qual está descrevendo 5 conjuntos fuzzy que representam a
temperatura de um processo industrial.

""" ####################################################################################################

#Temperatura
temperatura_muito_baixa = Region(name='Ta', npoints=1000, universe_size=50, region_min=0, region_max=15, region_type='trapezoid', trap_init=0, trap_end=5)
temperatura_baixa = Region(name='Tb', npoints=1000, universe_size=50,  region_min=5, region_max=25, region_type='triangular')
temperatura_media = Region(name='Tc', npoints=1000, universe_size=50, region_min=15, region_max=35, region_type='triangular')
temperatura_alta = Region(name='Td', npoints=1000, universe_size=50, region_min=25, region_max=45, region_type='triangular')
temperatura_muito_alta = Region(name='Te', npoints=1000, universe_size=50, region_min=35, region_max=50, region_type='trapezoid', trap_init=45, trap_end=50)
temperatura = [temperatura_muito_baixa, temperatura_baixa, temperatura_media, temperatura_alta, temperatura_muito_alta]

#Pressão
pressao_muito_pequena = Region(name='Pa', npoints=1000, universe_size=10, region_min=0, region_max=3, region_type='trapezoid', trap_init=0, trap_end=1)
pressao_pequena = Region(name='Pb', npoints=1000, universe_size=10,  region_min=1, region_max=5, region_type='triangular')
pressao_media = Region(name='Pc', npoints=1000, universe_size=10, region_min=3, region_max=7, region_type='triangular')
pressao_grande = Region(name='Pd', npoints=1000, universe_size=10, region_min=5, region_max=9, region_type='triangular')
pressao_muito_grande = Region(name='Pe', npoints=1000, universe_size=10, region_min=7, region_max=10, region_type='trapezoid', trap_init=9, trap_end=10)
pressao = [pressao_muito_pequena, pressao_pequena, pressao_media, pressao_grande, pressao_muito_grande]

def rules(region):
	if region == temperatura_muito_baixa:
		return pressao_media
	if region == temperatura_baixa:
		return pressao_muito_pequena
	if region == temperatura_media:
		return pressao_grande
	if region == temperatura_alta:
		return pressao_muito_grande
	if region == temperatura_muito_alta:
		return pressao_pequena

""" ####################################################################################################

1. Elabore os procedimentos computacionais necessários para obter as regiões fuzzy de saída a partir
de valores pontuais (singleton) de entrada.

""" ####################################################################################################

#Resposta: Na classe Operators() foi implementado o operador que da regfião fuzzy de saída baseando-se
#na demonstração geométrica de infererência min-max.
#em tal algorítimo encontra-se as regiões ativas, encontra-se o valore de pertinência para o singleton
#de talz regiões. Através de um mínimo entre a pertinência de cada região de entrada e a respectiva saída
#saída acionda por ela tem-se as partes da região fuzzy de saída, que são algomeradas por união.
operator = Operators()
output_regions = operator.get_output(temperatura, 33, rules)

""" ####################################################################################################

2. Considere os seguintes valores de temperatura que foram aquisitados em tempo real pelos instrumentos
de medição do processo, os quais saõ definidos por:

""" ####################################################################################################

Ta = 13.3
print('######### 2A ###########')
print('Regiões de Entrada Ativadas por Ta = ', Ta)
active_inputs = operator.is_active(temperatura, Ta)
print_names(active_inputs)
print('Portanto as regras Ativadas são:')
for active_input in active_inputs:
	print('Para a Ativação de ', active_input.name, 'Temos a Saída de ', rules(active_input).name)

Tb = 18.8
print('######### 2B ###########')
print('Regiões de Entrada Ativadas por Tb = ', Tb)
active_inputs = operator.is_active(temperatura, Tb)
print_names(active_inputs)
print('Portanto as regras Ativadas são:')
for active_input in active_inputs:
	print('Para a Ativação de ', active_input.name, 'Temos a Saída de ', rules(active_input).name)

Tc = 30.0
print('######### 2C ###########')
print('Regiões de Entrada Ativadas por Tc = ', Tc)
active_inputs = operator.is_active(temperatura, Tc)
print_names(active_inputs)
print('Portanto as regras Ativadas são:')
for active_input in active_inputs:
	print('Para a Ativação de ', active_input.name, 'Temos a Saída de ', rules(active_input).name)

Td = 42.3
print('######### 2D ###########')
print('Regiões de Entrada Ativadas por Td = ', Td)
active_inputs = operator.is_active(temperatura, Td)
print_names(active_inputs)
print('Portanto as regras Ativadas são:')
for active_input in active_inputs:
	print('Para a Ativação de ', active_input.name, 'Temos a Saída de ', rules(active_input).name)

Te = 47.0
print('######### 2E ###########')
print('Regiões de Entrada Ativadas por Te = ', Te)
active_inputs = operator.is_active(temperatura, Te)
print_names(active_inputs)
print('Portanto as regras Ativadas são:')
for active_input in active_inputs:
	print('Para a Ativação de ', active_input.name, 'Temos a Saída de ', rules(active_input).name)

""" ####################################################################################################

3. Determine e Imprima, pra cada um dos valores do item 2, as regiões fuzzy individuais de saída relativas
à aplicação de cada regra fuzzy ativada. Para os casos que possuir duas regras atiadas simultaneamente,
imprima então os dois gráficos uma ao lado do outro.

""" ####################################################################################################
#Definindo Regiões de Saída
output_regions_Ta = operator.get_output(temperatura, Ta, rules, implication='mandani', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Ta)+1)
for i in range(0, len(output_regions_Ta)):
	titles.append('Ta_'+str(i))
	to_plot[i] = (output_regions_Ta[i])
titles.append('Ta_Agreggation_Max')
to_plot[len(output_regions_Ta)] = operator.union(output_regions_Ta)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-3a.png')

#Definindo Regiões de Saída
output_regions_Tb = operator.get_output(temperatura, Tb, rules, implication='mandani', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Tb)+1)
for i in range(0, len(output_regions_Tb)):
	titles.append('Tb_'+str(i))
	to_plot[i] = (output_regions_Tb[i])
titles.append('Tb_Agreggation_Max')
to_plot[len(output_regions_Tb)] = operator.union(output_regions_Tb)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-3b.png')

#Definindo Regiões de Saída
output_regions_Tc = operator.get_output(temperatura, Tc, rules, implication='mandani', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Tc)+1)
for i in range(0, len(output_regions_Tc)):
	titles.append('Tc_'+str(i))
	to_plot[i] = (output_regions_Tc[i])
titles.append('Tc_Agreggation_Max')
to_plot[len(output_regions_Tc)] = operator.union(output_regions_Tc)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-3c.png')

#Definindo Regiões de Saída
output_regions_Td = operator.get_output(temperatura, Td, rules, implication='mandani', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Td)+1)
for i in range(0, len(output_regions_Td)):
	titles.append('Td_'+str(i))
	to_plot[i] = (output_regions_Td[i])
titles.append('Td_Agreggation_Max')
to_plot[len(output_regions_Td)] = operator.union(output_regions_Td)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-3d.png')

#Definindo Regiões de Saída
output_regions_Te = operator.get_output(temperatura, Te, rules, implication='mandani', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Te)+1)
for i in range(0, len(output_regions_Te)):
	titles.append('Te_'+str(i))
	to_plot[i] = (output_regions_Te[i])
titles.append('Te_Agreggation_Max')
to_plot[len(output_regions_Te)] = operator.union(output_regions_Te)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-3e.png')


""" ####################################################################################################

4. Refaça o Exercício 3 Considerando como Zadeh o processo de implicação

""" ####################################################################################################
#Resposta: Código idêntico trocando o argumento implication de 'mandani' para 'zandeh'

#Definindo Regiões de Saída
output_regions_Ta = operator.get_output(temperatura, Ta, rules, implication='zadeh', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Ta)+1)
for i in range(0, len(output_regions_Ta)):
	titles.append('Ta_'+str(i))
	to_plot[i] = (output_regions_Ta[i])
titles.append('Ta_Agreggation_Max')
to_plot[len(output_regions_Ta)] = operator.union(output_regions_Ta)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-4a.png')

#Definindo Regiões de Saída
output_regions_Tb = operator.get_output(temperatura, Tb, rules, implication='zadeh', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Tb)+1)
for i in range(0, len(output_regions_Tb)):
	titles.append('Tb_'+str(i))
	to_plot[i] = (output_regions_Tb[i])
titles.append('Tb_Agreggation_Max')
to_plot[len(output_regions_Tb)] = operator.union(output_regions_Tb)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-4b.png')

#Definindo Regiões de Saída
output_regions_Tc = operator.get_output(temperatura, Tc, rules, implication='zadeh', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Tc)+1)
for i in range(0, len(output_regions_Tc)):
	titles.append('Tc_'+str(i))
	to_plot[i] = (output_regions_Tc[i])
titles.append('Tc_Agreggation_Max')
to_plot[len(output_regions_Tc)] = operator.union(output_regions_Tc)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-4c.png')

#Definindo Regiões de Saída
output_regions_Td = operator.get_output(temperatura, Td, rules, implication='zadeh', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Td)+1)
for i in range(0, len(output_regions_Td)):
	titles.append('Td_'+str(i))
	to_plot[i] = (output_regions_Td[i])
titles.append('Td_Agreggation_Max')
to_plot[len(output_regions_Td)] = operator.union(output_regions_Td)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-4d.png')

#Definindo Regiões de Saída
output_regions_Te = operator.get_output(temperatura, Te, rules, implication='zadeh', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Te)+1)
for i in range(0, len(output_regions_Te)):
	titles.append('Te_'+str(i))
	to_plot[i] = (output_regions_Te[i])
titles.append('Te_Agreggation_Max')
to_plot[len(output_regions_Te)] = operator.union(output_regions_Te)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-4e.png')

""" ####################################################################################################

5.  Refaça o Exercício 3 Considerando como LArsen o processo de implicação

""" ####################################################################################################

#Resposta: Código idêntico trocando o argumento implication de 'mandani' para 'larsen'


#Definindo Regiões de Saída
output_regions_Ta = operator.get_output(temperatura, Ta, rules, implication='larsen', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Ta)+1)
for i in range(0, len(output_regions_Ta)):
	titles.append('Ta_'+str(i))
	to_plot[i] = (output_regions_Ta[i])
titles.append('Ta_Agreggation_Max')
to_plot[len(output_regions_Ta)] = operator.union(output_regions_Ta)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-5a.png')

#Definindo Regiões de Saída
output_regions_Tb = operator.get_output(temperatura, Tb, rules, implication='larsen', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Tb)+1)
for i in range(0, len(output_regions_Tb)):
	titles.append('Tb_'+str(i))
	to_plot[i] = (output_regions_Tb[i])
titles.append('Tb_Agreggation_Max')
to_plot[len(output_regions_Tb)] = operator.union(output_regions_Tb)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-5b.png')

#Definindo Regiões de Saída
output_regions_Tc = operator.get_output(temperatura, Tc, rules, implication='larsen', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Tc)+1)
for i in range(0, len(output_regions_Tc)):
	titles.append('Tc_'+str(i))
	to_plot[i] = (output_regions_Tc[i])
titles.append('Tc_Agreggation_Max')
to_plot[len(output_regions_Tc)] = operator.union(output_regions_Tc)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-5c.png')

#Definindo Regiões de Saída
output_regions_Td = operator.get_output(temperatura, Td, rules, implication='larsen', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Td)+1)
for i in range(0, len(output_regions_Td)):
	titles.append('Td_'+str(i))
	to_plot[i] = (output_regions_Td[i])
titles.append('Td_Agreggation_Max')
to_plot[len(output_regions_Td)] = operator.union(output_regions_Td)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-5d.png')

#Definindo Regiões de Saída
output_regions_Te = operator.get_output(temperatura, Te, rules, implication='larsen', agregation='no_agregation')

#Sub Plot Individual
titles = []
to_plot = [0]*(len(output_regions_Te)+1)
for i in range(0, len(output_regions_Te)):
	titles.append('Te_'+str(i))
	to_plot[i] = (output_regions_Te[i])
titles.append('Te_Agreggation_Max')
to_plot[len(output_regions_Te)] = operator.union(output_regions_Te)
subplot(to_plot, titles, True, 'Fuzzy/EPC3/EPC3-5e.png')

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

0. A determinação da pressão interna de uma caldeira pode ser estimada em função de sua temperatura
interna e do volume de água no seu interior. O especialista envolvido com o processo forneceu alguns dados
que foram utilizados para o projeto de um sistema fuzzy para mapear o comportamento existente entre as 
suas entradas e a sua saída. Essas informações são as seguintes:

	Variáveis de Entrada:
		Temperatura: Varia de 800 a 1200 graus celcius
		Volume: Varia de 2m3 a 12m3 de água
	Variáveis de Saída:
		Pressão: Varia de 4atm a 12atm

Após Análise Inicial do Problema, o projetista propôs um sistema fuzzy para estimar a saída (pressão),
a partir das entradas (temperatura e volume), tendo como formato para as funções de pertinência
os seguinites padrões geométricos.

""" ####################################################################################################

temperatura_baixa = Region(name='Ta', npoints=500, universe_init=800, universe_size=400, region_min=800, region_max=1000, region_type='trapezoid', trap_init=800, trap_end=900)
temperatura_media = Region(name='Tb', npoints=500, universe_init=800, universe_size=400, region_min=900, region_max=1100, region_type='triangular')
temperatura_alta = Region(name='Tc', npoints=500, universe_init=800, universe_size=400, region_min=1000, region_max=1200, region_type='trapezoid', trap_init=1100, trap_end=1200)
temperatura = [temperatura_baixa, temperatura_media, temperatura_alta]

volume_pequeno = Region(name='Va', npoints=500, universe_init=2, universe_size=10, region_min=2, region_max=7, region_type='trapezoid', trap_init=2, trap_end=4.5)
volume_medio = Region(name='Vb', npoints=500, universe_init=2, universe_size=10, region_min=4.5, region_max=9.5, region_type='triangular')
volume_grande = Region(name='Vc', npoints=500, universe_init=2, universe_size=10, region_min=7, region_max=12, region_type='trapezoid', trap_init=9.5, trap_end=12)
volume = [volume_pequeno, volume_medio, volume_grande]

pressao_pequena = Region(name='Pa', npoints=500, universe_init=4, universe_size=8, region_min=4, region_max=8, region_type='trapezoid', trap_init=4, trap_end=5)
pressao_media = Region(name='Pb', npoints=500, universe_init=4, universe_size=8, region_min=6, region_max=10, region_type='triangular')
pressao_grande = Region(name='Pc', npoints=500, universe_init=4, universe_size=8, region_min=8, region_max=12, region_type='trapezoid', trap_init=11, trap_end=12)
pressao = [pressao_pequena, pressao_media, pressao_grande]

def rules(temperatura, volume):
	if temperatura == temperatura_baixa and volume == volume_pequeno:
		return pressao_pequena
	if temperatura == temperatura_media and volume == volume_pequeno:
		return pressao_pequena
	if temperatura == temperatura_alta and volume == volume_pequeno:
		return pressao_media
	if temperatura == temperatura_baixa and volume == volume_medio:
		return pressao_pequena
	if temperatura == temperatura_media and volume == volume_medio:
		return pressao_media
	if temperatura == temperatura_alta and volume == volume_medio:
		return pressao_grande
	if temperatura == temperatura_baixa and volume == volume_grande:
		return pressao_media
	if temperatura == temperatura_media and volume == volume_grande:
		return pressao_grande
	if temperatura == temperatura_alta and volume == volume_grande:
		return pressao_grande


""" ####################################################################################################

1. Elabore os procedimentos computacionais necessários para obter os valores de saída (defuzzificados) em
função das regiões fuzzy resultantes a partir das contribuições de todas as regras ativadas.

""" ####################################################################################################

#Resposta: Algoritimo que adquire saída fuzzy implementado na biblioteca , pelo aluno, através da lógica
#  de E(min), implicação genérica e agregação Max.
# Algoritimo de deffuzyficação implementado em biblioteca ,pelo aluno, através com lógica escholível entre
# centro de area, média dos máximos e primeiro máximo.

operator = Operators()
in_regions = [temperatura, volume]
x = [950, 10]
output_region = operator.get_output(in_regions=in_regions, x=x, rule_function=rules, function_inputs=2, implication='mandani', agregation='max')
deffuz_output = operator.defuzzyficate(output_region, 'cda')
print('Como exemplo do exercício 1 temos entradas temperatura ', x[0], 'e volume ', x[1], 'e saída ', deffuz_output)

""" ####################################################################################################

2. Considere os seguintes valores de temperatura e volume que foram aquisitados em tempo real pelos
instrumentos de medição do processo, os quais são definidos por:

""" ####################################################################################################

Ta = 965
Va = 11
print('EXERCÍCIO 2A')
print('Para as entradas de Temperatura: ', Ta, 'e Volume: ', Va, 'Teremos a regra de Saída Como funções ativadas:')
temp_active = operator.is_active(temperatura, Ta)
vol_active = operator.is_active(volume, Va)
print_names(temp_active)
print_names(vol_active)
print('')
print('O que faz com que ativemos as regiões:')
for temp in temp_active:
	for vol in vol_active:
		print(temp.name, 'E', vol.name, '->', rules(temp, vol).name)

Tb = 920
Vb = 7.6
print('EXERCÍCIO 2B')
print('Para as entradas de Temperatura: ', Tb, 'e Volume: ', Vb, 'Teremos a regra de Saída Como funções ativadas:')
temp_active = operator.is_active(temperatura, Tb)
vol_active = operator.is_active(volume, Vb)
print_names(temp_active)
print_names(vol_active)
print('')
print('O que faz com que ativemos as regiões:')
for temp in temp_active:
	for vol in vol_active:
		print(temp.name, 'E', vol.name, '->', rules(temp, vol).name)

Tc = 1050
Vc = 6.3
print('EXERCÍCIO 2C')
print('Para as entradas de Temperatura: ', Tc, 'e Volume: ', Vc, 'Teremos a regra de Saída Como funções ativadas:')
temp_active = operator.is_active(temperatura, Tc)
vol_active = operator.is_active(volume, Vc)
print_names(temp_active)
print_names(vol_active)
print('')
print('O que faz com que ativemos as regiões:')
for temp in temp_active:
	for vol in vol_active:
		print(temp.name, 'E', vol.name, '->', rules(temp, vol).name)


Td = 843
Vd = 8.6
print('EXERCÍCIO 2D')
print('Para as entradas de Temperatura: ', Td, 'e Volume: ', Vd, 'Teremos a regra de Saída Como funções ativadas:')
temp_active = operator.is_active(temperatura, Td)
vol_active = operator.is_active(volume, Vd)
print_names(temp_active)
print_names(vol_active)
print('')
print('O que faz com que ativemos as regiões:')
for temp in temp_active:
	for vol in vol_active:
		print(temp.name, 'E', vol.name, '->', rules(temp, vol).name)

Te = 1122
Ve = 5.2
print('EXERCÍCIO 2E')
print('Para as entradas de Temperatura: ', Te, 'e Volume: ', Ve, 'Teremos a regra de Saída Como funções ativadas:')
temp_active = operator.is_active(temperatura, Te)
vol_active = operator.is_active(volume, Ve)
print_names(temp_active)
print_names(vol_active)
print('')
print('O que faz com que ativemos as regiões:')
for temp in temp_active:
	for vol in vol_active:
		print(temp.name, 'E', vol.name, '->', rules(temp, vol).name)


""" ####################################################################################################

3. Determine e imprima, para cada um dos valores acima, a região fuzzy resultante da agregação de todas
as regras ativadas.

""" ####################################################################################################

output_region_a = operator.get_output(in_regions=in_regions, x=[Ta, Va], rule_function=rules, function_inputs=2, implication='mandani', agregation='max')
output_region_b = operator.get_output(in_regions=in_regions, x=[Tb, Vb], rule_function=rules, function_inputs=2, implication='mandani', agregation='max')
output_region_c = operator.get_output(in_regions=in_regions, x=[Tc, Vc], rule_function=rules, function_inputs=2, implication='mandani', agregation='max')
output_region_d = operator.get_output(in_regions=in_regions, x=[Td, Vd], rule_function=rules, function_inputs=2, implication='mandani', agregation='max')
output_region_e = operator.get_output(in_regions=in_regions, x=[Te, Ve], rule_function=rules, function_inputs=2, implication='mandani', agregation='max')
output_regions = [output_region_a, output_region_b, output_region_c, output_region_d, output_region_e]
titles = ['Input A','Input B', 'Input C', 'Input D', 'Input E']
subplot(output_regions, titles, True, 'Fuzzy/EPC4/EPC4-3.png')

""" ####################################################################################################

4. Baseado nos restultados do Exercício 3, determine então os valores retornados do processo de defuzzyficação
quando se aplica o método do "Centro de Área"

""" ####################################################################################################

method = 'cda'
deffuz_output = operator.defuzzyficate(output_region_a, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Ta, 'e volume ', Va, 'e saída ', deffuz_output)
deffuz_output = operator.defuzzyficate(output_region_b, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Tb, 'e volume ', Vb, 'e saída ', deffuz_output)
deffuz_output = operator.defuzzyficate(output_region_c, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Tc, 'e volume ', Vc, 'e saída ', deffuz_output)
deffuz_output = operator.defuzzyficate(output_region_d, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Td, 'e volume ', Vd, 'e saída ', deffuz_output)
deffuz_output = operator.defuzzyficate(output_region_e, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Te, 'e volume ', Ve, 'e saída ', deffuz_output)


""" ####################################################################################################

5. Baseado nos restultados do Exercício 3, determine então os valores retornados do processo de defuzzyficação
quando se aplica o método do "Média dos Máximos"

""" ####################################################################################################

method = 'mdm'
deffuz_output = operator.defuzzyficate(output_region_a, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Ta, 'e volume ', Va, 'e saída ', deffuz_output)
deffuz_output = operator.defuzzyficate(output_region_b, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Tb, 'e volume ', Vb, 'e saída ', deffuz_output)
deffuz_output = operator.defuzzyficate(output_region_c, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Tc, 'e volume ', Vc, 'e saída ', deffuz_output)
deffuz_output = operator.defuzzyficate(output_region_d, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Td, 'e volume ', Vd, 'e saída ', deffuz_output)
deffuz_output = operator.defuzzyficate(output_region_e, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Te, 'e volume ', Ve, 'e saída ', deffuz_output)


""" ####################################################################################################

6. Baseado nos restultados do Exercício 3, determine então os valores retornados do processo de defuzzyficação
quando se aplica o método do "Primeiro Máximo"

""" ####################################################################################################

method = 'mpm'
deffuz_output = operator.defuzzyficate(output_region_a, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Ta, 'e volume ', Va, 'e saída ', deffuz_output)
deffuz_output = operator.defuzzyficate(output_region_b, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Tb, 'e volume ', Vb, 'e saída ', deffuz_output)
deffuz_output = operator.defuzzyficate(output_region_c, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Tc, 'e volume ', Vc, 'e saída ', deffuz_output)
deffuz_output = operator.defuzzyficate(output_region_d, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Td, 'e volume ', Vd, 'e saída ', deffuz_output)
deffuz_output = operator.defuzzyficate(output_region_e, method)
print('Como aplicação do método defuzzy', method, 'e entradas temperatura ', Te, 'e volume ', Ve, 'e saída ', deffuz_output)

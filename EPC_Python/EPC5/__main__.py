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

	Para um sistema elétrico de potência há a necessidade de se classificar disturbios relacionados à
	qualidade de energia elétrica.
	Assim baseando-se em medições de grandeza elétricas, pretende-se projetar um sistema fuzzy tipo
	mandani para classificar os seguintes tipos de distúrbios.
		Interrupção
		Afundamento
		Elevação
		Operação Normal
		Presença Harmõnicas

""" ####################################################################################################

#Entrada 1
vf_muito_baixa = Region(name='vf_muito_baixa', npoints=200, universe_size=1.8, region_min=0, region_max=0.12, region_type='trapezoid', trap_init=0, trap_end=0.09)
vf_baixa = Region(name='vf_baixa', npoints=200, universe_size=1.8, region_min=0.09, region_max=0.96, region_type='trapezoid', trap_init=0.12, trap_end=0.94)
vf_media = Region(name='vf_media', npoints=200, universe_size=1.8, region_min=0.94, region_max=1.06, region_type='trapezoid', trap_init=0.96, trap_end=1.04)
vf_alta = Region(name='vf_alta', npoints=200, universe_size=1.8, region_min=1.04, region_max=1.8, region_type='trapezoid', trap_init=1.1, trap_end=1.8)
vf = [vf_muito_baixa, vf_baixa, vf_media, vf_alta]

#Entrada 2
dht_pequena = Region(name='dht_pequena', npoints=200, universe_size=100, region_min=0, region_max=6, region_type='trapezoid', trap_init=0, trap_end=5)
dht_grande = Region(name='dht_grande', npoints=200, universe_size=100, region_min=5, region_max=100, region_type='trapezoid', trap_init=7, trap_end=100)
dht = [dht_pequena, dht_grande]

#Saida
fo_interrupcao = Region(name='fo_interrupcao', npoints=200, universe_size=1, region_min=0, region_max=0.333, region_type='triangular')
fo_afundamento = Region(name='fo_afundamento', npoints=200, universe_size=1, region_min=0.1667, region_max=0.5, region_type='triangular')
fo_operacao_normal = Region(name='fo_operacao_normal', npoints=200, universe_size=1, region_min=0.333, region_max=0.667, region_type='triangular')
fo_elevacao = Region(name='fo_elevacao', npoints=200, universe_size=1, region_min=0.5, region_max=0.833, region_type='triangular')
fo_harmonicas = Region(name='fo_harmonicas', npoints=200, universe_size=1, region_min=0.667, region_max=1, region_type='triangular')
fo = [fo_interrupcao, fo_afundamento, fo_operacao_normal, fo_elevacao, fo_harmonicas]

#classes
class_1 = Region(name='interrupcao', npoints=200, universe_size=1, region_min=0, region_max=0.333, region_type='triangular')
class_2 = Region(name='afundamento', npoints=200, universe_size=1, region_min=0.166, region_max=0.5, region_type='triangular')
class_3 = Region(name='operacao_normal', npoints=200, universe_size=1, region_min=0.333, region_max=0.666, region_type='triangular')
class_4 = Region(name='elevacao', npoints=200, universe_size=1, region_min=0.5, region_max=0.833, region_type='triangular')
class_5 = Region(name='harmonicas', npoints=200, universe_size=1, region_min=.666, region_max=1, region_type='triangular')
classes = [class_1, class_2, class_3, class_4, class_5]

def rules(vf, dht):
	if vf == vf_muito_baixa and dht == dht_pequena:
		return fo_interrupcao
	if vf == vf_baixa and dht == dht_pequena:
		return fo_afundamento
	if vf == vf_media and dht == dht_pequena:
		return fo_operacao_normal
	if vf == vf_alta and dht == dht_pequena:
		return fo_elevacao
	if vf == vf_muito_baixa and dht == dht_grande:
		return fo_interrupcao
	if vf == vf_baixa and dht == dht_grande:
		return fo_harmonicas
	if vf == vf_media and dht == dht_grande:
		return fo_harmonicas
	if vf == vf_alta and dht == dht_grande:
		return fo_harmonicas

operator = Operators()

vf_real = [0.01, 0.05, 0.50, 0.85, 1.02, 0.97, 1.57, 1.26, 0.99, 1.20]
dht_real = [0.34, 16.26, 4.84, 1.79, 0.47, 1.21, 4.76, 1.21, 16.32, 18.96]
defuzzy = []
out_classes = []
for i in range (0, 10):
	out_fuzzy = operator.get_output(in_regions=[vf, dht], x=[vf_real[i], dht_real[i]], rule_function=rules, function_inputs=2, implication='mandani', agregation='max')
	out_value = operator.defuzzyficate(out_fuzzy, defuzzy_rule='cda')
	defuzzy.append(out_value)
	out_classes.append(operator.classificate(classes=classes, universe_init=0, universe_size=1, output=out_value))

print('Os Valores Fuzzy São:')
print('\t', defuzzy)

print('As Classificações São:')
print(end='\t')
print_names(out_classes)
print('')

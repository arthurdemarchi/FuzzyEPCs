"""
EXercício: EPC2
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
from ..MyLibs.relations import Relations
from ..MyLibs.relations_operators import RelationOperator

""" ####################################################################################################

1. Considere a função de pertinência abaixa a qual está descrevendo 5 conjuntos fuzzy que representam a
temperatura de um processo industrial.

""" ####################################################################################################

"""
1a. Encontre as expressões analíticas referentes a cada um dos conjuntos fuzzy.
"""

#Resposta:
#Muito Baixa
#	u(x) =  1, se 0 <= x < 5
#	u(x) = -0.1x + 1.5 se 5 <= x < 15
#	u(x) =  0 CC
#Baixa
#	u(x) =  0.1x - 0.5 se 5 <= x < 15
#	u(x) = -0.1x + 2.5 se 15 <= x < 25
#	u(x) =  0 CC
#Média
#	u(x) =  0.1x - 1.5 se 15 <= x < 25
#	u(x) = -0.1x + 3.5 se 25 <= x < 35
#	u(x) =  0 CC
#Alta
#	u(x) =  0.1x - 2.5 se 25 <= x < 35
#	u(x) = -0.1x + 4.5 se 35 <= x < 45
#	u(x) =  0 CC
#Muito Alta
#	u(x) =  0.1x - 3.5 se 35 <= x < 45
#	u(x) =  1 se 45 <= x < 50
#	u(x) =  0 CC

"""
1b. Elabore os procedimentos computacionais que permitam mapear os conjunto fuzzy acima, utilizando para tanto 1000
	pontos de discretização {Sugestão: Utilize Arrays}.
	Para verificar nível de generalização do seu sistema, verifique se haverá necessidade de mofigicações acentuadas
	quando passarmos a trabalhar com 500 ou 2000 pontos de discretização.
"""

#Resposta: Partindo da biblioteca implementada pelo Aluno de forma genérica.
#O Construtor da classe Region determina as funções a partir de seu tipo e alguns pontos característicos.
#As funções triangulares são assumidamente simitréticas com pertinência máxima 1, basta passar o ponto de início e
#final de pontos ativados da função.
#O mesmo vale para as funções trapezoidais, no entanto também é necessário passar o ponto de inicio e fim do teto
#do trapezoide.

#1000 Pontos
muito_baixa = Region(name='muito_baixa', npoints=1000, universe_size=50, region_min=0, region_max=15, region_type='trapezoid', trap_init=0, trap_end=5)
baixa = Region(name='baixa', npoints=1000, universe_size=50, region_min=5, region_max=25, region_type='triangular')
media = Region(name='media', npoints=1000, universe_size=50, region_min=15, region_max=35, region_type='triangular')
alta = Region(name='alta', npoints=1000, universe_size=50, region_min=25, region_max=45, region_type='triangular')
muito_alta = Region(name='muito_alta', npoints=1000, universe_size=50, region_min=35, region_max=50, region_type='trapezoid', trap_init=45, trap_end=50)

#Construindo um array com todas as regiões
fuzzy = [muito_baixa, baixa, media, alta, muito_alta]

#Visualizando resultados
plot(fuzzy, "Regiões Fuzzy do Exercício 1 com 1000 pontos de Discretização", 'x', 'u(x)', True, 'Fuzzy/EPC2/EPC2-1b1.png')

#500 Pontos
muito_baixa = Region(name='muito_baixa', npoints=500, universe_size=50, region_min=0, region_max=15, region_type='trapezoid', trap_init=0, trap_end=5)
baixa = Region(name='baixa', npoints=500, universe_size=50, region_min=5, region_max=25, region_type='triangular')
media = Region(name='media', npoints=500, universe_size=50, region_min=15, region_max=35, region_type='triangular')
alta = Region(name='alta', npoints=500, universe_size=50, region_min=25, region_max=45, region_type='triangular')
muito_alta = Region(name='muito_alta', npoints=500, universe_size=50, region_min=35, region_max=50, region_type='trapezoid', trap_init=45, trap_end=50)

#Construindo um array com todas as regiões
fuzzy = [muito_baixa, baixa, media, alta, muito_alta]

#Visualizando resultados
plot(fuzzy, "Regiões Fuzzy do Exercício 1 com 500 pontos de Discretização", 'x', 'u(x)', True, 'Fuzzy/EPC2/EPC2-1b2.png')

#2000 pontos
muito_baixa = Region(name='muito_baixa', npoints=2000, universe_size=50, region_min=0, region_max=15, region_type='trapezoid', trap_init=0, trap_end=5)
baixa = Region(name='baixa', npoints=2000, universe_size=50, region_min=5, region_max=25, region_type='triangular')
media = Region(name='media', npoints=2000, universe_size=50, region_min=15, region_max=35, region_type='triangular')
alta = Region(name='alta', npoints=2000, universe_size=50, region_min=25, region_max=45, region_type='triangular')
muito_alta = Region(name='muito_alta', npoints=2000, universe_size=50, region_min=35, region_max=50, region_type='trapezoid', trap_init=45, trap_end=50)

#Construindo um array com todas as regiões
fuzzy = [muito_baixa, baixa, media, alta, muito_alta]

#Visualizando resultados
plot(fuzzy, "Regiões Fuzzy do Exercício 1 com 2000 pontos de Discretização", 'x', 'u(x)', True, 'Fuzzy/EPC2/EPC2-1b3.png')

"""
1c.	Elabore os Procedimentos computacionais que, dado um valor qualquer de x, permitam indicar quais dos conjuntos fuzzy
	acima estarão ativos, ou seja, aqueles que possuem u(x) != 0.
"""

#Resposta: Este desafio foi solicionado através da seguinte estratégia:
#	Dentro da Classe Region foi implementado um método is_active() que determina dado um valor se aquela região esta ativa.
#	Isso é feito através do método get_u(), também da classe region, que retorna um valor de pertinência pra qualquer x 
# 	pertencente ao universo daquela regioão.
#	Implementado este código na Classe Region foi então implementado na Classe Operators um método (is_active()) que recebendo
# 	uma lista de regiões usa seus métodos internos para saber quais estão ativas e retorna uma lista com o nome das regiões.
# 	Bibliotecas estão todas indexadas no módulo Mylibs, foram implementadas pelo aluno, e podem ser revisadas conforme
#	necessário.
#	Com posse de tudo isso para este exercício basta instanciar operator e utilizar o seu método is_actve()
#	Para o exemplo será utilizado valor 36.1, onde as regiões alta e muito alta estão ativadas.
operator = Operators()
regions = operator.is_active(fuzzy, 36.1)
print('Resultado Exemplo Exercício 1-C:', end='\n\t')
print_names(regions)

"""
1d.	Elabore os procedimentos computacionais que, dado um conjunto fuzzy que esta ativo, retorne o respectivo valor do grau de
	pertinência em relação a um valor de temperatura x pertencente ao universo do discurso.
"""

#Resposta: Este exercício é solucionado pelo método get_u() implementado dentro da classe Region.
#sua resposta para valores não ativos é sempre zero, caso seja interessante manter a resposta como None, ou False, podemos rapida-
#mente trocar esta da seguinte forma:
def new_get_u(region, x):
	if x > region.universe_size or x < 0:
		print('Error: X Out of universe.')
		return None
	if not region.is_active(x):
		print('Function not Activated')
		return None
	return region.get_u(x)


"""
1e.	Elabore os procedimentos computacionais que dado um conjunto fuzzy, bem como um valor de grau de pertinência, retorne então o
	respectivo conjunto crisp representando o alfa-corte efetuado.
"""

#Resposta: Este exercício é solucionado pelo método get_alfa_cut() implementado dentro da classe Region.
#	Exemplificando uso temos:
region_1d = Region('region_1d', 100, 10, 5, 10, 'triangular')
result_1d = region_1d.get_alfa_cut(0.9)
print('Resultado Exemplo Exercício 1-D: \n \t', result_1d, '\n')

""" ####################################################################################################

2. Baseado nos procedimentos computacionais realizados acima faça.

""" ####################################################################################################


"""
2a. Imprima na mesma folha os gráficos (conforme a figura anterior) dos cinco conjuntos fuzzy quando utilizamos 50
	e 1000 pontos de discretização para representa-los, explicando ainda a importância de se especificar corretamente
	este parâmetro.
"""

#Resposta: O código abaixo gera as duas figuras requeridas e as plota em um mesmo arquivo png como pedido, uma unica folha.
#A definição do parâmetro e discretização é muito importante pois o mesmo define com qual precisão temos acesso aos dados da
#região fuzzy.

muito_baixa_50 = Region(name='muito_baixa_50', npoints=50, universe_size=50, region_min=0, region_max=15, region_type='trapezoid', trap_init=0, trap_end=5)
baixa_50 = Region(name='baixa_50', npoints=50, universe_size=50, region_min=5, region_max=25, region_type='triangular')
media_50 = Region(name='media_50', npoints=50, universe_size=50, region_min=15, region_max=35, region_type='triangular')
alta_50 = Region(name='alta_50', npoints=50, universe_size=50, region_min=25, region_max=45, region_type='triangular')
muito_alta_50 = Region(name='muito_alta_50', npoints=50, universe_size=50, region_min=35, region_max=50, region_type='trapezoid', trap_init=45, trap_end=50)

#Construindo um array com todas as regiões
fuzzy_50 = [muito_baixa_50, baixa_50, media_50, alta_50, muito_alta_50]

muito_baixa_1000 = Region(name='muito_baixa_1000', npoints=1000, universe_size=50, region_min=0, region_max=15, region_type='trapezoid', trap_init=0, trap_end=5)
baixa_1000 = Region(name='baixa_1000', npoints=1000, universe_size=50, region_min=5, region_max=25, region_type='triangular')
media_1000 = Region(name='media_1000', npoints=1000, universe_size=50, region_min=15, region_max=35, region_type='triangular')
alta_1000 = Region(name='alta_1000', npoints=1000, universe_size=50, region_min=25, region_max=45, region_type='triangular')
muito_alta_1000 = Region(name='muito_alta_1000', npoints=1000, universe_size=50, region_min=35, region_max=50, region_type='trapezoid', trap_init=45, trap_end=50)

#Construindo um array com todas as regiões
fuzzy_1000 = [muito_baixa_1000, baixa_1000, media_1000, alta_1000, muito_alta_1000]


#Escrevendo PNG dos resultados
sets_of_regions = [fuzzy_50, fuzzy_1000]
titles = ["Exercício 2 - 50 Pontos", "Exercício 2 - 1000 Pontos"]
subplot(sets_of_regions, titles, True, 'Fuzzy/EPC2/EPC2-2a.png')


"""
2b.	Imprima o conjunto fuzzy resultante da "União" dos cinco conjuntos fuzzy definidos acima, utilizando para tanto 1000
	pontos de discretização e o operador Máximo.

2c.	Imprima o Conjunto fuzzy resultante da Intersecção dos cinco conjuntos fuzzy definidos acima, utilizando para tanto 500
	pontos de discretização e o operador Mínimo.

2d.	Imprima o conjunto fuzzy resultante da operação de Complemento efetuada sobre o conjunto fuzzy C.

imptima b, c e d em uma mesma folha.
"""

#Resposta: As funções de união, intersecção e complemento estão implementadas na classe Operators de forma genérica.
#novamente todas as implesmentações feitas pelo aluno.

#Conjunto com 500 pontos
muito_baixa_500 = Region(name='muito_baixa_500', npoints=500, universe_size=50, region_min=0, region_max=15, region_type='trapezoid', trap_init=0, trap_end=5)
baixa_500 = Region(name='baixa_500', npoints=500, universe_size=50, region_min=5, region_max=25, region_type='triangular')
media_500 = Region(name='media_500', npoints=500, universe_size=50, region_min=15, region_max=35, region_type='triangular')
alta_500 = Region(name='alta_500', npoints=500, universe_size=50, region_min=25, region_max=45, region_type='triangular')
muito_alta_500 = Region(name='muito_alta_500', npoints=500, universe_size=50, region_min=35, region_max=50, region_type='trapezoid', trap_init=45, trap_end=50)

#Construindo um array com todas as regiões
fuzzy_500 = [muito_baixa_500, baixa_500, media_500, alta_500, muito_alta_500]

#Conjunto com 1000 Pontos
muito_baixa_1000 = Region(name='muito_baixa_1000', npoints=1000, universe_size=50, region_min=0, region_max=15, region_type='trapezoid', trap_init=0, trap_end=5)
baixa_1000 = Region(name='baixa_1000', npoints=1000, universe_size=50, region_min=5, region_max=25, region_type='triangular')
media_1000 = Region(name='media_1000', npoints=1000, universe_size=50, region_min=15, region_max=35, region_type='triangular')
alta_1000 = Region(name='alta_1000', npoints=1000, universe_size=50, region_min=25, region_max=45, region_type='triangular')
muito_alta_1000 = Region(name='muito_alta_1000', npoints=1000, universe_size=50, region_min=35, region_max=50, region_type='trapezoid', trap_init=45, trap_end=50)

#Construindo um array com todas as regiões
fuzzy_1000 = [muito_baixa_1000, baixa_1000, media_1000, alta_1000, muito_alta_1000]


#Insanciando o Operador
operator = Operators()

#Fazendo União
union_1000 = operator.union(fuzzy_1000)

#Fazendo Intersecção
intersection_500 = operator.intersection(fuzzy_500)

#Fazendo Complemento
complement_media_500 = operator.complement(media_500)

#Preparando para o subplot
sets_of_regions = [union_1000, intersection_500, complement_media_500]
titles = ['União 1000', 'Intersecção 500', 'complemento de C']
subplot(sets_of_regions, titles, True, 'Fuzzy/EPC2/EPC2-2bcd.png')

""" ####################################################################################################

3. Baseado nos procedimentos computacionais realizados no primeiro e segundo exercício, considera-se ainda
os apenas os conjuntos fuzzy ativos para uma determinada temperatura, faça os seguintes gráficos:

""" ####################################################################################################

"""

3a. Imprima o conjunto Fuzzy resultante da União dos Conjuntos fuzzy ativos em x = 16,75

3b. Imprima o conjunto Fuzzy resultante da União dos Conjuntos fuzzy ativos em x = 37,29

3c. Imprima o conjunto Fuzzy resultante da Intersecção dos Conjuntos fuzzy ativos em x = 20

3d. Imprima o conjunto Fuzzy resultante da Intersecção dos Conjuntos fuzzy ativos em x = 40

"""
#Resposta: Utilizando as funções is_active em combinação com outras da classe Operators temos:

#Criando conjunto exigido por a
active_1675 = operator.is_active(fuzzy_1000, 16.75)
union_1675 = operator.union(active_1675)

#Criando conjunto exigido por b
active_3729 = operator.is_active(fuzzy_1000, 37.29)
union_3729 = operator.union(active_3729)

#Criando conjunto exigido por c
active_20 = operator.is_active(fuzzy_1000, 20)
intersection_20 = operator.intersection(active_20)

#Criando conjunto exigido por d
active_40 = operator.is_active(fuzzy_1000, 40)
intersection_40 = operator.intersection(active_40)

sets_of_regions = [union_1675, union_3729, intersection_20, intersection_40]
titles = ['União ativos em 16,75', 'União ativos em 37,29', 'Intersecção ativos em 20', 'Intersecção ativos em 40']
subplot(sets_of_regions, titles, True, 'Fuzzy/EPC2/EPC2-3abcd.png')

""" ####################################################################################################

4. Refaça o exercício anterior adotando os operadores Soma Algébrica (União) e Produto Algébrico
(Intersecção)

""" ####################################################################################################

#Resposta: Mesmo código, com a opção de união e soma especificada:

#Criando conjunto exigido por a
active_1675 = operator.is_active(fuzzy_1000, 16.75)
union_1675 = operator.union(active_1675, 'algebric_sum')

#Criando conjunto exigido por b
active_3729 = operator.is_active(fuzzy_1000, 37.29)
union_3729 = operator.union(active_3729, 'algebric_sum')

#Criando conjunto exigido por c
active_20 = operator.is_active(fuzzy_1000, 20)
intersection_20 = operator.intersection(active_20, 'algebric_product')

#Criando conjunto exigido por d
active_40 = operator.is_active(fuzzy_1000, 40)
intersection_40 = operator.intersection(active_40, 'algebric_product')

sets_of_regions = [union_1675, union_3729, intersection_20, intersection_40]
titles = ['União ativos em 16,75', 'União ativos em 37,29', 'Intersecção ativos em 20', 'Intersecção ativos em 40']
subplot(sets_of_regions, titles, True, 'Fuzzy/EPC2/EPC2-4abcd.png')


""" ####################################################################################################

5. Basedo nos procedimentos computacionais anteriores, imprima os gráficos resultantes das seguintes operações

""" ####################################################################################################

"""

5a. AuBuC
5b. Bint(CuD)
5c. (AintB)u(BintC)
5d. (notA)u(BintC)u(notD)

"""

#Resposta: Isolando os conjuntos discretizado em mil para melhor visualização
A = fuzzy_1000[0]
B = fuzzy_1000[1]
C = fuzzy_1000[2]
D = fuzzy_1000[3]
E = fuzzy_1000[4]

region_5a = operator.union([A, B, C])

region_5b = operator.union([C, D])
region_5b = operator.intersection([region_5b, B])

region_5c_1 = operator.intersection([A, B])
region_5c_2 = operator.intersection([B, C])
region_5c = operator.union([region_5c_1, region_5c_2])

region_5d_1 = operator.complement(A)
region_5d_2 = operator.intersection([B, C])
region_5d_3 = operator.complement(D)
region_5d = operator.union([region_5d_1, region_5d_2, region_5d_3])

sets_of_regions = [region_5a, region_5b, region_5c, region_5d]
titles = ['AuBuC', 'Bint(CuD)', '(AintB)u(BintC)', '(notA)u(BintC)u(notD)']
subplot(sets_of_regions, titles, True, 'Fuzzy/EPC2/EPC2-5abcd.png')


""" ####################################################################################################

6. Sejam três relações fuzzy discretas as quais descrevem o nível de relacionamento entres as variáveis
de um processo, sendo definas por R(x,y) e S(y,z), onde x E X, y E Y, z E Z. Os respectivos universos de
discurso estarão especificados por X = {x1, x2, x3 ... x10}; Y = {y1, y2, ye .. y5}; Z = {z1, z2 ... z15}.
A partir da geração de valores aleatórios uniformemente distribuídos entre 0 e 1 para R(x,y) e S(y,z),
faça as seguintes atividades:

""" ####################################################################################################

"""
6a. Calcular e imprimir a composição resultante R(x,y)max-minS(y,z)
"""

#Resposta: Utilizando as definições Implementadas pelo aluno nas classes Relation e RelationsOperator
#os exercícios abaixo são resolvidos de forma direta.

operator = RelationOperator()

relation_1 = Relations('random', 10, 5)
relation_2 = Relations('random', 5, 15)
relation_3 = operator.max_min(relation_1, relation_2)

#Imprimindo Resultados
print('Matriz R(x,y)')
relation_1.print()
print('Matriz S(y,z)')
relation_2.print()
print('Matriz R(x,y)max-minS(y,z)')
relation_3.print()

"""
6b. Calcular e imprimir a composição resultante R(x,y) S(y,z)
"""
relation_4 = operator.max_prod(relation_1, relation_2)
print('Matriz R(x,y)max-prodS(y,z)')
relation_4.print()

"""
6c. Calcular e imprimir a composição resultante R(x,y) S(y,z)
"""
relation_5 = operator.max_media(relation_1, relation_2)
print('Matriz R(x,y)max-mediaS(y,z)')
relation_5.print()

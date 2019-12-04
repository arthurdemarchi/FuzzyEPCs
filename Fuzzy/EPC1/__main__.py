"""
EXercício: EPC1
Aluno: Arthur Denarchi
nUSP: 7992894
"""

"""
AVISO: TODOS OS IMPORTS SÃO DE ''BILBIOTECAS'' IMPLEMENTADAS PELO PŔOPRIO ALUNO
ESTÃO EM OUTROS ARQUIVOS APENAS POR ORGANIZAÇÃO E REUTILIZAÇÃO DE SOFTWARE.
BIBLIOTECAS JUNTOS EM ANEXO PARA CORREÇÃO.
"""
from ..MyLibs.region import Region
from ..MyLibs.utils import plot


""" ####################################################################################################

1. Considere o conjunto fuzzy A definido no universo de discurso X = {x e R | 0 <= x <= 10},
	o qual é representado pela seguinte função de pertinência:
	def fun_ex1()

""" ####################################################################################################

def fun_ex1(x):
	if x >= 3 and x<= 5:
		return 0.5*x-1.5
	elif x >=5 and x <= 7:
		return -0.5*x+3.5
	else:
		return 0
"""
1a. Esboce o fráfico da função de pertinência representada acima, indicando também qual é
	o seu tipo.
"""

#Resposta: O tipo da função descrita em fun_ex1 é triangular.
# Imagem gerado pelo código abaixo em anexo.
region = Region(name='Region', npoints=1000, universe_size=10, region_min=3, region_max=4, region_type='triangular')
plot(region, 'EPC1 - Esboço do Gráfico do Exercício 1-a: TRIANGULAR', 'X', 'Y', True, 'Fuzzy/EPC1/EPC1-1a.png')

"""
1b. Sabendo-se que a função acima está representando o conjunto referente à temperatura "média"
	de um determinado processo industrial, explique então qual o significado que esta embutido em
	tal representação.
"""

#Resposta: Nesta representação está embutido a ideia de que existe um ponto ótimo de máxima pertinência
#ao conjunto, ou seja, o especialista especificou um valor ótimo de temperatura que é definido como "médio"
#a partir dali os valores ao redor são proporcionalmente cada vez menos pertinentes.

"""
1c. Explique se o conjunto fuzzy acima é considerado um conjunto normalizado.
"""

#Resposta: O conjunto é considerado normalizado pois o(s) ponto(s) máximo(s) de pertinência são equivalentes
#a pertinência completa(1).

"""
1d. Explique se o conjunto fuzzy acima é considerado convexo.
"""

#Resposta: O conjunto acima é considerado convexo pois sua forma se da apenas por duas curvas, uma sempre
#crescente seguida de uma sempre decrescente. Essa característica impossibilita que exista um ponto no universo
#da região que seja considerado minimo local. Assim é impossível traçar uma "reta" que lique dois pontos no universo
#e não esta contida na curva de pertinência desenhada no gráfico.


""" ####################################################################################################

2. Calcule cardinalidade dos conjuntos fuzzy discretos dados a seguir:

""" ####################################################################################################
"""
	2a. A = 0.3/x1 + 0.5/x2 + 0.9/x3 + 0.4/x4 + 0.1/x5
	#Resposta: 0.3+0.5+0.9+0.4+0.1 = 2.2

	2b. A = 0.0/x1 + 0.4/x2 + 1.0/x3 + 1.0/x4 + 0.4/x5 + 0.0/x6
	#Resposta: 2.8

	2c. u = x/(x+1), com x E {0, 1, 2 ... 10}
	#Resposta 0 + 1/2 + 2/3 + 3/4 + ... 10/11 = 7.98012265512
"""


""" ####################################################################################################

3. Uma equipe de engenheiros e cientistas obteve a partir de experimentação diversos valores de alfa-
cortes referentes a um conjunto fuzzy V que esta sendo mapeado, o qual está representando o ajuste de
vazão v de uma coluna de destilação de petróleo. Os valores referes aos alfa-cortes são dados a seguir:

V0.00 = {v E R | 2.0 <= v 8.0}
V0.25 = {v E R | 2.5 <= v 7.5}
V0.50 = {v E R | 3.0 <= v 7.0}
V0.75 = {v E R | 3.5 <= v 6.5}
V1.00 = {v E R | 4.0 <= v 6.0}

""" ####################################################################################################

#Resposta pela análise dos cortes acima podemos ver que temos um aumento de 0.25 de pertinência a cada 0.5
#de aumento no valor dos elementos do universo, percebe-se pelos valores também uma simetria na desigualdade
#Assim temos uma função de pertinência que possui duas retas com "slope" +1/2 e -1/2. Vemos também que existe
#uma constância de pertiência 1 nos valores entre 4 e 6 (assumindo região normalizada).
#Dado análise acima temos uma função trapezoidal, simétrica de slope 1/2, com teto do trapézio de 4 a 6.

# Imagem gerado pelo código abaixo em anexo.
region = Region(name='Region', npoints=800, universe_size=8, region_min=2, region_max=8, region_type='trapezoid', trap_init=4, trap_end=6)
plot(region, 'EPC 1 - Esboço do Gráfico do Exercício 3', 'V', 'U', True, 'Fuzzy/EPC1/EPC1-3.png')

#Expressão Analítica
#	se 2.0 <= x < 4.0 -> u = 0.5x-1
#	se 4.0 <= x < 6 -> u = 1
#	se 6.0 <= x < 8 -> u = -0.5x+4
#	cc, u = 0

""" ####################################################################################################

4. Um determinado conjunto fuzzy deverá ser mapeado utilizando função de pertinência triangular ou
trapezoidal. Discorra sobre que subsídios você usuaria para escolher uma dessas funções para representar
este conjunto. Explicite os seus argumentos através de um exemplo.

""" ####################################################################################################

#Resposta: A principal diferença nas funções trapezoidal e triangular esta no teto constante de pertiência
#da função trapezoidal, enquanto que na triangular apenas um ponto tem pertinência máxima, na trapezoidal 
#varios pontos tem pertinência máxima. Assim sendo, a escolha da função triangular se da quando existe um
#ponto claro numérico que define melhor a condição linguístaca e a função trapezoidal é mais indicado quando
#este ponto esta nebuloso em um grande conjunto.
#Do ponto de vista dos vários conjuntos fuzzy temos que é estranho observar mais de uma região com pertinência
#máxima para um mesmo semi conjunto do universo. Pois não faz sentido por exemplo que um carro esteja ao mesmo
#tempo com velocidade alta(pertinencia máxima) e velocidade média (pertinência máxima). Assim sendo, caso haja
#uma sobreposição muito grande dos conceitos não havendo subconjuntos onde apenas uma região se aplica, fica
#inviável a utilização de regiões com função trapezoidal.

#Exemplificando:
# 	Se eu divido a velocidade de um carro entre baixa, média e alta
# 	E como especialista defino que a velocidade baixa consite do carro parado até um valor próximo de 50km/h
# 	A velocidade média como algo entre talvez 30km/h e 70km/h
# 	A velocidade alta como com certeza maior que 80km/h
# 	Neste caso a função da velocidade baixa é trapezoidal pois não existe sobreposição em seu primeiros valores
# 	dela com nenhuma outra.
# 	A função de velocidade média é triangular pois ambas as outras duas regiões partilham valores com ela
# 	A função de velocidade alta também é trapezoidal pois seus valores finais não são partilhados com nenhuma
# 	outra região

""" ####################################################################################################

5. Explique se a afirmação seguinte é verdadeira ou falsa: "Se um conjunto fuzzy contínuo em seu universo
de discurso tiver algum de seus alfa-cortes também contínuo, então referido conjunto é considerado convexo".

""" ####################################################################################################

#Resposta: A afirmação é falsa. Um contra exemplo são conjuntos fuzzy com mínimos locais são geralmente
#não convexos e são completamente contínuos.
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
from ..MyLibs.number import Number
from ..MyLibs.utils import subplot


""" ####################################################################################################

	Sejam as seguintes funções de pertinência, representando dois números fuzzy A e B, as quais são
	especificadas pelos seguintes padrões geométricos.

""" ####################################################################################################

A_1 = Number(200, 32, 1, 4, 1)
A_2 = Number(200, 32, 1, 4, 2)
A_3 = Number(200, 32, 1, 4, 3)

B_4 = Number(200, 32, 3, 8, 4)
B_5 = Number(200, 32, 3, 8, 5)
B_6 = Number(200, 32, 3, 8, 6)

"""
 A+B
"""
result = A_1.add(B_4)
result_1 = [result.number, A_1.number, B_4.number]

result = A_2.add(B_5)
result_2 = [result.number, A_2.number, B_5.number]

result = A_3.add(B_6)
result_3 = [result.number, A_3.number, B_6.number]

plot_result = [result_1, result_2, result_3]
titles = ['A_1 + B_4', 'A_2 + B_5', 'A_3 + B_6']
subplot(plot_result, titles, True, 'Fuzzy/EPC7/EPC7-1.png')

"""
 A-B
"""
result = A_1.subtract(B_4)
result_1 = [result.number, A_1.number, B_4.number]

result = A_2.subtract(B_5)
result_2 = [result.number, A_2.number, B_5.number]

result = A_3.subtract(B_6)
result_3 = [result.number, A_3.number, B_6.number]

plot_result = [result_1, result_2, result_3]
titles = ['A_1 - B_4', 'A_2 - B_5', 'A_3 - B_6']
subplot(plot_result, titles, True, 'Fuzzy/EPC7/EPC7-2.png')



"""
 AxB
"""
result = A_1.product(B_4)
result_1 = [result.number, A_1.number, B_4.number]

result = A_2.product(B_5)
result_2 = [result.number, A_2.number, B_5.number]

result = A_3.product(B_6)
result_3 = [result.number, A_3.number, B_6.number]

plot_result = [result_1, result_2, result_3]
titles = ['A_1*B_4', 'A_2*B_5', 'A_3*B_6']
subplot(plot_result, titles, True, 'Fuzzy/EPC7/EPC7-3.png')


"""
 A/B
"""
result = A_1.division(B_4)
result_1 = [result.number, A_1.number, B_4.number]

result = A_2.division(B_5)
result_2 = [result.number, A_2.number, B_5.number]

result = A_3.division(B_6)
result_3 = [result.number, A_3.number, B_6.number]

plot_result = [result_1, result_2, result_3]
titles = ['A_1/B_4', 'A_2/B_5', 'A_3/B_6']
subplot(plot_result, titles, True, 'Fuzzy/EPC7/EPC7-4.png')


"""
 min(A,B)
"""
result = A_1.min(B_4)
result_1 = [result, A_1.number, B_4.number]

result = A_2.min(B_5)
result_2 = [result, A_2.number, B_5.number]

result = A_3.min(B_6)
result_3 = [result, A_3.number, B_6.number]

plot_result = [result_1, result_2, result_3]
titles = ['max between A_1, B_4', 'max between A_2, B_5', 'max between A_3, B_6']
subplot(plot_result, titles, True, 'Fuzzy/EPC7/EPC7-5.png')


"""
 max(A,B)
"""
result = A_1.max(B_4)
result_1 = [result, A_1.number, B_4.number]

result = A_2.max(B_5)
result_2 = [result, A_2.number, B_5.number]

result = A_3.max(B_6)
result_3 = [result, A_3.number, B_6.number]

plot_result = [result_1, result_2, result_3]
titles = ['max between A_1 B_4', 'max between A_2 + B_5', 'max between A_3 + B_6']
subplot(plot_result, titles, True, 'Fuzzy/EPC7/EPC7-6.png')

from core.metodosimplex import SimplexPrimal

A = [[1, 2, 1, 0, 0],
     [2,-1, 0, 1, 0],
     [5, 3, 0, 0, 1]]

b = [6, 4, 15]
c = [-5, -4]

prob = SimplexPrimal(A,b,c, output='html=texto.html,minimal')
prob.resolver()

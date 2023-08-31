from vectores import *

def area_triangulo(ax,ay,az,bx,by,bz,cx,cy,cz):
    vec_ab = diferencia(ax,ay,az,bx,by,bz)
    vec_ac = diferencia(ax,ay,az,cx,cy,cz) 
    ab_x_ac = producto_vectorial(vec_ab,vec_ac)
    area_res = norma(ab_x_ac)/2
    return area_res

assert area_triangulo(2,2,0,4,20,0,14,10,0) == 100
assert area_triangulo(4,6,0,4,16,0,12,8,0) == 40
assert area_triangulo(4,4,0,12,4,0,12,12,0) == 32


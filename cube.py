from intersect import *
from vector import V3
from planeh import *
from planef import *
from planel import *

class Cube(object):
    def __init__ (self,center, width,material):
        self.center = center
        self.width = width
        self.material = material
        
        self.izquierda =  PlaneL(V3(center[0]-width/2,center[1],center[2]),width,width, material,-1)
        self.derecha =  PlaneL(V3(center[0]+width/2,center[1],center[2]),width,width, material,1)
        
        self.arriba =  PlaneH(V3(center[0],center[1]+width/2,center[2]),width,width, material,1)
        self.abajo =  PlaneH(V3(center[0],center[1]-width/2,center[2]),width,width, material,-1)
        
        self.frente =  PlaneF(V3(center[0],center[1],center[2]+width/2),width,width, material,1)
        
        
    
    def ray_intersect(self,origin,direction):


        iz = self.izquierda.ray_intersect(origin,direction)
        de = self.derecha.ray_intersect(origin,direction)
        ar = self.arriba.ray_intersect(origin,direction)
        ab = self.abajo.ray_intersect(origin,direction)
        fr = self.frente.ray_intersect(origin,direction)

        interseccion = [iz,de,ar,ab,fr]
       
        menor = 99999
        inter = 0
        for i in range(len(interseccion)):
            if interseccion[i]:
                if interseccion[i].distance < menor:
                    menor =interseccion[i].distance
                    inter = interseccion[i]
               
        return inter
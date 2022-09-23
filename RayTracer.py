import math
from random import random
from Lib import *
from Color import *
from vector import V3
import random
from sphere import *

class Raytracer(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.clear_color =(255,0,0)
        self.current_color= (0,0,0)
        self.framebuffer=[]
        self.ImageAspectRatio = self.width/self.height
        self.fov=int(math.pi/2)
        self.tangente = math.tan(self.fov/2)
        self.density=1
        self.scene=[]
        self.clear()
    
    def clear (self):
        self.framebuffer=[
            [rgbcolor(*self.clear_color) for x in range(self.width)]
            for y in range(self.height)]
    
    def point(self, x,y):
        if (x < self.width and x >= 0 and y < self.height and y >= 0):
            self.framebuffer[y][x] = rgbcolor(*self.current_color)
            
    def write(self,filename):
        writebmp(filename,self.width,self.height,self.framebuffer)
        
    def cast_ray(self,origin,direction):
        
        for s in self.scene:
            if s[0].ray_intersect(origin,direction):
                return s[1]
        else:
            return self.clear_color
    
    def render(self,nombre):
        self.current_color=(0,255,0)
        for y in range(self.height):
            for x in range(self.width):
                
                prob = random.random()
                
                if (prob < self.density):
                
                    i=((2 * (x +0.5 ) / self.width) - 1) * self.ImageAspectRatio * self.tangente
                    j=(1 - (2 * (y + 0.5) / self.height)) * self.tangente
                                        
                    direction = V3(i,j,-1).normalize()
                    origin = V3(0,0,0)
                    self.current_color= self.cast_ray(origin,direction)
                    
                    self.point(x,y)
        self.write(nombre+".bmp")
        
    
        
r=Raytracer(600,700)
r.density=1
r.scene=[
         [Sphere(V3(0,-0.2,-16),0.2),(0,0,0)], #boton
         [Sphere(V3(0,0.8,-16),0.2),(0,0,0)], #boton
         [Sphere(V3(0,1.8,-16),0.2),(0,0,0)], #boton
         [Sphere(V3(0,5,-16),3),(255,255,255)], #Piernas
         [Sphere(V3(0,1,-16),2),(255,255,255)], #Cuerpo
         [Sphere(V3(-0.5,-1.8,-16),0.2),(0,0,0)], #Ojo izquierdo
         [Sphere(V3(0.5,-1.8,-16),0.2),(0,0,0)], #Ojo derecho
         [Sphere(V3(0,-1.4,-16),0.2),(255,128,0)], #Nariz
         [Sphere(V3(0,-1.5,-16),1.5),(255,255,255)], #Cabeza
         
         ]
r.render("Prueba")
   
  
                   
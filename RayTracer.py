from code import interact
import math
from random import random
from Lib import *
from Color import *
from light import Light
from material import Material
from vector import V3
import random
from sphere import *
from light import *

class Raytracer(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.clear_color =(0,0,0)
        self.current_color= (0,0,0)
        self.framebuffer=[]
        self.ImageAspectRatio = self.width/self.height
        self.fov=int(math.pi/2)
        self.tangente = math.tan(self.fov/2)
        self.density=1
        self.scene=[]
        self.light = Light(V3(0,0,0),1)
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
        material, intersect = self.scene_intersect(origin,direction)
        
        if material is None:
            return self.clear_color
        
        light_direction = (self.light.position - intersect.point).normalize()
        intensity = light_direction @ intersect.normal
        
        diffuse = intensidadColor(material.diffuse,intensity)
        
        return diffuse
        
        
        
        
    def scene_intersect(self,origin, direction):
        zbuffer = 9999999999999
        material = None
        intersect = None
        
        for s in self.scene:
            object_intersect = s.ray_intersect(origin,direction)
            if object_intersect:
                if object_intersect.distance < zbuffer:
                    zbuffer = object_intersect.distance
                    material = s.material
                    intersect = object_intersect
        return material, intersect
        
        
    
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
        
    
        
r=Raytracer(800,800)
r.density=1

white = Material(diffuse=(255,255,255))
black = Material(diffuse=(0,0,0))
naranja = Material(diffuse=(255,128,0))
red = Material(diffuse=(255,0,0))
r.clear_color=(0,255,255)

#'''
r.scene=[
         Sphere(V3(0,-1.5,-20),1.5,white), #Cabeza
         Sphere(V3(0,5,-20),3,white), #Piernas
         Sphere(V3(0,1,-20),2,white), #Cuerpo
         Sphere(V3(-0.5,-1.8,-16),0.2,black), #Ojo izquierdo
         Sphere(V3(0.5,-1.8,-16),0.2,black), #Ojo derecho
         Sphere(V3(0,-1.4,-16),0.2,naranja), #Nariz
         Sphere(V3(0,-0.2,-16),0.2,black), #boton
         Sphere(V3(0,0.8,-16),0.2,black), #boton
         Sphere(V3(0,1.8,-16),0.2,black), #boton
         ]
'''
r.scene = [
    Sphere(V3(-6, 0, -16), 2.5, red),
    Sphere(V3(5, 0, -16), 2.5, red),
    Sphere(V3(-0.5, 0, -10), 2.5, white)
]'''
r.render("Prueba2")
   
  
                   
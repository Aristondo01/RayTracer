from code import interact
import math
from random import random
from tokenize import Special
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
        self.light = Light(V3(5,-5,0),1.5,V3(255,255,255))
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
        
        
        #Diffuse 
        light_direction = (self.light.position - intersect.point).normalize()
        diffuse_intensity = light_direction @ intersect.normal
        diffuse = intensidadColor(material.diffuse,diffuse_intensity)
        diffuse = V3(*diffuse) * material.albedo[0]
        
        #Specular
        light_reflection = reflect(light_direction,intersect.normal)
        specular_intensity = self.light.intensity * max(0,(light_reflection @ direction)) **material.spec
        
        specular = self.light.color * specular_intensity * material.albedo[1]
        
        diffuse = diffuse + specular
        
        
        

        return (int(diffuse.x),int(diffuse.y),int(diffuse.z))
        
        
        
        
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

glass = Material(diffuse=(176,223,254),albedo=[0.695,0.305],spec=150)
wood = Material(diffuse=(149,69,53),albedo=[0.85,0.25],spec=5)
ice = Material(diffuse=(0,0,0),albedo=[0.85,0.1],spec=1)

ice2 = Material(diffuse=(255,150,150),albedo=[0.695,0.305],spec=10)





r.clear_color=(255,255,255)


#'''
r.scene=[
         Sphere(V3(0,-1.5,-8),1.2,wood), #Cabeza
         Sphere(V3(0,1,-8),1.5,glass), #Cuerpo
         Sphere(V3(-0.8,1.8,-6),0.5,wood), #Pierna izquierda
         Sphere(V3(0.8,1.8,-6),0.5,wood), #Pierna derecha
         
         Sphere(V3(-1.1,-0.2,-6),0.5,wood), #mano izquierda
         Sphere(V3(1.1,-0.2,-6),0.5,wood), #mano derecha
         
         Sphere(V3(-0.8,-1.8,-6),0.4,wood), #oreja izquierda
         Sphere(V3(0.8,-1.8,-6),0.4,wood), #oreja derecha
         
         Sphere(V3(-0.3,-1.4,-6),0.1,ice), #ojo izquierda
         Sphere(V3(0.3,-1.4,-6),0.1,ice), #ojo derecha
         
         Sphere(V3(0,-0.7,-5),0.3,ice2), #ojo derecha
         
         
         
         ]
'''
r.scene = [
    Sphere(V3(-6, 0, -16), 2.5, rubber),
    Sphere(V3(5, 0, -16), 2.5, rubber),
    Sphere(V3(-0.5, 0, -10), 2.5, ivory)
]'''
r.render("Prueba")
   
  
                   
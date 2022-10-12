import math
from random import random
from Lib import *
from Color import *
from light import Light
from material import Material
import random
from sphere import *
from plane import *
from light import *

MAX_RECURSION_DEPTH =3

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
        self.light = Light(V3(0,-5,0),1.5,V3(255,255,255))
        self.clear()
        self.EnvMap = None
    
    def clear (self):
        self.framebuffer=[
            [rgbcolor(*self.clear_color) for x in range(self.width)]
            for y in range(self.height)]
    
    def point(self, x,y):
        if (x < self.width and x >= 0 and y < self.height and y >= 0):
            self.framebuffer[y][x] = rgbcolor(*self.current_color)
            
    def write(self,filename):
        writebmp(filename,self.width,self.height,self.framebuffer)
    
    def get_background(self):
        if self.EnvMap:
            return self.EnvMap.get_color()
        else:
            return self.clear_color
        
    def cast_ray(self,origin,direction, recursion=0):
        shadow_bais = 1.1
        if recursion >= MAX_RECURSION_DEPTH:
            return self.clear_color
        
        
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
        
        #diffuse = diffuse + specular
        
        #shadow
        shadow_origin = intersect.point + (intersect.normal * shadow_bais)
        shadow_material, shadow_intecsect =self.scene_intersect(shadow_origin,light_direction)
        
        shadow_intensity = 1
        if shadow_material:
            shadow_intensity = 0.3
            
        diffuse = V3(*material.diffuse) * diffuse_intensity * material.albedo[0] * shadow_intensity
        
        
        #reflection
        if material.albedo[2] > 0:
            
            reflect_direction = reflect(direction,intersect.normal)
            reflect_bias = -0.5 if reflect_direction @ intersect.normal < 0 else 0.5
            reflect_origin = intersect.point + (intersect.normal * reflect_bias)
            reflect_color = V3(*self.cast_ray(reflect_origin,reflect_direction,recursion+1))
        else:
            reflect_color =V3(0,0,0)
        
        reflection = reflect_color * material.albedo[2]
        
        #refractions
        if material.albedo[3] > 0:
            refract_direction = refract(direction,intersect.normal, material.refractive_index)
            refract_bias = -0.5 if refract_direction @ intersect.normal < 0 else 0.5
            refract_origin = intersect.point + (intersect.normal * refract_bias)
            refract_color = V3(*self.cast_ray(refract_origin,refract_direction,recursion+1))
        else:
            refract_color =V3(0,0,0)
        
        refraction = refract_color * material.albedo[3]
        
        diffuse= diffuse + reflection +specular +  refraction
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

wood = Material(diffuse=(149,69,53),albedo=[0.85,0.25],spec=5)
ice = Material(diffuse=(0,0,0),albedo=[0.85,0.1],spec=1)

ice2 = Material(diffuse=(255,150,150),albedo=[0.695,0.305],spec=10)

rubber = Material(diffuse=(80,0,0),albedo=[0.9, 0.1, 0, 0],spec=10)
ivory = Material(diffuse=(100,100,80),albedo=[0.695, 0.305, 0.1, 0],spec=50)
mirror = Material(diffuse=(255,255,255),albedo=[0, 1, 0.8, 0],spec=1425)
glass = Material(diffuse=(150,180,200),albedo=[0, 0.5 ,0.1, 0.8],spec=125, refractive_index=1.5)









r.clear_color=(0,0,100)


r.light = Light(V3(-20, 20, 20), 2,V3(255, 255, 255))
r.scene = [
    Plane(V3(0,2.5,-6),2,2, mirror),
    Sphere(V3(0, -1.5, -10), 1.5, ivory),
    Sphere(V3(0, 0, -5), 0.5, glass),
    Sphere(V3(1, 1, -8), 1.7, rubber),
    Sphere(V3(-2, 1, -10), 2, mirror),
]#'''

r.render("Prueba")
   
  
                   
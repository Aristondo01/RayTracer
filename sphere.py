from intersect import *
class Sphere(object):
    def __init__ (self,center,radius,material):
        self.center = center
        self.radius = radius
        self.material = material
    
    def ray_intersect(self,origin,direction):
        L = self.center - origin
        tca = direction @ L
        
        d2 = L.length() **2 -tca**2
        
        if d2 > self.radius**2:
            return None
        
        
        thc = (self.radius**2 - d2)**0.5
        
        t0 = tca - thc
        t1 = tca + thc
        
        if t0 < 0 :
            t0 =t1
        if t0 < 0:
            return None
        
        hitpoint = direction * t0 + origin
        normal = (hitpoint - self.center).normalize()
        return Intersect(
            distance = t0,
            point = hitpoint,
            normal= normal
            )
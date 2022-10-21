from intersect import *
from vector import V3

class PlaneH(object):
    def __init__ (self,center, width,height ,material,normal):
        self.center = center
        self.width = width
        self.height = height
        self.material = material
        self.normal = V3(0,normal,0)
        self.xmin = center.x-width*0.5
        self.ymin = center.z-width*0.5
    
    def ray_intersect(self,origin,direction):
       
        d = ( self.center.y - origin.y) / direction.y
        impact =direction * d - origin
        
        if d <= 0 or \
            impact.x > (self.center.x + self.width*0.5) or impact.x < (self.center.x - self.width*0.5) or \
            impact.z > (self.center.z + self.height*0.5) or impact.z < (self.center.z - self.height*0.5):
                
            return None
        
        return Intersect(
            distance = d,
            point = impact,
            normal= self.normal,
            porcentaje = ((impact.x - self.xmin)/self.width,(impact.z - self.ymin)/self.height)
            )
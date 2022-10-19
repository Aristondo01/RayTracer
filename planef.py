from intersect import *
from vector import V3

class PlaneF(object):
    def __init__ (self,center, width,height ,material,normal):
        self.center = center
        self.width = width
        self.height = height
        self.material = material
        self.normal = V3(0,0,normal)
        self.wmin = center.x-width/2
        self.ymin = center.y-width/2
        

    
    def ray_intersect(self,origin,direction):
       
        d = ( self.center.z - origin.z) / direction.z
        impact =direction * d - origin
        
        if d <= 0 or \
            impact.x > (self.center.x + self.width/2) or impact.x < (self.center.x - self.width/2) or \
            impact.y > (self.center.y + self.height/2) or impact.y < (self.center.y - self.height/2):
                
            return None
        
        return Intersect(
            distance = d,
            point = impact,
            normal= self.normal
            )
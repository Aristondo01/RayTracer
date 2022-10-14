from intersect import *
from vector import V3

class PlaneL(object):
    def __init__ (self,center, width,height ,material,normal):
        self.center = center
        self.width = width
        self.height = height
        self.material = material
        self.normal = V3(normal,0,0)
    
    def ray_intersect(self,origin,direction):
       
        d = ( self.center.x - origin.x) / direction.x
        impact =direction * d - origin
        
        if d <= 0 or \
            impact.y > (self.center.y + self.width/2) or impact.y < (self.center.y - self.width/2) or \
            impact.z > (self.center.z + self.height/2) or impact.z < (self.center.z - self.height/2):
                
            return None
        
        return Intersect(
            distance = d,
            point = impact,
            normal= self.normal
            )
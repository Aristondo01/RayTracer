from intersect import *
from vector import V3

class Plane(object):
    def __init__ (self,center, width,height ,material):
        self.center = center
        self.width = width
        self.height = height
        self.material = material
    
    def ray_intersect(self,origin,direction):
       
        d = ( self.center.y - origin.y) / direction.y
        impact =direction * d - origin
        normal = V3(0,-1,0)
        
        if d <= 0 or \
            impact.x > (self.center.x + self.width/2) or impact.x < (self.center.x - self.width/2) or \
            impact.z > (self.center.z + self.height/2) or impact.z < (self.center.z - self.height/2):
                
            return None
        
        return Intersect(
            distance = d,
            point = impact,
            normal= normal
            )
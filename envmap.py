import numpy 
import mmap
import struct
from math import atan2, pi, acos
from vector import V3
from Color import *


class Envmap(object):
    def _init_(self, path):
        self.path = path
        self.read()
    
    def read(self):
        with open(self.path,"rb") as image:
            image.seek(10)
            header_size = struct.unpack("=l",image.read(4))[0]
            image.seek(18)
            self.width = struct.unpack("=l",image.read(4))[0]
            self.heigth = struct.unpack("=l",image.read(4))[0]
            image.seek(header_size)
            self.pixels=[]
            
            for y in range(self.heigth):
                self.pixels.append([])
                for x in range(self.width):
                    b= ord(image.read(1))
                    g= ord(image.read(1))
                    r= ord(image.read(1))
                    
                    self.pixels[y].append((r,g,b))


    def get_color(self, direction):
        x = int(atan2(direction.z, direction.x) / (2 * pi) + 0.5) * self.width
        y = int(acos(-direction.y / pi) * self.height)

        index = (y * self.width + x) * 3
        c = self.pixels[index].astype(numpy.uint8)
        return V3(c[0], c[1], c[2])
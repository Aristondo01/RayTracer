import numpy 
import mmap
import struct
from math import atan2, pi, acos
from vector import V3
from Color import *


class Envmap(object):
    def __init__(self, path):
        self.path = path+".bmp"
        self.pixels=None
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
        direction = direction.normalize()
        x = int((atan2(direction.z, direction.x) / (2 * pi) + 0.5) * self.width)
        y = int(acos(-direction.y) / pi * self.heigth)
        
        """print(acos(-direction.y / pi))
        print()
        print(x,y)
        print(len(self.pixels),len(self.pixels[0]))
        print()"""
        return self.pixels[y][x]
        
import numpy 
import mmap
import struct
from math import atan2, pi, acos

class Envmap(object):
    def _init_(self, path):
        self.path = path
        self.read()
    
    def read(self):
        with open(self.path) as image:
            m = mmap(image.fileno(), 0, access = mmap.ACCESS_READ)
            ba = bytearray(m)
            header_size = struct.unpack("=l", ba[10:14][0])
            self.width = struct.unpack("=l", ba[18:22][0])
            self.height = struct.unpack("=l", ba[22:26][0])
            all_bytes = ba[header_size:]
            self.pixels = numpy.frombuffer(all_bytes, dtype="uint8")

    def get_color(self, direction):
        x = int(atan2(direction.z, direction.x) / (2 * pi) + 0.5) * self.width
        y = int(acos(-direction.y / pi) * self.height)

        index = (y * self.width + x) * 3
        c = self.pixels[index].astype(numpy.uint8)
        return color(c[0], c[1], c[2])
from vector import V3
from textures import *
class Material:
    def __init__(self, diffuse,albedo,spec, refractive_index=0,path=None):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
        self.refractive_index = refractive_index
        if path:
            self.textura = Texture(path+".bmp")
        else:
            self.textura = None
        
from vector import V3


class Light:
    def __init__(self,position, intensity, color=V3(255,255,255)):
        self.position = position
        self.intensity = intensity
        self.color = color
        
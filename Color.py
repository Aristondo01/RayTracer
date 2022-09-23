def rgbcolor(r,g,b):
        b=max(0,min(b,255))
        g=max(0,min(g,255))
        r=max(0,min(r,255))
        
        return bytes([b,g,r])
def intcolor(n):
        return round(n*255)

def intcolora(n):
        return [round(n[0]*255),round(n[1]*255),round(n[2]*255)]

def normalcolor(n):
        return (n/250)
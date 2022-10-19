from rayTracer import *

r=Raytracer(800,500)
r.density=1

wood = Material(diffuse=(255,0,0),albedo=[0.9,0.1,0,0],spec=5,path="tronco")
bwood = Material(diffuse=(255,0,0),albedo=[0.9,0.1,0,0],spec=5,path="madera")
obsidian = Material(diffuse=(255,0,0),albedo=[0.9,0.1,0,0],spec=5,path="obsidiana")
leaf = Material(diffuse=(255,0,0),albedo=[0.9,0.1,0,0],spec=5,path="arbol")
portal = Material(diffuse=(150,180,200),albedo=[0.9, 0.8 ,0.3, 0],spec=500,path="portal")
mirror = Material(diffuse=(255,255,255),albedo=[0.9, 0.8, 0.8, 0],spec=1425,path="vidrio")
glass = Material(diffuse=(150,180,200),albedo=[0, 0.5 ,0.1, 0.8],spec=125,path="vidrio", refractive_index=1.5)


ice = Material(diffuse=(0,0,0),albedo=[0.85,0.1],spec=1)
ice2 = Material(diffuse=(255,150,150),albedo=[0.695,0.305],spec=10)
rubber = Material(diffuse=(80,0,0),albedo=[0.9, 0.1, 0, 0],spec=10)
ivory = Material(diffuse=(100,100,80),albedo=[0.695, 0.305, 0.1, 0],spec=50)

r.setEnvMap("fondo2")

r.clear_color=(0,0,100)

r.light = Light(V3(20, 20, 20), 2,V3(255, 255, 255))
r.scene = [
    #PlaneH(V3(0,-2.5,-6),2,2, mirror,-1),
    
    #PlaneL(V3(1,-1,-6),2,2, wood,-1),
    #Sphere(V3(0, 1.5, -10), 1.5, ivory),
    #Sphere(V3(0, 0, -5), 0.5, glass),
    #Sphere(V3(1, -1, -8), 1.7, rubber),
    #Sphere(V3(-2, -1, -10), 2, mirror),
    Cube((0,1,-5),1,wood),
    Cube((0,-1,-5),1,mirror),
    Cube((2,1,-5),1,leaf),    
    Cube((2,-1,-5),1,bwood),  
    Cube((-2,1,-5),1,obsidian),  
    Cube((-2,-1,-5),1,portal),  
    
    
    
]#'''

r.render("Prueba")

from rayTracer import *

r=Raytracer(900,500)
r.density=1

pato = Material(diffuse=(255,0,0),albedo=[0.9,0.5,0,0],spec=5,path="pato")
door = Material(diffuse=(255,0,0),albedo=[0.9,0.1,0,0],spec=5,path="puerta")
wood = Material(diffuse=(255,0,0),albedo=[0.9,0.2,0,0],spec=10,path="tronco")
brick = Material(diffuse=(255,0,0),albedo=[0.9,0.3,0,0],spec=15,path="ladrillo")
bwood = Material(diffuse=(255,0,0),albedo=[0.9,0.1,0,0],spec=5,path="madera")
obsidian = Material(diffuse=(255,0,0),albedo=[0.9,0.1,0,0],spec=5,path="obsidiana")
leaf = Material(diffuse=(255,0,0),albedo=[0.9,0.1,0,0],spec=5,path="arbol")
portal = Material(diffuse=(255,0,255),albedo=[0.9, 0.8 ,0, 0.4],spec=500,path="portal",refractive_index=1.5)
mirror = Material(diffuse=(0,0,255),albedo=[0,1, 0.8, 0],spec=1450)
agua = Material(diffuse=(0,0,255),albedo=[0.6, 0.7, 1, 0],spec=1450)
glass = Material(diffuse=(150,180,200),albedo=[0, 0.5 ,0.1, 0.8],spec=125,path="vidrio", refractive_index=1.5)


r.setEnvMap("fondo2")

r.clear_color=(0,0,100)

r.light = Light(V3(20, 20, 20), 2,V3(255, 255, 255))
r.scene = [

    
    #------------Arbol--------------------- 
    Cube((-3,-1,-4.9),0.5,wood), #Tronco
    Cube((-3,-0.5,-4.9),0.5,wood), #Tronco
    Cube((-3,0,-4.9),0.5,wood), #Tronco
    Cube((-3,0.5,-4.9),0.5,wood), #Tronco
    
    Cube((-2.5,1,-5),0.5,leaf),  #Hojas
    Cube((-3,1.5,-5),0.5,leaf),  #Hojas
    Cube((-3,1,-4.5),0.5,leaf),  #Hojas
    
    Cube((-3,0.5,-4),0.5,leaf),  #Hojas
    Cube((-2.5,0.5,-4.5),0.5,leaf),  #Hojas  
    Cube((-2.5,0.5,-4),0.5,leaf), #Hojas  
    Cube((-2.5,0.5,-5.5),0.5,leaf), #Hojas  
    Cube((-2.5,0.5,-5),0.5,leaf), #Hojas   
    
       
    #------------Portal--------------------- 
    
    Cube((4,-1,-5),0.5,obsidian), #Obsidiana
    Cube((3.5,-1,-5),0.5,obsidian), #Obsidiana
    Cube((3,-1,-5),0.5,obsidian), #Obsidiana
    Cube((2.5,-1,-5),0.5,obsidian), #Obsidiana
    
    Cube((4,-0.5,-5),0.5,obsidian), #Obsidiana
    Cube((4,0,-5),0.5,obsidian), #Obsidiana
    Cube((4,0.5,-5),0.5,obsidian), #Obsidiana
    Cube((4,1,-5),0.5,obsidian), #Obsidiana
    
    Cube((2.5,-0.5,-5),0.5,obsidian), #Obsidiana
    Cube((2.5,0,-5),0.5,obsidian), #Obsidiana
    Cube((2.5,0.5,-5),0.5,obsidian), #Obsidiana
    Cube((2.5,1,-5),0.5,obsidian), #Obsidiana
    
    Cube((4,1.5,-5),0.5,obsidian), #Obsidiana
    Cube((3.5,1.5,-5),0.5,obsidian), #Obsidiana
    Cube((3,1.5,-5),0.5,obsidian), #Obsidiana
    Cube((2.5,1.5,-5),0.5,obsidian), #Obsidiana
    
    Cube((3.5,-0.5,-5),0.5,portal), #Portal
    Cube((3,-0.5,-5),0.5,portal), #Portal
    Cube((3.5,0,-5),0.5,portal), #Portal
    Cube((3,0,-5),0.5,portal), #Portal
    Cube((3.5,0.5,-5),0.5,portal), #Portal
    Cube((3,0.5,-5),0.5,portal), #Portal
    Cube((3.5,1,-5),0.5,portal), #Portal
    Cube((3,1,-5),0.5,portal), #Portal
    
    
    #------------Casa--------------------- 
    Cube((-1.5,-0.5,-6),0.5,bwood), #pared   
    Cube((-1,-0.5,-6),0.5,bwood), #pared   
    Cube((-0.5,-0.5,-6),0.5,bwood), #pared
    Cube((0,-0.5,-6),0.5,bwood), #pared   
    Cube((1,-0.5,-6),0.5,bwood), #pared   
    
    
    Cube((-1.5,0,-6),0.5,bwood), #pared  
    Cube((-1,0,-6),0.5,mirror), #vidrio   
    Cube((-0.5,0,-6),0.5,bwood), #pared
    Cube((0,0,-6),0.5,bwood), #pared   
    Cube((1,0,-6),0.5,bwood), #pared  
    
    
    Cube((-1.5,0.5,-6),0.5,bwood), #pared   
    Cube((-1,0.5,-6),0.5,bwood), #pared   
    Cube((-0.5,0.5,-6),0.5,bwood), #pared
    Cube((0,0.5,-6),0.5,bwood), #pared   
    Cube((0.5,0.5,-6),0.5,bwood), #pared   
    Cube((1,0.5,-6),0.5,bwood), #pared 
    
    Cube((-1.5,1,-6),0.5,brick), #techo
    Cube((-1,1,-6),0.5,brick), #techo  
    Cube((-0.5,1,-6),0.5,brick), #techo
    Cube((0,1,-6),0.5,brick), #techo 
    Cube((0.5,1,-6),0.5,brick), #techo
    Cube((1,1,-6),0.5,brick), #techo
    
    
    Cube((-1,1.5,-6),0.5,brick), #techo
    Cube((-0.5,1.5,-6),0.5,brick), #techo
    Cube((0,1.5,-6),0.5,brick), #techo 
    Cube((0.5,1.5,-6),0.5,brick), #techo 
    
    Cube((-0.5,2,-6),0.5,brick), #techo
    Cube((0,2,-6),0.5,brick), #techo
    
    
    
    PlaneF(V3(0.5,-0.25,-6),0.5,1, door,1),
    PlaneF(V3(1,-1.7,-5.8),0.7,0.7, pato,1),
    PlaneH(V3(0,-1.9,-5),1.5,1.5, agua,1),

]#'''

r.render("Prueba")

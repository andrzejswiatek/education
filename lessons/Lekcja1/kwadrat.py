import turtle

def rysuj_kwadrat(dlugosc):
    #1
    turtle.forward(dlugosc)
    turtle.right(90)
    #2
    turtle.forward(dlugosc)
    turtle.right(90)
    #3
    turtle.forward(dlugosc)
    turtle.right(90)
    #4
    turtle.forward(dlugosc)
    turtle.right(90)

def rysuj_kwadrat2(dlugosc):
    for i in range(4):
        turtle.forward(dlugosc)
        turtle.right(90)
    
#rysuj_kwadrat(50)
#rysuj_kwadrat(100)
#rysuj_kwadrat(150)
#rysuj_kwadrat(200)

for i in range(100):        
    rysuj_kwadrat2(100+i*3)
         

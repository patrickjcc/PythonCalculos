import math
def main():
    #escribe tu código abajo de esta línea
    x1 = float(input('x1= '))
    y1 = float(input('y1= '))
    x2 = float(input('x2= '))
    y2 = float(input('y2= '))
    
    distancia = ((x2-x1)**2+(y2-y1)**2)**0.5
    
    print(f'distancia= {distancia:.2f}')

if __name__ == '__main__':
    main()

def main():
    #escribe tu código abajo de esta línea
    peso1=float(input('Dame el peso inicial: '))
    peso2=float(input('Dame el peso final: '))
    tiempo=int(input('Dame la cantidad de meses: '))
    
    print('Lo que debes bajar por mes es: '+str(float((peso1-peso2) /tiempo)))
if __name__ == '__main__':
    main()

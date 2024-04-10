def calcular_area_rectangulo(base, altura):
    area_rectangulo = base * altura
    return area_rectangulo

def calcular_area_triangulo(base, altura):
    area_triangulo = 0.5 * base * altura
    return area_triangulo

def main():
    #Area de rectangulo
    base_rectangulo = 4
    altura_rectangulo = 6
    area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
    print("El área del rectángulo es:", area_rectangulo)

    #Area de triangulo
    base_triangulo = 5
    altura_triangulo = 8
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print("El área del triángulo es:", area_triangulo)

main()

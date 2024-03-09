from math import pi, sqrt


def circleArea(radius: float) -> float:
   '''
    Функция определения площади круга по радиусу.
    В качестве аргумента передается радиус.
    '''
   
   if radius < 0:
       raise ValueError('Радиус не может быть отрицательным')
   return pi*(radius**2)


def triangleArea(a,b,c):
    '''
    Здесь реализован упрощенный вариант решения задания.
    Вводные данные - стороны треугольника.
    '''
    if (a + b > c) and (a + c > b) and (b+c > a):  
        if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a):
            print('Прямоугольный')
        p = (a+b+c)/2
        return sqrt(p * (p-a) * (p-b) * (p-c))
    else:
        raise ValueError('Данный треугольник не существует или является вырожденным')
    

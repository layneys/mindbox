'''
Так как не был уточнен формат вводимых данных для n-угольников я решил работать с координатами вершин. 

'''


from math import pi


def circleArea(radius: float) -> float:
   '''
    Функция определения площади круга по радиусу.
    В качестве аргумента передается радиус.
    '''
   
   if radius < 0:
       raise ValueError('Радиус не может быть отрицательным')
   return pi*(radius**2)


def shoelaceArea(vertices: list) -> float:
    '''
    Функция определения площади многоугольника 
    Используется формула площади Гаусса, соответственно многоугольник выпуклый и не самоперсекающийся.
    В качестве аргумента принимается список вида [[x1,y1],[x2,y2]...[xn,yn]],
    Где [xi,yi] - набор координат вершин.
    Проверку на то, является ли треугольник прямоугольным решил не реализовывать, т.к. она не имеет смысла.
    '''
    checkConvexity(vertices)
    det = list(vertices).copy()
    det.append(vertices[0])
    area = 0 
    for i in range(len(vertices)):
        area += det[i][0] * det[i+1][1] - det[i+1][0] * det[i][1] 
    return 0.5*abs(area)



'''
Далее дополнительно реализовано определение выпуклости многоугольника.
Используется определение постоянства знака векторного произведения соседствующих ребер. 
'''


def sign(number):
   
    if number > 0:
        return('positive')
    elif number == 0:
        return('zero')
    else:
        return('negative')
    

def checkConvexity(vertices: list[list[int]]):
   
    if len(set(tuple(i) for i in vertices)) != len(vertices):
        raise ValueError('Некорректно введен массив')

    coords = vertices.copy()
    coords.append(coords[0])
    coords.append(coords[1])
    for i in range(len(coords)-2):
      
        cross = (coords[i+1][0] - coords[i][0]) * (coords[i+2][1] - coords[i+1][1]) - (coords[i+1][1] - coords[i][1]) * (coords[i+2][0] - coords[i+1][0])
        current_sign = sign(cross)
        if i == 0: 
            previous_sign = current_sign
        elif previous_sign == current_sign:
            previous_sign = current_sign
        else: 
           raise ValueError('Многоугольник не выпуклый')


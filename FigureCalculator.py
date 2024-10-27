#Программа не высчитывает пересечения и объединения фигур
#Требуются библиотеки PySimpleGUI и matplotlib
counterx = 400
countery = 0
import math
def schyot(x1, y1, x2, y2, x3, y3, x4, y4):
#Любую фигуру можно представить в виде прямоугольников и треугольников
#Выделим основной прямоугольник
    x11 = min(x1, x2, x3, x4)
    x12 = max(x1, x2, x3, x4)
    y11 = min(y1, y2, y3, y4)
    y12 = max(y1, y2, y3, y4)
#Найдём его площадь
    S = abs((x12-x11)*(y12-y11))
#При каждой из сторон фигуры выделим прямоугольные треугольники
    h1 = abs(y2 - y1)
    a1 = abs(x2 - x1)
    h2 = abs(y2 - y3)
    a2 = abs(x3 - x2)
    h3 = abs(y3 - y4)
    a3 = abs(x3 - x4)
    h4 = abs(y1 - y4)
    a4 = abs(x4 - x1)
#Следом найдём их площадь
    S1 = (1/2)*(a1*h1)
    S2 = (1/2)*(a2*h2)
    S3 = (1/2)*(a3*h3)
    S4 = (1/2)*(a4*h4)
#Выделяем и считаем частные случаи
    if y1 < y2 < y3 and x1 < x2 < x3:
        z1 = x1 - x2
        w1 = y3 - y2
        S1d = abs(z1*w1)
    else:
        S1d = 0
    if y2 < y3 < y1 and x1 < x2 < x3:
        z2 = x3 - x2
        w2 = y3 - y1
        S2d = abs(z2*w2)
    else:
        S2d = 0
    if x3 < x4 < x2 and y2 > y3 > y4:
        z3 = x2 - x4
        w3 = y3 - y4
        S3d = abs(z3*w3)
    else:
        S3d = 0
    if y4 > y1 > y3 and x1 < x4 < x3:
        z4 = x4 - x1
        w4 = y1 - y11
        S4d = abs(z4*w4)
    else:
        S4d = 0
    if y2 < y1 < y3 and x1 < x2 < x3:
        z2s = x2 - x1
        w2s = y3 - y1
        S2s = abs(z2s*w2s)
    else:
        S2s = 0
    if x3 < x2 < x4 and y2 > y3 > y4:
        z3s = x4 - x2
        w3s = y2 - y3
        S3s = abs(z3s*w3s)
    else:
        S3s = 0
    if y4 > y3 > y1 and x1 < x4 < x3:
        z4s = x3 - x4
        w4s = y3 - y1
        S4s = abs(z4s*w4s)
    else:
        S4s = 0
    if y1 < y12 > y2:
        s1 = abs((y12 - max(y2, y1))*(x1 - x2))
    else:
        s1 = 0
    if y2 < y12 > y3:
        s2 = abs((y12 - max(y2, y3))*(x3 - x2))
        if y2 > y1:
            s2 += abs((x11 - x2)*(y12 - y3))
    else:
        s2 = 0
    if x2 < x12 > x3:
        s3 = abs((x12 - max(x3, x2))*(y2 - y3))
    else:
        s3 = 0
    if y3 > y11 < y4:
        s4 = abs((min(y3, y4) - y11)*(x3 - x4))
    else:
        s4 = 0
    if y4 > y11 < y1:
        s5 = abs((min(y4, y1) - y11)*(x4 - x1))
    else:
        s5 = 0
#Находим площадь и периметр искомого четырёхугольника
    A1 = math.sqrt(a1**2 + h1**2)
    A2 = math.sqrt(a2**2 + h2**2)
    A3 = math.sqrt(a3**2 + h3**2)
    A4 = math.sqrt(a4**2 + h4**2)
    Pfigure = A1 + A2 + A3 + A4
    if x1 == x2 and y1 == y2:
        if x3 == x4 and y3 == y4:
            Pfigure /= 2
    if x3 == x2 and y3 == y2:
        if x1 == x4 and y1 == y4:
            Pfigure /= 2
    Sfigure = abs(S - S1 - S2 - S3 - S4 - S1d - S2d - S3d - S4d - S2s - S3s - S4s - s2 - s3 - s4 - s5)
    return Sfigure, Pfigure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')
sg.theme('DarkAmber')
fig = matplotlib.figure.Figure(figsize=(4, 3), dpi=100)

def draw_figure(canvas, figure):
   tkcanvas = FigureCanvasTkAgg(figure, canvas)
   tkcanvas.draw()
   tkcanvas.get_tk_widget().pack(side='top', fill='both', expand=1)
   return tkcanvas

def graphics1():
#После нажатия на кнопку запуска выволится окно с вводом данных
    layout1 = [[sg.Text('Пожалуйста, не закрывайте это окно во время работы. Это приведёт к остановке программы.', size=(100, 1), key='-text-', font='Helvetica 16')],
              [sg.Text('Введите упорядоченные относительные координаты углов (первая вершина левая нижняя, обход по часовой стрелке):', size=(100, 1), key='-text-', font='Helvetica 16')], 
              [sg.Text('x1', size=(15,1), key='-text-', font='Helvetica 16')], [sg.Input(key='-x1-', do_not_clear=True)],
              [sg.Text('y1', size=(15,1), key='-text-', font='Helvetica 16')], [sg.Input(key='-y1-', do_not_clear=True)],
              [sg.Text('x2', size=(15,1), key='-text-', font='Helvetica 16')], [sg.Input(key='-x2-', do_not_clear=True)],
              [sg.Text('y2', size=(15,1), key='-text-', font='Helvetica 16')], [sg.Input(key='-y2-', do_not_clear=True)],
              [sg.Text('x3', size=(15,1), key='-text-', font='Helvetica 16')], [sg.Input(key='-x3-', do_not_clear=True)],
              [sg.Text('y3', size=(15,1), key='-text-', font='Helvetica 16')], [sg.Input(key='-y3-', do_not_clear=True)],
              [sg.Text('x4', size=(15,1), key='-text-', font='Helvetica 16')], [sg.Input(key='-x4-', do_not_clear=True)],
              [sg.Text('y4', size=(15,1), key='-text-', font='Helvetica 16')], [sg.Input(key='-y4-', do_not_clear=True)],
              [sg.Button('Рассчитать', enable_events=True, key='-G-', font='Helvetica 16')]],
    window1 = sg.Window('Ввод', layout1, size=(1440,720), location=(475, 290))
    event, values = window1.read()
    
    if event == '-G-':
#Выносим данные из ячеек ввода
        x1 = float(values['-x1-'])
        y1 = float(values['-y1-'])
        x2 = float(values['-x2-'])
        y2 = float(values['-y2-'])
        x3 = float(values['-x3-'])
        y3 = float(values['-y3-'])
        x4 = float(values['-x4-'])
        y4 = float(values['-y4-'])
        window1.close()
    return x1, x2, x3, x4, y1, y2, y3, y4

def graphics2(Sfigure, Pfigure, counterx, countery):
#Выводим результат счёта на экран
    layout3 = [[sg.Text('Площадь новой фигуры равна:', size = (30,1), key = '-text-', font = 'Helvetica 16')],
              [sg.Text(Sfigure, size = (30,1), key = '-text-', font = 'Helvetica 16')],
              [sg.Text('Периметр новой фигуры равен:', size = (30,1), key = '-text-', font = 'Helvetica 16')],
              [sg.Text(Pfigure, size = (30,1), key = '-text-', font = 'Helvetica 16')],
              [sg.Button('Добавить фигуру', enable_events=True, key='-QW-', font='Helvetica 16')], 
              [sg.Canvas(key='-CANVAS-')]]
    window3 = sg.Window('Результат', layout3, size=(400, 500), location=(counterx, countery), finalize=True)
    tkcanvas = draw_figure(window3['-CANVAS-'].TKCanvas, fig)
    event, values = window3.read()
    
#Создаём кнопку запуска программы
layout = [[sg.Text('Функции программы:', size = (30,1), key = '-text-', font = 'Helvetica 16')],
          [sg.Text('Программа расчитана на создание четырёхугольников разных форм и рассчёт их площадей и периметров, однако с её помощью можно создавать много чего ещё:', size = (30,5), key = '-text-', font = 'Helvetica 16')],
          [sg.Text('1. Чтобы добавить многоугольник, отличный от четырёхугольника, представьте его в виде нескольких четырёхугольников с общей стороной.', size = (30,5), key = '-text-', font = 'Helvetica 16')],
          [sg.Text('2. Чтобы найти площадь и периметр объединения или пересечения, представьте объединение или пересечение в виде многоугольника и действуйте по аналогии с п. 1. Чтобы найти координаты пересечений фигур, наведите на пересечения фигур курсором мыши на окне с чертежом.', size = (30,9), key = '-text-', font = 'Helvetica 16')],
          [sg.Text('3. Чтобы создать треугольник, представьте его в виде четырёхугольника с 1 развёрнутым углом (Углом равным 180 градусам).', size = (30,5), key = '-text-', font = 'Helvetica 16')],
          [sg.Button('Старт программы', enable_events=True, key='-FUNCTION-', font='Helvetica 16')]],
window = sg.Window('Старт', layout, size=(400,700))
event, values = window.read()
while True:
#Если закрыть окно с этой кнопкой, программа прекратит работу
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
#Производим процедуру счёта
    if event == '-FUNCTION-':
        window.close()
        x1, x2, x3, x4, y1, y2, y3, y4 = graphics1()
        Sfigure, Pfigure = schyot(x1, y1, x2, y2, x3, y3, x4, y4)
#Создаём визуализацию фигуры
        x1p = [x1, x2, x3, x4, x1]
        y1p = [y1, y2, y3, y4, y1]
        plot = plt.plot(x1, y1)
        fig.add_subplot(111).plot(x1p, y1p)
#Выводим площадь фигуры и её визуализацию
        layout2 = [[sg.Text('Площадь фигуры равна:', size = (30,1), key = '-text-', font = 'Helvetica 16')],
                  [sg.Text(float(Sfigure), size = (30,1), key = '-text-', font = 'Helvetica 16')],
                  [sg.Text('Периметр фигуры равен:', size = (30,1), key = '-text-', font = 'Helvetica 16')],
                  [sg.Text(float(Pfigure), size = (30,1), key = '-text-', font = 'Helvetica 16')],
                  [sg.Button('Добавить фигуру', enable_events=True, key='-Z-', font='Helvetica 16')],
                  [sg.Canvas(key='-CANVAS-')]],
        window2 = sg.Window('Результат', layout2, size=(400, 500), location=(0, 0), finalize=True)
        tkcanvas = draw_figure(window2['-CANVAS-'].TKCanvas, fig)
        event, values = window2.read()
#Введение новой фигуры
    if event == '-Z-':
        while True:
            x1, x2, x3, x4, y1, y2, y3, y4 = graphics1()
            Sfigure, Pfigure = schyot(x1, y1, x2, y2, x3, y3, x4, y4)
            fig = matplotlib.figure.Figure(figsize=(4, 3), dpi=100)
            fig.add_subplot(111).plot(x1p, y1p, '--', [x1, x2, x3, x4, x1], [y1, y2, y3, y4, y1])
            x1p += [x1, x2, x3, x4, x1]
            y1p += [y1, y2, y3, y4, y1]
            graphics2(Sfigure, Pfigure, counterx, countery)
            counterx += 400
            if counterx == 2000:
                counterx = 0
                countery = 500
            if countery == 500 and counterx == 2000:
                countery = 0

# Требуются библиотеки PySimpleGUI и matplotlib
counterx, countery, i, j, h = 400, 0, 4, 2, 1
ev1 = None
fontn = 'Helvetica'
color1 = ':k'
color2 = '-b'
import math
def schyot(x1, y1, x2, y2, x3, y3, x4, y4):
# Любую фигуру можно представить в виде прямоугольников и треугольников
# Выделим основной прямоугольник
    x11 = min(x1, x2, x3, x4)
    x12 = max(x1, x2, x3, x4)
    y11 = min(y1, y2, y3, y4)
    y12 = max(y1, y2, y3, y4)
# Найдём его площадь
    S = abs((x12-x11)*(y12-y11))
# При каждой из сторон фигуры выделим прямоугольные треугольники
    h1 = abs(y1 - y2)
    a1 = abs(x1 - x2)
    h2 = abs(y2 - y3)
    a2 = abs(x2 - x3)
    h3 = abs(y3 - y4)
    a3 = abs(x3 - x4)
    h4 = abs(y4 - y1)
    a4 = abs(x4 - x1)
# Следом вычтем их площадь из площади основного прямоугольника
    S -= (1/2)*(a1*h1)
    S -= (1/2)*(a2*h2)
    S -= (1/2)*(a3*h3)
    S -= (1/2)*(a4*h4)
# Выделяем и считаем частные случаи
    if y1 < y2 < y3 and x1 < x2 < x3:
        z1 = x1 - x2
        w1 = y3 - y2
        S -= abs(z1*w1)
    if y4 < y3 < y2 and x2 < x3 < x4:
        z1 = x2 - x3
        w1 = y2 - y3
        S -= abs(z1*w1)
    if y1 < y4 < y3 and x1 < x4 < x3:
        z1 = x4 - x12
        w1 = y11 - y4
        S -= abs(z1*w1)
    if y2 < y3 < y1 and x1 < x2 < x3:
        z2 = x3 - x2
        w2 = y3 - y1
        S -= abs(z2*w2)
    if x3 < x4 < x2 and y2 > y3 > y4:
        z3 = x2 - x4
        w3 = y3 - y4
        S -= abs(z3*w3)
    if y4 > y1 > y3 and x1 < x4 < x3:
        z4 = x4 - x1
        w4 = y1 - y11
        S -= abs(z4*w4)
    if y2 < y1 < y3 and x1 < x2 < x3:
        z2s = x2 - x1
        w2s = y3 - y1
        S -= abs(z2s*w2s)
    if x3 < x2 < x4 and y2 > y3 > y4:
        z3s = x4 - x2
        w3s = y2 - y3
        S -= abs(z3s*w3s)
    if y4 > y3 > y1 and x1 < x4 < x3:
        z4s = x3 - x4
        w4s = y3 - y1
        S -= abs(z4s*w4s)
    if y2 < y12 > y3:
        S -= abs((y12 - max(y2, y3))*(x3 - x2))
    if y4 > y11 < y1:
        S -= abs((min(y4, y1) - y11)*(x4 - x1))
    if y1 < y2 < y3 < y4 and x1 < x2 < x3 < x4:
        S -= abs((x2 - x1)*(y4 - y3))
    if y1 < y4 < y3 < y2 and x1 < x4 < x3 < x2:
        S -= abs((x2 - x3)*(y4 - y1))
    if y1 > y4 > y3 > y2 and x1 < x4 < x3 < x2:
        S -= abs((x4 - x1)*(y3 - y2))
    if y1 > y2 > y3 > y4 and x1 < x2 < x3 < x4:
        S -= abs((x4 - x3)*(y1 - y2))
# Находим периметр искомого четырёхугольника
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
    Sfigure = abs(S)
    return Sfigure, Pfigure

def change_theme(themen):
    sg.theme(themen)
    
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
matplotlib.use('TkAgg')
themen = 'DarkAmber'
change_theme(themen)
fig = matplotlib.figure.Figure(figsize=(4, 3), dpi=100)

def draw_figure(canvas, figure):
   tkcanvas = FigureCanvasTkAgg(figure, canvas)
   tkcanvas.draw()
   tkcanvas.get_tk_widget().pack(side='top', fill='both', expand=1)
   return tkcanvas

def graphics1(fontn, color1, color2, ev1):
    ev1 = None
# После нажатия на кнопку запуска выволится окно с вводом данных
    layout1 = [[sg.Text('Введите упорядоченные относительные координаты углов (первая вершина левая нижняя, обход по часовой стрелке):', size=(100, 1), key='-text-', font=(fontn, 16))], 
              [sg.Text('x1', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-x1-', do_not_clear=True)],
              [sg.Text('y1', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-y1-', do_not_clear=True)],
              [sg.Text('x2', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-x2-', do_not_clear=True)],
              [sg.Text('y2', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-y2-', do_not_clear=True)],
              [sg.Text('x3', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-x3-', do_not_clear=True)],
              [sg.Text('y3', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-y3-', do_not_clear=True)],
              [sg.Text('x4', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-x4-', do_not_clear=True)],
              [sg.Text('y4', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-y4-', do_not_clear=True)],
              [sg.Button('Рассчитать', enable_events=True, key='-G-', font=(fontn, 16))],
              [sg.Button('Настройки', enable_events=True, key='-Settings-', font=(fontn, 16))]],
    window1 = sg.Window('Ввод', layout1, size=(1440,720), location=(475, 290))
    event, values = window1.read()
    # Выносим данные из ячеек ввода
    x1 = float(values['-x1-'])
    y1 = float(values['-y1-'])
    x2 = float(values['-x2-'])
    y2 = float(values['-y2-'])
    x3 = float(values['-x3-'])
    y3 = float(values['-y3-'])
    x4 = float(values['-x4-'])
    y4 = float(values['-y4-'])
    if event == '-Settings-':
        ev1 = 1
        fontn, color1, color2, event = settings(event, window1, fontn, color1, color2)
    if event == '-G-':
        window1.close()
    return x1, x2, x3, x4, y1, y2, y3, y4, event, fontn, color1, color2, ev1

def graphics12(x1p, y1p, x2p, y2p, fontn, color1, color2, ev1):
# После нажатия на кнопку запуска выволится окно с вводом данных
    ev1 = None
    layout1 = [[sg.Text('Введите упорядоченные относительные координаты углов (первая вершина левая нижняя, обход по часовой стрелке):', size=(100, 1), key='-text-', font=(fontn, 16))], 
              [sg.Text('x1', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-x1-', do_not_clear=True)],
              [sg.Text('y1', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-y1-', do_not_clear=True)],
              [sg.Text('x2', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-x2-', do_not_clear=True)],
              [sg.Text('y2', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-y2-', do_not_clear=True)],
              [sg.Text('x3', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-x3-', do_not_clear=True)],
              [sg.Text('y3', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-y3-', do_not_clear=True)],
              [sg.Text('x4', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-x4-', do_not_clear=True)],
              [sg.Text('y4', size=(15,1), key='-text-', font=(fontn, 16))], [sg.Input('0', key='-y4-', do_not_clear=True)],
              [sg.Button('Рассчитать', enable_events=True, key='-G-', font=(fontn, 16))],
              [sg.Button('Настройки', enable_events=True, key='-Settings-', font=(fontn, 16))],
              [sg.Button('Показать имеющиеся фигуры', enable_events=True, key='-SHOWPLOT-', font=(fontn, 16))]],
    window1 = sg.Window('Ввод', layout1, size=(1440,720), location=(475, 290))
    event, values = window1.read()
    # Выносим данные из ячеек ввода
    x1 = float(values['-x1-'])
    y1 = float(values['-y1-'])
    x2 = float(values['-x2-'])
    y2 = float(values['-y2-'])
    x3 = float(values['-x3-'])
    y3 = float(values['-y3-'])
    x4 = float(values['-x4-'])
    y4 = float(values['-y4-'])
    if event == '-Settings-':
        ev1 = 1
        fontn, color1, color2, event = settings(event, window1, fontn, color1, color2)
        # Создаём визуализацию всех фигур сразу
    if event == '-SHOWPLOT-':
        window1.close()
        plot1 = plt.plot(x1p, y1p, color2, x2p, y2p, '-w', x2p, y2p, '-w', x2p, y2p, '-w', x2p, y2p, '-w', x2p, y2p, '-w', [x1, x2, x3, x4, x1], [y1, y2, y3, y4, y1], color2)
        plt.grid()
        plt.show()
    window1.close()
    return x1, x2, x3, x4, y1, y2, y3, y4, event, fontn, color1, color2, ev1

def graphics2(Sfigure, Pfigure, counterx, countery, fontn):
# Выводим результат счёта на экран
    layout3 = [[sg.Text('Площадь новой фигуры равна:', size = (30,1), key = '-text-', font = (fontn, 16))],
              [sg.Text(Sfigure, size = (30,1), key = '-text-', font = (fontn, 16))],
              [sg.Text('Периметр новой фигуры равен:', size = (30,1), key = '-text-', font = (fontn, 16))],
              [sg.Text(Pfigure, size = (30,1), key = '-text-', font = (fontn, 16))],
              [sg.Button('Добавить фигуру', enable_events=True, key='-QW-', font=(fontn, 16))], 
              [sg.Canvas(key='-CANVAS-')]]
    window3 = sg.Window('Результат', layout3, size=(400, 500), location=(counterx, countery), finalize=True)
    tkcanvas = draw_figure(window3['-CANVAS-'].TKCanvas, fig)
    event, values = window3.read()
    
# Создаём кнопку запуска программы
def start(fontn):
    layout = [[sg.Text('Функции программы:', size = (30,1), key = '-text-', font = (fontn, 16))],
              [sg.Text('Программа расчитана на создание четырёхугольников разных форм и рассчёт их площадей и периметров, однако с её помощью можно создавать много чего ещё:', size = (30,5), key = '-text-', font = (fontn, 16))],
              [sg.Text('1. Чтобы создать многоугольник, отличный от четырёхугольника, представьте его в виде нескольких четырёхугольников с общей стороной.', size = (30,5), key = '-text-', font = (fontn, 16))],
              [sg.Text('2. Чтобы найти площадь и периметр объединения или пересечения, представьте объединение или пересечение в виде многоугольника и действуйте по аналогии с п. 1.', size = (30,5), key = '-text-', font = (fontn, 16))],
              [sg.Text('3. Чтобы создать треугольник, представьте его в виде четырёхугольника с 1 развёрнутым углом (Углом равным 180 градусам).', size = (30,5), key = '-text-', font = (fontn, 16))],
              [sg.Button('Настройки', enable_events=True, key='-Settings-', font=(fontn, 16))],
              [sg.Button('Старт программы', enable_events=True, key='-FUNCTION-', font=(fontn, 16))]],
    window = sg.Window('Старт', layout, size=(400,750))
    event, values = window.read()
    return event, window

def settings(event, window, fontn, color1, color2):
    window.close()
    if event == '-Settings-':
        layoutsett = [[sg.Button('Настройки цветов интерфейса', enable_events=True, key='-ISettings-', font=(fontn, 16))],
                      [sg.Button('Настройки текста', enable_events=True, key='-TSettings-', font=(fontn, 16))],
                      [sg.Button('Настройки изображения фигур', enable_events=True, key='-PSettings-', font=(fontn, 16))]]
        windowsett = sg.Window('Настройки', layoutsett, size=(400,150))
        event, values = windowsett.read()
        if event == '-ISettings-':
            windowsett.close()
            windowsetti = sg.Window('Настройки', [[sg.Combo(sg.theme_list(), readonly=True, k='-THEME LIST-'), sg.OK(), sg.Cancel()]], size=(400,100))
            event, values = windowsetti.read()
            if event == 'OK':
                themen = values['-THEME LIST-']
                change_theme(themen)
            windowsetti.close()
        if event == '-TSettings-':
            windowsett.close()
            windowsettt = sg.Window('Настройки', [[sg.Combo(sg.Text.fonts_installed_list() + ['По умолчанию'], readonly=True, k='-FONT LIST-'), sg.OK(), sg.Cancel()]], size=(400,100))
            event, values = windowsettt.read()
            if event == 'OK':
                fontn = values['-FONT LIST-']
                if fontn == 'По умолчанию':
                    fontn = 'Helvetica 16'
            windowsettt.close()
        if event == '-PSettings-':
            windowsett.close()
            layoutplot = [[sg.Text('Цвет предыдущих фигур', size = (30,1), key = '-text-', font = (fontn, 16))],
                          [sg.Combo(['Синий', 'Зелёный', 'Красный', 'Зеленовато-голубой', 'Пурпурный', 'Салатовый', 'Чёрный'], readonly=True, k='-COLOR LIST1-')],
                          [sg.Text('Вид линии предыдущих фигур', size = (30,1), key = '-text-', font = (fontn, 16))],
                          [sg.Combo(['Сплошная', 'Отрезок с запятой', 'Пунктир'], readonly=True, k='-LINE LIST1-')],
                          [sg.Text('Цвет новой фигуры', size = (30,1), key = '-text-', font = (fontn, 16))],
                          [sg.Combo(['Синий', 'Зелёный', 'Красный', 'Зеленовато-голубой', 'Пурпурный', 'Салатовый', 'Чёрный'], readonly=True, k='-COLOR LIST2-')],
                          [sg.Text('Вид линии новой фигуры', size = (30,1), key = '-text-', font = (fontn, 16))],
                          [sg.Combo(['Сплошная', 'Отрезок с запятой', 'Пунктир'], readonly=True, k='-LINE LIST2-')],
                          [sg.OK(), sg.Cancel()]]
            windowsettp = sg.Window('Настройки', layoutplot, size=(400,330))
            event, values = windowsettp.read()
            if event == 'OK':
                if values['-COLOR LIST1-'] == 'Синий':
                    color1 = 'b'
                if values['-COLOR LIST1-'] == 'Зелёный':
                    color1 = 'g'
                if values['-COLOR LIST1-'] == 'Красный':
                    color1 = 'r'
                if values['-COLOR LIST1-'] == 'Зеленовато-голубой':
                    color1 = 'c'
                if values['-COLOR LIST1-'] == 'Пурпурный':
                    color1 = 'm'
                if values['-COLOR LIST1-'] == 'Салатовый':
                    color1 = 'y'
                if values['-COLOR LIST1-'] == 'Чёрный':
                    color1 = 'k'
                if values['-LINE LIST1-'] == 'Сплошная':
                    color1 += '-'
                if values['-LINE LIST1-'] == 'Отрезок с запятой':
                    color1 += '-.'
                if values['-LINE LIST1-'] == 'Пунктир':
                    color1 += '--'
                if values['-COLOR LIST2-'] == 'Синий':
                    color2 = 'b'
                if values['-COLOR LIST2-'] == 'Зелёный':
                    color2 = 'g'
                if values['-COLOR LIST2-'] == 'Красный':
                    color2 = 'r'
                if values['-COLOR LIST2-'] == 'Зеленовато-голубой':
                    color2 = 'c'
                if values['-COLOR LIST2-'] == 'Пурпурный':
                    color2 = 'm'
                if values['-COLOR LIST2-'] == 'Салатовый':
                    color2 = 'y'
                if values['-COLOR LIST2-'] == 'Чёрный':
                    color2 = 'k'
                if values['-LINE LIST2-'] == 'Сплошная':
                    color2 += '-'
                if values['-LINE LIST2-'] == 'Отрезок с запятой':
                    color2 += '-.'
                if values['-LINE LIST2-'] == 'Пунктир':
                    color2 += '--'
            windowsettp.close()
    return fontn, color1, color2, event

event, window = start(fontn)
while event != '-FUNCTION-':
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    fontn, color1, color2, event = settings(event, window, fontn, color1, color2)
    event, window = start(fontn)
while True:
# Если закрыть окно с этой кнопкой, программа прекратит работу
# Производим процедуру счёта
    if event == '-FUNCTION-':
        window.close()
        x1, x2, x3, x4, y1, y2, y3, y4, event, fontn, color1, color2, ev1 = graphics1(fontn, color1, color2, ev1)
        while event != '-G-':
            if ev1 == 1:
                x1, x2, x3, x4, y1, y2, y3, y4, event, fontn, color1, color2, ev1 = graphics1(fontn, color1, color2, ev1)
            if event == '-G-':
                break
        Sfigure, Pfigure = schyot(x1, y1, x2, y2, x3, y3, x4, y4)
# Создаём визуализацию фигуры
        x1p = [x1, x2, x3, x4, x1]
        y1p = [y1, y2, y3, y4, y1]
        fig.add_subplot(111).plot(x1p, y1p, color2)
        x2p = [x1]
        y2p = [y1]
# Выводим площадь фигуры и её визуализацию
        layout2 = [[sg.Text('Площадь фигуры равна:', size = (30,1), key = '-text-', font = (fontn, 16))],
                  [sg.Text(float(Sfigure), size = (30,1), key = '-text-', font = (fontn, 16))],
                  [sg.Text('Периметр фигуры равен:', size = (30,1), key = '-text-', font = (fontn, 16))],
                  [sg.Text(float(Pfigure), size = (30,1), key = '-text-', font = (fontn, 16))],
                  [sg.Button('Добавить фигуру', enable_events=True, key='-Z-', font=(fontn, 16))],
                  [sg.Canvas(key='-CANVAS-')]],
        window2 = sg.Window('Результат', layout2, size=(400, 500), location=(0, 0), finalize=True)
        tkcanvas = draw_figure(window2['-CANVAS-'].TKCanvas, fig)
        event, values = window2.read()
# Введение новой фигуры
    if event == '-Z-':
        while True:
            exc = 0
            x1, x2, x3, x4, y1, y2, y3, y4, event, fontn, color1, color2, ev1 = graphics12(x1p, y1p, x2p, y2p, fontn, color1, color2, ev1)
            while event != '-G-':
                if event == '-SHOWPLOT-':
                    x1, x2, x3, x4, y1, y2, y3, y4, event, fontn, color1, color2, ev1 = graphics12(x1p, y1p, x2p, y2p, fontn, color1, color2, ev1)
                if ev1 == 1:
                    x1, x2, x3, x4, y1, y2, y3, y4, event, fontn, color1, color2, ev1 = graphics12(x1p, y1p, x2p, y2p, fontn, color1, color2, ev1)    
                if event == '-G-':
                    break
            Sfigure, Pfigure = schyot(x1, y1, x2, y2, x3, y3, x4, y4)
            fig = matplotlib.figure.Figure(figsize=(4, 3), dpi=100)
            fig.add_subplot(111).plot(x1p, y1p, color1, x2p, y2p, '-w', x2p, y2p, '-w', x2p, y2p, '-w', x2p, y2p, '-w', x2p, y2p, '-w', [x1, x2, x3, x4, x1], [y1, y2, y3, y4, y1], color2)
            x1p += [x1, x2, x3, x4, x1]
            y1p += [y1, y2, y3, y4, y1]
            graphics2(Sfigure, Pfigure, counterx, countery, fontn)
            # Изменим местоположение окон, чтобы от части избежать наложения
            counterx += 400
            if counterx == 2000:
                counterx = 0
                countery = 500
            if countery == 500 and counterx == 2000:
                countery = 0
            # Избавимся от связок между двумя фигурами
            if x1p[i] == x1p[i + 2] and y1p[i] == y1p[i + 2]:
                exc += 0
            else:
                exc += 1
                
            if x1p[j] == x1p[j + 4] and y1p[j] == y1p[j + 4]:
                exc += 0
            else:
                exc += 1

            if x1p[h] == x1p[h + 6] and y1p[h] == y1p[h + 6]:
                exc += 0
            else:
                exc += 1

            if x1p[h] == x1p[i + 5] and y1p[h] == y1p[i + 5]:
                exc += 0
            else:
                exc += 1

            if exc == 4:
                x2p += [x1]
                y2p += [y1]
                
            i += 5
            j += 5
            h += 5

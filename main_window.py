from PySide6.QtWidgets import QMainWindow
from ui_main_window import Ui_MainWindow

import numpy as np
import math
import random
import matplotlib.pyplot as plt

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Биофотоника. Задание 1. Футин Даниил")

        self.app = app

        self.perform_pushButton.clicked.connect(self.perform)
        self.reset_pushButton.clicked.connect(self.reset)

        self.reset()

    def perform(self):
        # Чистим графики
        self.distribution_graph.canvas.ax.clear()
        self.density_graph.canvas.ax.clear()

        # Исходные данные:
        # Количество фотонов
        N = self.photons_quantity_spinBox.value()
        # Радиус пучка
        a = self.beam_radius_doubleSpinBox.value()
        
        # Вычисляем количество бинов по правилу Стёрджеса
        bins_number = 1 + math.floor(math.log2(N))

        # счётчик для цикла
        i = 0
        # Переменная для нахождения максимального радиуса из тех, которые мы получим
        rmax = 0
        # Тут храним все радиусы, которые получим
        radiuses = list()

        while(i < N):
            # Получаем очередной радиус r
            r = self.calculate_radius(a)
            # Добавляем его в наш список
            radiuses.append(r)
            if (r > rmax):
                rmax = r
            # Получаем очередной угол phi
            phi = self.angle()
            # Переводим координаты полученной точки в Декартову систему координат
            coordinates = self.cartesian(r, phi)

            #Ставим точку на координатной плоскости
            self.distribution_graph.canvas.ax.scatter(coordinates[0], coordinates[1], marker = ".")
            i += 1
        
        # Рисуем окружности
        for i in range(0, bins_number):
            self.distribution_graph.canvas.ax.add_artist(plt.Circle((0,0), ( (1 + i) / bins_number ) * rmax, fill = False))

        # Сортируем список радиусов
        radiuses.sort()

        # Формируем края бинов
        edges = np.arange(0, rmax + 0.01, rmax/bins_number)

        # Создаем массив, в котором будут храниться подсчёты количества радиусов, попавших в i-ое кольцо
        counts = np.zeros(bins_number)

        # счётчик для цикла
        i = 1
        # Распределяем смоделированные радиусы в бины
        for r in radiuses:
            while(r > edges[i]):
                i += 1
            counts[i-1] += 1  
        
        # Делим количество точек, лежащих в кольце на площадь кольца и количество фотонов N
        for i in range(0, len(counts), 1):
            counts[i] /= N * ((edges[i+1])**2 - (edges[i])**2) * math.pi
        
        # Строим гистограмму по данным, которые мы получили
        self.density_graph.canvas.ax.stairs(counts, edges)

        # Создаем массив точек, в которых будем вычислять нормированную плотность вероятности
        r_axis = np.arange(0, rmax, rmax * 0.01)    
        # Строим график аналитической кривой нормированной плотности вероятности
        density_data = list()
        for r_i in r_axis:
            density_data.append(self.normalized_density(r_i, a))
        self.density_graph.canvas.ax.plot(r_axis, density_data)

        # Выводим изменения
        self.distribution_graph.canvas.draw()
        self.density_graph.canvas.draw()
    
    """
    Метод для очищение графиков и установки значений по умолчанию для количества фотонов N
    и радиуса пучка a
    """        
    def reset(self):
        self.distribution_graph.canvas.ax.clear()
        self.density_graph.canvas.ax.clear()

        self.photons_quantity_spinBox.setValue(1000)
        self.beam_radius_doubleSpinBox.setValue(1.0)

        self.distribution_graph.canvas.draw()
        self.density_graph.canvas.draw()

    """
    Генерируем равномерно распределённую случайную величину F в полуинтервале [0,1)
    и подставляем её в формулу для радиуса, которую мы получили.
    """
    def calculate_radius(self, a: float):
        F = random.uniform(0, 1)
        return a * math.sqrt((-2) * math.log(F))
    
    """
    Генерируем равномерно распределённую случайную величину phi в полуинтервале [0, 2*pi).
    Это и будет наш угол в полярных координатах.
    """
    def angle(self):
        return random.uniform(0, 2 * math.pi)
    """
    Переводим координаты нашей точки в полярных координатах в Декартовы координаты.
    """
    def cartesian(self, r: float, phi: float):
        return [r * math.cos(phi), r * math.sin(phi)]
    
    """
    Метод для вывода аналитической кривой нормированной плотности вероятности
    """
    def normalized_density(self, r: float, a: float):
        return ( 1 / (2 * math.pi * (a**2)) ) *  math.exp(-((r / (math.sqrt(2) * a))**2))


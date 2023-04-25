from PySide6.QtWidgets import QMainWindow
from ui_main_window import Ui_MainWindow

import numpy as np
import math
import random


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
        
        # счётчик для цикла
        i = 0

        # Переменная для нахождения максимального радиуса из тех, которые мы получим
        rmax = 0
        # Тут храним все радиусы, которые получим
        radiuses = list()

        while(i < N):
            # Получаем очередной радиус r
            r = self.calculate_radius(a)
            # Добавляем его в наш лист
            radiuses.append(r)
            if (r > rmax):
                rmax = r
            # Получаем очередной угол phi
            phi = self.angle()
            # Переводим координаты полученной точки в Декартову систему координат
            coordinates = self.cartesian(r, phi)

            #Ставим точку на координатной плоскости
            self.distribution_graph.canvas.ax.scatter(coordinates[0], coordinates[1])
            i += 1
        
        r_axis = np.arange(0, rmax, rmax * 0.01)
        
        # Строим график аналитической кривой нормированной плотности вероятности
        density_data = list()
        for r_i in r_axis:
            density_data.append(self.normalized_density(r_i, a))
        
        self.density_graph.canvas.ax.plot(r_axis, density_data)
        # Строим гистограмму по данным, которые мы получили
        self.density_graph.canvas.ax.hist(radiuses, 100, density = True, stacked = True)
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
        return (1/(a**2)) * r * math.exp(-(r / (math.sqrt(2) * a))**2)


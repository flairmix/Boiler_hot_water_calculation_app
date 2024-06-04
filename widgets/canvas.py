
from PySide6 import QtWidgets

from matplotlib.figure import Figure
from matplotlib import rcParams
import matplotlib.style as mplstyle
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from boiler_hours import *
from app import boiler_inputs



class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=24, height=10, dpi=100, hours=24, boiler=Boiler(**boiler_inputs), consumption='decrease'):
        '''
        consumption = 'decrease' / 'increase'
        '''
        # rcParams['path.simplify_threshold'] = 1.0
        mplstyle.use(['fast'])
       
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        
        hours_x = [i for i in range(0, hours)]

        self.axes = fig.add_subplot(111)
        self.axes.set_xlim(left=0)
        self.axes.set_yticks([i for i in range (-50, 50, 1)]) 
        self.axes.set_xticks([i for i in range (0, hours, 1)]) 

        for i in range(0, len(hours_x), 1):
            if (i == 0):
                plt.text(hours_x[i], boiler.hw_reserve_and_boil[i]+0.2, f"{round(boiler.hw_reserve_and_boil[i], 1)} м3/ч")
            elif (i != 0 and abs(boiler.hw_reserve_and_boil[i] - boiler.hw_reserve_and_boil[i-1]) > 0.5):
                plt.text(hours_x[i]+0.5, boiler.hw_reserve_and_boil[i]+0.2, f"{round(boiler.hw_reserve_and_boil[i], 1)} м3/ч")
        
        for i in range(0, len(hours_x), 1):
            if (i == 0):
                plt.text(hours_x[i], boiler.consumption_by_hours_24[i]-0.8, f"{round(boiler.consumption_by_hours_24[i], 1)} м3/ч")
            elif (i != 0 and abs(boiler.consumption_by_hours_24[i] - boiler.consumption_by_hours_24[i-1]) > 0.5):
                plt.text(hours_x[i], boiler.consumption_by_hours_24[i]-0.8, f"{round(boiler.consumption_by_hours_24[i], 1)} м3/ч")


        self.axes.plot(hours_x, [0] * len(hours_x), "r-")
        self.axes.plot(hours_x, boiler.consumption_by_hours_24, "b.-", label=f'Расход горячей воды из бойлера {boiler.t3_boiler} гр')
        self.axes.plot(hours_x, boiler.hw_reserve_and_boil, "g.-", label=f'Запас воды в бойлере {boiler.t3_boiler} гр')
        self.axes.plot(hours_x, boiler.boiler_heating_G_list, ".-", label=f'Нагрев воды бойлере до {boiler.t3_boiler} гр')
        
        plt.title("Запас горячей воды в бойлере")
        plt.xlabel('hours')
        plt.ylabel('consumption')
        plt.grid(True, color='tab:gray')
        plt.legend() 
        # plt.ioff()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        

    def update_data(self, hours=24, boiler=Boiler(**boiler_inputs), consumption='decrease'):
        
        hours_x = [i for i in range(0, hours)]

        self.axes.set_yticks([i for i in range (-50, 50, 1)]) 
        self.axes.set_xticks([i for i in range (0, hours, 1)]) 
        self.axes.set_xlim(left=0)
        
        for i in range(0, len(hours_x), 1):
            if (i == 0):
                plt.text(hours_x[i], boiler.hw_reserve_and_boil[i]+0.2, f"{round(boiler.hw_reserve_and_boil[i], 1)} м3/ч")
            elif (i != 0 and abs(boiler.hw_reserve_and_boil[i] - boiler.hw_reserve_and_boil[i-1]) > 0.5):
                plt.text(hours_x[i]+0.5, boiler.hw_reserve_and_boil[i]+0.2, f"{round(boiler.hw_reserve_and_boil[i], 1)} м3/ч")

        for i in range(0, len(hours_x), 1):
            if (i == 0):
                plt.text(hours_x[i], boiler.consumption_by_hours_24[i]-0.8, f"{round(boiler.consumption_by_hours_24[i], 1)} м3/ч")
            elif (i != 0 and abs(boiler.consumption_by_hours_24[i] - boiler.consumption_by_hours_24[i-1]) > 0.5):
                plt.text(hours_x[i], boiler.consumption_by_hours_24[i]-0.8, f"{round(boiler.consumption_by_hours_24[i], 1)} м3/ч")


        self.axes.plot(hours_x, [0] * len(hours_x), "r-")
        self.axes.plot(hours_x, boiler.consumption_by_hours_24, "b.-", label=f'Расход горячей воды из бойлера {boiler.t3_boiler} гр')
        self.axes.plot(hours_x, boiler.hw_reserve_and_boil, "g.-", label=f'Запас воды в бойлере {boiler.t3_boiler} гр')
        self.axes.plot(hours_x, boiler.boiler_heating_G_list, ".-", label=f'Нагрев воды бойлере до {boiler.t3_boiler} гр')    
               
        plt.title("Запас горячей воды в бойлере")
        plt.xlabel('hours')
        plt.ylabel('consumption')
        plt.grid(True)
        plt.legend()
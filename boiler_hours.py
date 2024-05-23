from matplotlib import pyplot as plt 
from matplotlib import figure 
import pandas as pd
import numpy as np


pd.options.display.max_columns = 0
pd.set_option('display.expand_frame_repr', False)


def mix_temp (m1, T1, m2, T2) -> int:
    return int((m1*T1 + m2*T2) / (m1 + m2))

def heating_water(Q_kW, G_m3_h, t2)  -> float:
    return ((Q_kW / 1.163 / G_m3_h) + t2)

def heating_water_G(Q_kW, t2, t1) -> float:
    return abs(Q_kW / 1.163 / (t2 - t1))


class Boiler():
    def __init__(self,
                name,
                boiler_power_kW : int,
                power_recircle_kW : int,
                boiler_volume_m3 : float,
                days : float,
                consumption_by_hours_24 : list[float],
                tw1 : int = 5,
                t3 : int = 65,
                t4 : int = 55,
                t3_boiler : int = 65
                ) -> None:
        self.name = name
        self.days = days
        self.consumption_by_hours_24 = consumption_by_hours_24
        self.consumption_by_hours_24_65 = []
        self.tw1 = tw1
        self.t3 = t3
        self.t4 = t4
        self.t3_boiler = t3_boiler
        self.boiler_power_kW = boiler_power_kW
        self.power_recircle_kW = power_recircle_kW
        self.boiler_volume_m3 = boiler_volume_m3
        self.hw_reserve_init = self.boiler_volume_m3 
        self.hours = self.days * 24
        self.power_result_kW = boiler_power_kW - power_recircle_kW
        self.hw_reserve = [self.boiler_volume_m3]
        self.hw_reserve_and_boil = [self.hw_reserve_init]
        self.boiler_heating_G = round(heating_water_G(Q_kW=self.power_result_kW, t1=self.t3_boiler, t2=self.tw1), 2)
        self.data = pd.DataFrame([i for i in range(len(self.consumption_by_hours_24 * self.days))], columns=["час"])
        self.data.set_index("час", inplace=True, drop=True)
        self.report = []

    def calculate(self):

        if (self.days <= 0):
            msg_error = f"ERROR - days must more then 0, but {self.days} instead"
            raise Exception(msg_error)

        try:
            #save the init consume of 65 water
            self.consumption_by_hours_24_65 = self.consumption_by_hours_24 * self.days
        
            # case if we want to overheat t3 vore then 65 degrees 
            if self.t3_boiler != 65:
                power_hw = [(i*1.163*(self.t3-self.tw1)) for i in self.consumption_by_hours_24 * self.days]
                self.consumption_by_hours_24 = [round(i/1.163/(self.t3_boiler-self.tw1),3) for i in power_hw]
            else:
                self.consumption_by_hours_24 = self.consumption_by_hours_24 * self.days

            for i in range(1, len(self.consumption_by_hours_24)):
                self.hw_reserve.append(round(self.hw_reserve[i-1] + self.consumption_by_hours_24[i], 3))
            
            self.boiler_heating_G = round(heating_water_G(Q_kW=self.power_result_kW, t1=self.t3_boiler, t2=self.tw1), 2)
            
            self.boiler_heating_G_list = [min(abs(self.boiler_heating_G), abs(i)) for i in self.consumption_by_hours_24]

            for i in range(1, (self.hours)):
                self.hw_reserve_and_boil.append(round(self.hw_reserve_and_boil[i-1] + self.boiler_heating_G + self.consumption_by_hours_24[i], 2))

                if self.hw_reserve_and_boil[i] > self.boiler_volume_m3:  
                    self.hw_reserve_and_boil[i] = self.boiler_volume_m3

                if self.hw_reserve_and_boil[i] < 0:  
                    self.hw_reserve_and_boil[i] = 0
            
        except IndexError:
            if (len(self.consumption_by_hours_24 * self.days) % 24 != 0):
                msg_error = f"ERROR - consumption_by_hours_24 not properly size (must be {len(self.consumption_by_hours_24_65)} value long, but - {len(self.consumption_by_hours_24)} instead)"
                raise Exception(msg_error)



    def plot_boiler(self, consumption = 'decrease'):
        '''
        consumption = 'decrease' / 'increase'
        '''
        hours_x = [i for i in range(0, self.hours)]

        if consumption == 'increase':
            consumption_by_hours_24 = [abs(i) for i in self.consumption_by_hours_24]
        else:
            consumption_by_hours_24 = self.consumption_by_hours_24

        plt.figure(figsize=(24, 12), dpi=80)
        plt.ylim(0, int(max(self.hw_reserve_and_boil)+5))

        plt.xticks([i for i in range(0, len(hours_x)+2, max(int(len(hours_x) / 48), 1))])
        plt.yticks([i for i in range(int(min(self.consumption_by_hours_24))-2, int(max(self.hw_reserve_and_boil))+5, 1)])

        for i in range(0, len(hours_x), 1):
            if (i == 0):
                plt.text(hours_x[i], self.hw_reserve_and_boil[i]+0.2, f"{round(self.hw_reserve_and_boil[i], 1)} м3/ч")
            elif (i != 0 and abs(self.hw_reserve_and_boil[i] - self.hw_reserve_and_boil[i-1]) > 0.5):
                plt.text(hours_x[i]+0.5, self.hw_reserve_and_boil[i]+0.2, f"{round(self.hw_reserve_and_boil[i], 1)} м3/ч")
        
        for i in range(0, len(hours_x), 1):
            if (i == 0):
                plt.text(hours_x[i], consumption_by_hours_24[i]-0.8, f"{round(consumption_by_hours_24[i], 1)} м3/ч")
            elif (i != 0 and abs(consumption_by_hours_24[i] - consumption_by_hours_24[i-1]) > 0.5):
                plt.text(hours_x[i], consumption_by_hours_24[i]-0.8, f"{round(consumption_by_hours_24[i], 1)} м3/ч")


        if self.t3_boiler != self.t3:
            plt.plot(hours_x, self.consumption_by_hours_24_65, ".-", label=f'Расход горячей воды {self.t3} гр')
            plt.yticks([i for i in range(int(min(self.consumption_by_hours_24_65))-2, int(max(self.hw_reserve_and_boil) +5), 1)])

        # hw_reserve_and_boil_plot = [i if i>0 else 0 for i in self.hw_reserve_and_boil]


        plt.plot(hours_x, [0] * len(hours_x), "r-")
        plt.plot(hours_x, consumption_by_hours_24, "b.-", label=f'Расход горячей воды из бойлера {self.t3_boiler} гр')
        plt.plot(hours_x, self.hw_reserve_and_boil, "g.-", label=f'Запас воды в бойлере {self.t3_boiler} гр')
        plt.plot(hours_x, self.boiler_heating_G_list, ".-", label=f'Нагрев воды бойлере до {self.t3_boiler} гр')


        plt.title("Запас горячей воды в бойлере")
        plt.xlabel('hours')
        plt.ylabel('consumption')
        plt.grid(True)
        plt.legend()
        plt.show()


    def create_df(self) -> None:

        # data = pd.DataFrame([i for i in range(len(self.consumption_by_hours_24))], columns=["час"])
        
        self.data["Резерв ГВС в начале часа, м3/ч"] = [self.boiler_volume_m3] + [self.hw_reserve_and_boil[i-1] for i in range(1, len(self.hw_reserve_and_boil))]
        
        self.data["Расход_65гр, м3/ч"] = self.consumption_by_hours_24_65
        
        if self.t3_boiler != self.t3:
            self.data["Расход_воды_из бойлера, м3/ч"] = self.consumption_by_hours_24

        self.data["Нагрев, м3/ч"] = [self.boiler_heating_G] *len(self.hw_reserve_and_boil)

        self.data["Резерв ГВС в конце часа, м3/ч"] = self.hw_reserve_and_boil
         
    def update_df(self) -> None:
        pass


    def print_df(self) -> None:
        try:
            print(self.data)
        except:
            print("DataFrame doesn't exist")

    def df_save(self):
        self.data.to_csv(f"таблица расчетов {self.name}")

    def print_report(self):
        self.report =["Исходные данные",
                f"Объем бойлера - {self.boiler_volume_m3} м3",
                f"Мощность нагрева бойлера - {self.boiler_power_kW} кВт",
                f"Нагрузка ГВС макс.час - {0} кВт",
                f"Нагрузка ГВС ср.час - {0} кВт",
                f"Нагрузка ГВС циркуляции - {self.power_recircle_kW} кВт",
                f"температура ГВС Т3 - {self.t3}",
                f"температура ГВС Т4 - {self.t4}",
                f"температура ГВС B1 - {self.tw1}",
                f"Рассматриваемый промежуток времени {self.hours} ч",
                "Расчет выполняется по формулам :",
                "объем нагреваемой воды_м3 = (Мощность нагревателя_кВт - Мощность на нагрев циркуляции_кВт) / 1.163 / (Температура_65 - Температура_5)",
                "запас горячей воды_м3 = (резерв горячей воды - расход горячей воды + объем нагреваемой воды "
                ]
        for i in self.report:
            print(i)



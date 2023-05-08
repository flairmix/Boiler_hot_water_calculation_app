from enum import Enum, auto
from math import sqrt

import source_data
import calc

PRESSURE_ATMOSPHERE_BAR = 1.01325
TEMPERATURE_ATMOSPHERE_0 = 273.15
TEMPERATURE_ATMOSPHERE_20 = 293.15


class GAS_VELOCITY(Enum):
    """ m/s """
    GAS_VELOCITY_LOW_PRESSURE = 7
    GAS_VELOCITY_MID_PRESSURE = 15
    GAS_VELOCITY_HIGH_2_PRESSURE = 25
    GAS_VELOCITY_HIGH_1_PRESSURE = 25


class GAS_DROP_CONSTRUCT_COEF(Enum):
    SP_89 = 0.05    #СП 89.13330 п7.8
    SP_373 = 0.03   #СП 373.13330 п5.14
    SP_253 = 0.05   #СП 253.13330 п6.9


class GAS_PRESSURE_CLASS(Enum):
    """ bar """
    GAS_LOW_PRESSURE = [0.0, 0.05]    
    GAS_MID_PRESSURE = [0.05, 3.0]
    GAS_HIGH_2_PRESSURE = [3.0, 6.0]
    GAS_HIGH_1_PRESSURE = [6.0, 12.0]


class Gas_system():
    def __init__(self):
        self.POWER_sum = source_data.POWER_sum       

    def gas_consumption_norm(self, list:source_data.Q_boilers, efficiency_boiler=0.92, heating_value=8000):
        """
        return gas consumption for list of boilers, m3/h
        Q_boiler - Gcal/h - boiler power 
        """
        #расчет расхода природного газа  
        G_gas = []
        for boiler in source_data.Q_boilers:
            G_gas.append(round(10 **6 * boiler / heating_value / efficiency_boiler, 3)) 
            # print("расход газа котел,", boiler,"  м3/ч - ", G_gas[-1])

        G_gas_sum = sum(i for i in G_gas)
        # print("расход газа сумма, м3/ч - ", G_gas_sum)

        return(G_gas_sum)


    def gas_consumption_norm_one(self, Q_boiler, efficiency_boiler=0.92, heating_value=8000):
        """
        return gas consumption for one boiler 
        Q_boiler - Gcal/h - boiler power 
        """
        return round(10 **6 * Q_boiler / heating_value / efficiency_boiler, 3)


    def gas_consumption_work(self, gas_consumption_norm, gas_work_pressure):
        return (gas_consumption_norm * PRESSURE_ATMOSPHERE_BAR) / (gas_work_pressure + PRESSURE_ATMOSPHERE_BAR)
   

class Gas_subsystem(Gas_system):
    '''gas_pressure_bar - kgf/cm2 '''
    def __init__(self, gas_pressure_bar):
        super().__init__()

        self.gas_pressure_bar = gas_pressure_bar

        for name, member in GAS_PRESSURE_CLASS.__members__.items():
            if (self.gas_pressure_bar > member.value[0] and self.gas_pressure_bar <= member.value[1]):
                # print(name, member.value)
                self.gas_pressure_class = member
                break

        if (member.name == "GAS_LOW_PRESSURE"):
                self.velocity_max = GAS_VELOCITY.GAS_VELOCITY_LOW_PRESSURE.value
        elif(member.name == "GAS_MID_PRESSURE"):
                self.velocity_max = GAS_VELOCITY.GAS_VELOCITY_MID_PRESSURE.value
        else:
                self.velocity_max = GAS_VELOCITY.GAS_VELOCITY_HIGH_1_PRESSURE.value
        
        
    def gas_consumption_work(self, gas_consumption_norm):
        
        coef = (source_data.gas_temperature * (PRESSURE_ATMOSPHERE_BAR)) / ((TEMPERATURE_ATMOSPHERE_0+20) * (self.gas_pressure_bar+(PRESSURE_ATMOSPHERE_BAR)))
        return gas_consumption_norm * coef


    def gas_velocity(self, gas_consumption_norm, dn_gas_pipe):
        """
        return gas velocity in pipe, m/s
        gas_consumption_norm, norm_m3/h
        """
        gas_velocity = 0.1247 * (gas_consumption_norm * 1 * source_data.gas_temperature) / ((dn_gas_pipe ** 2) * ((PRESSURE_ATMOSPHERE_BAR + self.gas_pressure_bar)/10))
        return gas_velocity


    def gas_dn_pipe(self, gas_consumption_norm):
        """
        return dn gas pipe , mm
        gas_consumption_norm, norm_m3/h
        """      
        for dn in [32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300, 325, 350]:
            if (self.gas_velocity(gas_consumption_norm, dn) <= self.velocity_max):
                return dn

    def gas_collector_dn(self, gas_consumption, length):
        gas_volume = gas_consumption / 1000
        # S = Пи х (D / 2)² х h
        # V = calc.pi * ((Dn **2) / 4) * length
        Dn = sqrt((4 * gas_volume) / (calc.pi * length))
        return Dn


def gas_consution(list:source_data.Q_boilers, efficiency_boiler=0.92, heating_value=8000):
    """
    return gas consumption for list of boilers, m3/h
    Q_boiler - Gcal/h - boiler power 
    """
    #расчет расхода природного газа  
    G_gas = []
    for boiler in source_data.Q_boilers:
        G_gas.append(round(10 **6 * boiler / heating_value / efficiency_boiler, 3)) 
        # print("расход газа котел,", boiler,"  м3/ч - ", G_gas[-1])

    G_gas_sum = sum(i for i in G_gas)
    # print("расход газа сумма, м3/ч - ", G_gas_sum)

    return(G_gas_sum)


def gas_consution_one(Q_boiler, efficiency_boiler=0.92, heating_value=8000):
    """
    return gas consumption for one boiler 
    Q_boiler - Gcal/h - boiler power 
    """
    return round(10 **6 * Q_boiler / heating_value / efficiency_boiler, 3)



if __name__ == '__main__':

    gas_1_1 = Gas_subsystem(0.05)

    print(gas_1_1.gas_pressure_class)
    gas_1_1_cons = gas_1_1.gas_consumption_norm(source_data.Q_boilers)

    print("расход газа м3/ч нормальный ", gas_1_1_cons)
    gas_1_1_cons_work = gas_1_1.gas_consumption_work(gas_1_1_cons)
    print("расход газа м3/ч рабочий", gas_1_1_cons_work)
    print("dn  ", gas_1_1.gas_dn_pipe(gas_1_1_cons))
    print("скорость ", gas_1_1.gas_velocity(gas_1_1_cons, gas_1_1.gas_dn_pipe(gas_1_1_cons)))

    length = 9
    print("Dn_collector ", round(gas_1_1.gas_collector_dn(gas_1_1_cons_work, length), 5), "при длине в м. - ", length)








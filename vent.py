import source_data
import gas_in


class Vent():
    def __init__(self):

        self.S_boiler_room = source_data.wall_0 * source_data.wall_1 
        self.V_boiler_room = round(source_data.wall_0 * source_data.wall_1 * source_data.height, 3)

    def print_info(self):
        print("Вентиляция")
        print("Габариты помещения")
        print("длина_0, м - ", source_data.wall_0, "; длина_1, м - ", source_data.wall_1, "; высота, м - ", source_data.height)
        print("объем здания, м3 - ", self.V_boiler_room)

    def volume_without_eqp(self, coef=0.9):
        """объем помещения минус объем оборудования """ 
        return (self.V_boiler_room * coef)

    def general_exchange_vent(self, coef_exchange=3):
        """ Расход воздуха на общеобменный воздухообмен, м3ч  """
        return (self.volume_without_eqp() * coef_exchange)

    def G_air_for_fire(self):
        """ Расход воздуха на горение, м3ч  """
        return (gas_in.gas_consution(source_data.Q_boilers) * 1.2 * ((1.13 * source_data.heating_value) / 1000))

    def G_air_sum(self):
        """ Расход воздуха на горение и общеобмен, м3ч  """
        return (self.G_air_for_fire() + self.general_exchange_vent())


class Vent_grill(Vent):
    def __init__(self):
        super().__init__()
        
        self.grill_number = 1 
        self.v_grill = 1

    def S_grill_calc(self):
        """ Сечение приточной решетки расчетное, м2 """
        return (self.G_air_sum() / 3600 / self.v_grill)
        
    def S_grill_sum(self):
        """ Сечение приточной решетки живое, м2 """
        return (self.S_grill_calc() * 0.7)

    def S_grill(self):
        """ Сечение одной приточной решетки живое, м2 """
        return (self.S_grill_sum() / self.grill_number)



class Vent_deflector(Vent):
    def __init__(self):
        super().__init__()

        self.grill_number = 1 
        self.v_grill = 1


class Heating_system():
    def __init__(self, temp_in, temp_out):

        self.temp_in = temp_in
        self.temp_out = temp_out


class H_Barrier(Heating_system):
    def __init__(self, temp_in, temp_out):
        super().__init__(temp_in, temp_out)




if __name__ == "__main__":    

    vent = Vent()
    print(vent.S_boiler_room)
    print(vent.general_exchange_vent())
    print(vent.G_air_for_fire())

    vent_grill = Vent_grill()
    print(vent_grill.S_boiler_room)


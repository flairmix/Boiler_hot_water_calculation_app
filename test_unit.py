import unittest
from boiler_hours import Boiler
from contextlib import contextmanager

consumption_1_case_standart = [-0.487, -0.487, -0.487, -0.487, -0.487,
                    -5.44, -13.869, -13.869, -5.44, -5.44,
                    -5.44, -4.65, -4.65, -4.65, -4.65,
                    -5.137, -5.44, -5.44, -13.869, -13.869,
                    -5.44, -5.44, -5.44, -5.44
                    ]

consumption_1_case_empty = []


class TestBoiler(unittest.TestCase):

    def test_calculate_normal(self):
        self.boiler_1 = Boiler(name ="test_boiler_1",
                boiler_power_kW = 600,
                power_recircle_kW = 193,
                boiler_volume_m3 = 20,
                hw_reserve_init = 20,
                days = 3,
                consumption_by_hours_24 = consumption_1_case_standart,
                tw1 = 10,
                t3 = 65,
                t4 = 55,
                t3_boiler = 65)
        
        self.boiler_1.calculate()

        self.assertEqual(self.boiler_1.consumption_by_hours_24_65, [-0.487, -0.487, -0.487, -0.487, -0.487, -5.44, -13.869, -13.869, -5.44, -5.44, 
                                                                     -5.44, -4.65, -4.65, -4.65, -4.65, -5.137, -5.44, -5.44, -13.869, -13.869, 
                                                                     -5.44, -5.44, -5.44, -5.44, -0.487, -0.487, -0.487, -0.487, -0.487, -5.44, 
                                                                     -13.869, -13.869, -5.44, -5.44, -5.44, -4.65, -4.65, -4.65, -4.65, -5.137, 
                                                                     -5.44, -5.44, -13.869, -13.869, -5.44, -5.44, -5.44, -5.44, -0.487, -0.487, 
                                                                     -0.487, -0.487, -0.487, -5.44, -13.869, -13.869, -5.44, -5.44, -5.44, -4.65, 
                                                                     -4.65, -4.65, -4.65, -5.137, -5.44, -5.44, -13.869, -13.869, -5.44, -5.44, 
                                                                     -5.44, -5.44],
                                                                    msg="consumption_by_hours_24_65 --- OK")
        self.assertEqual(len(self.boiler_1.consumption_by_hours_24_65),  72)
        self.assertEqual(len(self.boiler_1.hw_reserve),  72)
        self.assertEqual(self.boiler_1.boiler_heating_G,  6.36)
        self.assertEqual(len(self.boiler_1.hw_reserve_and_boil ),  72)
        self.assertEqual(self.boiler_1.hw_reserve_and_boil , [20, 20, 20, 20, 20, 20, 12.49, 4.98, 5.9, 6.82, 7.74, 9.45, 11.16, 12.87, 14.58, 
                                                                15.8, 16.72, 17.64, 10.13, 2.62, 3.54, 4.46, 5.38, 6.3, 12.17, 18.04, 20, 20, 20, 
                                                                20, 12.49, 4.98, 5.9, 6.82, 7.74, 9.45, 11.16, 12.87, 14.58, 15.8, 16.72, 17.64, 
                                                                10.13, 2.62, 3.54, 4.46, 5.38, 6.3, 12.17, 18.04, 20, 20, 20, 20, 12.49, 4.98, 5.9, 
                                                                6.82, 7.74, 9.45, 11.16, 12.87, 14.58, 15.8, 16.72, 17.64, 10.13, 2.62, 3.54, 4.46, 5.38, 6.3]
                                                            )






if __name__ == "__main__":
  unittest.main(verbosity=2) 
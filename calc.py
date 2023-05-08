
pi = 3.14159265359


def GCalh_to_kW(power_Gcal_h):
    return power_Gcal_h * 1163


def kW_to_GCalh(power_kW):
    return power_kW / 1163


def pipeG(Q:float, t1:int=130, t2:int=70) -> float:
    """
    return consuption for pipe in t/h
    Q - Gcal/h - power,
    t1 - high temperature, 
    t2 - low temperature
    """
    G = 1000* Q / (t1 - t2)
    return G


def pipeDn(G, v = 1):
    """
    return dn for pipe
    G - t/h - consuption,
    v = 1 m/s - velocity of water  
    """
    DN = (20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300)
    dn = 1000 * (G / 2826 / v) ** 0.5
    i = 0
    while dn > DN[i]:
        i += 1 
    return DN[i]


def pipev(G, dn):
    """
    return velosity for dn pipe
    G - t/h 
    dn - mm
    """
    v = 10**6 *(G / (dn**2) / 2826)
    return v


def kv(Gmax, dpMin):
    kv = Gmax / (dpMin ** 0.5)
    return kv


def dp(Gmax, kvs):
    """
    return dp for Gmax consumption with kvs
    G - t/h 
    """
    return Gmax / kvs
    

if __name__ == '__main__':
    
    dn1 = pipeDn(3.8, 1)
    print(f"PipeDN собственные нужды - {dn1}")

    dn11 = pipeDn(84, 1.5)
    dn12 = pipeDn(10, 1.5)
    print(f"PipeDN котел 1 - {dn11}")
    print(f"PipeDN котел 2 - {dn12}")

    print("__________________")    
    print("__________________")    
    print("ГВС")
    G = 32.30
    dt = 20
    dn1_hws = pipeDn(G, 1.5)
    print(f"PipeDN ГВС греющий - {dn1_hws}")
    print("__________________")

    print("клапан трехходовой ГВС")
    G_hws = 32.30
    dp = 0.3
    kvs_hws = kv(G_hws, dp)

    print(f"расход гвс - {G_hws}  t/h")
    print(f"dp гвс - {dp} bar")
    print(f"kv гвс - {kvs_hws} t/h")
    kvs_valve = 61
    dp_valve = G_hws / kvs_valve
    DN_valve = 65

    print(f"kvs клапана - {kvs_valve} t/h")
    print(f"dp клапана - {dp_valve} bar")
    print(f"DN клапана - {DN_valve} mm")
    print("__________________")    


    print("__________________")    
    print("Отопление")
    Gh = 143.48
    dt = 25
    dn1_h = pipeDn(Gh, 1.5)
    print(f"PipeDN отопление греющий - {dn1_h}")
    print("__________________")

    print("клапан трехходовой ГВС")
    dp = 0.5
    kvs_h = kv(Gh, dp)

    print(f"расход отопление - {Gh}  t/h")
    print(f"dp отопление - {dp:.2f} bar")
    print(f"kv отопление - {kvs_h:.2f} t/h")
    kvs_valve = 220
    dp_valve = Gh / kvs_valve
    DN_valve = 125

    print(f"kvs клапана - {kvs_valve:.2f} t/h")
    print(f"dp клапана - {dp_valve:.2f} bar")
    print(f"DN клапана - {DN_valve} mm")
    print("__________________")    


    dn1_hws = pipeDn(1.61, 1)
    print(dn1_hws)
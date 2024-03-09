


def _byte_to_int(data):
    # Byte dizisini ikili gruplara ayırma
    data = [data[i:i+2] for i in range(0, len(data), 2)]

    return data


def volts_cells(data):
    val = _byte_to_int(data)
    voltcell = []
    for pair in val[:15]:
        voltcell.append(pair[0] + (pair[1] / 100))
    
    return voltcell

def volt_general(data):
    val = _byte_to_int(data)
    volt = []
    for pair in val[15:17]:
        volt.append((pair[0] + pair[1] / 100))    
    return volt

def temperature(data):
    val = _byte_to_int(data)
    temp= []
    for pair in val[17:19]:
        temp.append((pair[0] + pair[1] / 100 ))
    return temp
def State_of_charge(data):
    val = _byte_to_int(data)
    SoC = []
    for pair in val[19:21]:
        SoC.append((pair[0] + pair[1] /100))
    return SoC

def Wh(data):
    val = _byte_to_int(data)
    wh = []
    for pair in val[21:23]:
        wh.append((pair[0] + pair[1]))
    return wh  

def Speed(data):
    val = _byte_to_int(data)
    speed = []
    for pair in val[23:25]:
        speed.append((pair[0] + pair[1]))
    return speed  
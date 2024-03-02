byte_object = "135168468416165146854986794865"

def Check_data(byte_object):
    if isinstance(byte_object,bytes):
        return "ok"
    else:
        return "error"    

def parse_by_object(byte_object):
    # Veriyi 4'lü gruplara ayır
    groups = [byte_object[i:i+4] for i in range(0, len(byte_object), 4)]

    # Her bir 4'lü grubun içindeki her ikinci sayıdan sonra virgül ekle
    formatted_groups = []
    for group in groups:
        formatted_group = group[:2] + "," + group[2:]
        formatted_groups.append(formatted_group)

    return formatted_groups
    

def Getvalues(formatted_data):
    # Parçalanan veriyi alarak değerleri ayıkla ve adlandır
    volt = float(formatted_data[0][2:])
    temperature = float(formatted_data[1][2:])
    SoC = float(formatted_data[2][:2])
    wh = float(formatted_data[3][:2])
    speed = float(formatted_data[4][:2])
    
    return volt, temperature, SoC, wh, speed

formatted_data = parse_by_object(byte_object)


volt, temperature, SoC, wh, speed = Getvalues(formatted_data)

print("Volt:", volt)
print("Temperature:", temperature)
print("SoC:", SoC)
print("Wh:", wh)
print("Speed:", speed)
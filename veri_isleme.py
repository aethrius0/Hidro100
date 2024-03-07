def hex_to_decimal(hex_str):
    """
    Converts hexadecimal string to decimal integer.

    Args:
        hex_str: Hexadecimal string to convert.

    Returns:
        Decimal integer equivalent of the hexadecimal string.
    """
    # Remove '0x' prefix if exists
    if hex_str.startswith('0x'):
        hex_str = hex_str[2:]

    decimal_value = 0
    power = len(hex_str) - 1
    for digit in hex_str:
        if '0' <= digit <= '9':
            decimal_value += int(digit) * (16 ** power)
        else:
            decimal_value += (ord(digit.upper()) - 55) * (16 ** power)
        power -= 1

    return decimal_value

def parse_continuous_data(received_bytes):
    """
    Parses continuously received bytes into different groups for voltage, temperature, SoC, Wh, and speed.

    Args:
        received_bytes: A list of received bytes in hexadecimal format.

    Returns:
        A list of dictionaries containing parsed data.
    """
    parsed_data = []
    
    bytes_list = received_bytes.split()
    for i in range(0, len(bytes_list), 10):
        byte1 = hex_to_decimal(bytes_list[i])
        byte2 = hex_to_decimal(bytes_list[i + 1])
        byte3 = hex_to_decimal(bytes_list[i + 2])
        byte4 = hex_to_decimal(bytes_list[i + 3])
        byte5 = hex_to_decimal(bytes_list[i + 4])
        byte6 = hex_to_decimal(bytes_list[i + 5])
        byte7 = hex_to_decimal(bytes_list[i + 6])
        byte8 = hex_to_decimal(bytes_list[i + 7])
        byte9 = hex_to_decimal(bytes_list[i + 8])
        byte10 = hex_to_decimal(bytes_list[i + 9])

        volt = ((byte1 << 8) | byte2) / 100.0  # Parsed voltage value as float
        temp = ((byte3 << 8) | byte4) / 100.0  # Parsed temperature value as float
        SoC = ((byte5 << 8) | byte6) / 100.0  # Parsed SoC value as float
        wh = ((byte7 << 8) | byte8) / 100.0  # Parsed Wh value as float
        speed = ((byte9 << 8) | byte10) / 100.0  # Parsed speed value as float

        parsed_data.append({
            'volt': volt,
            'temp': temp,
            'soc': SoC,
            'wh': wh,
            'speed': speed
        })
    
    return parsed_data

def Getvalues(formatted_data):
    # Parçalanan veriyi alarak değerleri ayıkla ve adlandır
    volt = formatted_data[0]['volt']
    temp = formatted_data[0]['temp']
    SoC = formatted_data[0]['soc']
    wh = formatted_data[0]['wh']
    speed = formatted_data[0]['speed']
    
    return volt, temp, SoC, wh, speed

received_bytes = b"\x10 \x11 \x12 \x13 \x14 \x15 \x16 \x10 \x11 \x12 \x13 \x14 \x15 \x16 \x10 \x11 \x12 \x13 \x14 \x15 \x16 \x10 \x11 \x12 \x13 \x14 \x15 \x16 \x10 \x11 \x12 \x13 \x14 \x15 \x16 \x10 \x11 \x12 \x13 \x14 \x15 \x16 \x10 \x11 \x12 \x13 \x14 \x15 \x16 \x10 \x11 \x12 \x13 \x14 \x15 \x16 \x10 \x11 \x12 \x13 \x14 \x15 \x16 \x10 \x11 \x12 \x13 \x14 \x15 \x16 \x10 \x11 \x12 \x13 \x14 \x15 \x16 \x10 \x11 \x12 \x13 \x14 \x15 \x16 \x10 \x11 \x12 \x13 \x14 \x15 \x16 \x10 \x11"
formatted_data = parse_continuous_data(received_bytes)

volt, temp, SoC, wh, speed = Getvalues(formatted_data)

print("Volt:", volt)
print("Temperature:", temp)
print("SoC:", SoC)
print("Wh:", wh)
print("Speed:", speed)

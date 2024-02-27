def parse_byte_object(byte_data):
    # Veriyi 4'lü gruplara ayır
    groups = [byte_data[i:i+4] for i in range(0, len(byte_data), 4)]

    # Her bir 4'lü grubun içindeki her ikinci sayıdan sonra virgül ekle
    formatted_groups = []
    for group in groups:
        formatted_group = group[:2] + "," + group[2:]
        formatted_groups.append(formatted_group)

    return formatted_groups

# Kullanıcıdan veri girişi al - terminalden 
byte_data = input("Lütfen byte verisini girin: ")

# Veriyi işle - parse fonksiyonu 
formatted_data = parse_byte_object(byte_data)

# Sonucu yazdırma kısmı 
for group in formatted_data:
    print(group)

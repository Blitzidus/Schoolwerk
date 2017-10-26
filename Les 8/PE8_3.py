def code(invoerstring):
    NieuweData = ""
    for character in invoerstring:
        NieuweData += chr(ord(character) + 3)
    return NieuweData


print(code("RutteAlkmaarDen Helder"))

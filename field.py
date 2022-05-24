FIELD = [['']*3 for _ in range(3)]

def field():
    global FIELD
    result = ""
    for num in FIELD:
        result += str(num)
    print(result)
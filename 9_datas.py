# 9. Construa uma função que receba uma data no formato DD/MM/AAAA e
# devolva uma string no formato de “D de mesPorExtenso de AAAA”.
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def data_por_extenso(data):
    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }

    try:
        dia, mes, ano = map(int, data.split("/"))

        if mes < 1 or mes > 12:
            return None
        if dia < 1 or dia > 31:
            return None

        if mes in [4, 6, 9, 11] and dia > 30:
            return None

        if mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if dia > 29:
                    return None
            else:
                if dia > 28:
                    return None
        return f"{dia} de {meses[mes]} de {ano}"

    except:
        return None

data_input = input("Digite a data no formato DD/MM/AAAA: ")
resultado = data_por_extenso(data_input)

if resultado:
    print("Data por extenso:", resultado)
else:
    print("Data inválida!")
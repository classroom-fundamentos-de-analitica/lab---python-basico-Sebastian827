"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    with open("data.csv", "r") as file:
        data=file.read()
    data=data[:-1]
    data=data.split("\n")
    data=[data[i].split("\t") for i in range(len(data))]

    sum=0
    for i in data:
        sum+=int(i[1])
    return sum

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return


def pregunta_02():
    with open("data.csv", "r") as file:
        data=file.read()
    data=data[:-1]
    data=data.split("\n")
    data=[data[i].split("\t") for i in range(len(data))]

    a={}
    b=[]

    for i in data:
        if i[0] in a:
            a[i[0]]+=1
        else:
            a[i[0]]=1
    for i in a:
        b.append(tuple([i,a[i]]))
    b=sorted(b)
    return b
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    return


def pregunta_03():
    with open("data.csv", "r") as file:
        data=file.read()
    data=data[:-1]
    data=data.split("\n")
    data=[data[i].split("\t") for i in range(len(data))]

    a={}
    b=[]

    for i in data:
        if i[0] in a:
            a[i[0]]+=int(i[1])
        else:
            a[i[0]]=int(i[1])
    for i in a:
        b.append(tuple([i,a[i]]))
    b=sorted(b)
    return b

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    return


def pregunta_04():
    with open("data.csv", "r") as file:
        data=file.read()
    data=data[:-1]
    data=data.split("\n")
    data=[data[i].split("\t") for i in range(len(data))]

    count={}
    b=[]

    for i in data:
        mes=i[2].split("-")[1]
        if mes in count:
            count[mes]+=1
        else:
            count[mes]=1
    for i in count:
        b.append(tuple([i,count[i]]))
    b=sorted(b)
    return b
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    return


def pregunta_05():
    with open("data.csv", "r") as file:
        data=file.read()
    data=data[:-1]
    data=data.split("\n")
    data=[data[i].split("\t") for i in range(len(data))]

    a={}
    b=[]
    for i in data:
        if i[0] in a:
            a[i[0]][0]= min(a[i[0]][0],int(i[1]))
            a[i[0]][1] =max(a[i[0]][1],int(i[1]))
        else:
            a[i[0]]=[int(i[1]),int(i[1])]
    for i in a:
        b.append(tuple([i,a[i][1],a[i][0]]))
    b=sorted(b)
    return b


    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    return


def pregunta_06():
    with open("data.csv", "r") as file:
        data=file.read()
    data=data[:-1]
    data=data.split("\n")
    data=[data[i].split("\t") for i in range(len(data))]

    a={}
    b=[]
    for i in range(len(data)):
        dic=data[i][-1]
        m=dic.split(",")
        l=[elemento.split(":") for elemento in m]
        diccionario = {elemento[0]: elemento[1] for elemento in l}
        
        for j in diccionario:
            if j in a:
                a[j][0]=max(int(a[j][0]),int(diccionario[j]))
                a[j][1]=min(int(a[j][1]),int(diccionario[j]))
            else:
                a[j]=[int(diccionario[j]),int(diccionario[j])]
        
    for i in a:
        b.append(tuple([i,a[i][1],a[i][0]]))
    b=sorted(b)
    return b
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return


def pregunta_07():
    with open("data.csv", "r") as file:
        data=file.read()
    data=data[:-1]
    data=data.split("\n")
    data=[data[i].split("\t") for i in range(len(data))]

    a={}
    b=[]
    for i in data:
        if i[1] in a:
            a[i[1]].append(i[0])
        else:
            a[i[1]]=list(i[0])
    for i in a:
     b.append(tuple([int(i),a[i]]))
    b=sorted(b)
    return b

    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return


def pregunta_08():
    with open("data.csv", "r") as file:
        data=file.read()
    data=data[:-1]
    data=data.split("\n")
    data=[data[i].split("\t") for i in range(len(data))]

    a={}
    b=[]
    for i in data:
        if i[1] in a:
            a[i[1]].append(i[0])
        else:
            a[i[1]]=list(i[0])
    for i in a:
        b.append(tuple([int(i),sorted(list(set(a[i])))]))
    b=sorted(b)
    return b
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    with open("data.csv", "r") as file:
        data=file.read()
    data=data[:-1]
    data=data.split("\n")
    data=[data[i].split("\t") for i in range(len(data))]

    a={}
    b=[]
    for i in range(len(data)):
        dic=data[i][-1]
        m=dic.split(",")
        l=[elemento.split(":") for elemento in m]
        diccionario = {elemento[0]: elemento[1] for elemento in l}
        for i in diccionario:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        
    for i in a:
        b.append(tuple([i,a[i]]))
    b=sorted(b)
    a={elemento[0]: elemento[1] for elemento in b}
    return a
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    with open("data.csv", "r") as file:
        data=file.read()
    data=data[:-1]
    data=data.split("\n")
    data=[data[i].split("\t") for i in range(len(data))]

    a=[]
    b=[]
    for i in range(len(data)):
        dic=data[i][-1]
        m=dic.split(",")
        l=[elemento.split(":") for elemento in m]
        diccionario = {elemento[0]: elemento[1] for elemento in l}

        lista=data[i][3].split(",")

        a.append([data[i][0],len(lista),len(diccionario)])

    for i in a:
        b.append(tuple([i[0],i[1],i[2]]))
    return b
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    with open("data.csv", "r") as file:
        data=file.read()
    data=data[:-1]
    data=data.split("\n")
    data=[data[i].split("\t") for i in range(len(data))]

    a={}
    b={}
    for i in range(len(data)):
        lista=data[i][3].split(",")
        for j in lista:
            if j in a:
                a[j]+=int(data[i][1])
            else:
                a[j]=int(data[i][1])
    for i in sorted(a):
        b[i]=a[i]
    return b
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    with open("data.csv", "r") as file:
        data=file.read()
    data=data[:-1]
    data=data.split("\n")
    data=[data[i].split("\t") for i in range(len(data))]
    
    a={}
    b={}
    for i in range(len(data)):
        dic=data[i][-1]
        m=dic.split(",")
        l=[elemento.split(":") for elemento in m]
        diccionario = {elemento[0]: elemento[1] for elemento in l}
        if data[i][0] in a:
            for j in diccionario:
                a[data[i][0]]+=int(diccionario[j])
        else:
            a[data[i][0]]=0
            for j in diccionario:
                a[data[i][0]]+=int(diccionario[j])
    for i in sorted(a):
        b[i]=a[i]
    return b
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return

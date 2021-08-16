# Recursion Exercise

def recursive_ex(x):
    if (x == 0):
        print("Este es el caso base")
    else:
        print("Entrando a la recursion: " + str(x))
        return recursive_ex(x-1)

recursive_ex(7)
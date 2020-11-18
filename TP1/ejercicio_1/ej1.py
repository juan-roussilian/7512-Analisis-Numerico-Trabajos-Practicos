import random
from matplotlib import pyplot as plt


def desbloquear_candado(clave):
    for j in range(9999):
        if j == clave:
            print("El candado se desbloqueo en " + str(j) + " intentos")
            break
    return j


def graficar(experimentos):
    plt.title("Histograma de intentos")
    plt.hist(
        experimentos,
        bins=1000,
        color="blue",
        edgecolor="green",
        linewidth=1
    )
    plt.xlabel("Intentos requeridos")
    plt.ylabel("Experimentos realizados")
    plt.show()


def main():
    experimentos = []
    for i in range(100000):
        clave_candado = random.randint(0, 9999)
        print("Realizando experimento #" + str(i))
        experimentos.append(desbloquear_candado(clave_candado))
    graficar(experimentos)


if __name__ == "__main__":
    main()

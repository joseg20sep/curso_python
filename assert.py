def divisors(num):
    assert num >= 0, "Debes ingresar un numero positivo"
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input('Ingresa un numero: ')
    assert num.replace("-", "").isnumeric() and int(num)>0 , "Debes ingresar solo numeros positivos"
    print(divisors(int(num)))
    print("Termina mi programa")


if __name__ == '__main__':
    run()
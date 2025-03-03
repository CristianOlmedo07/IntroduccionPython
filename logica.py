#un cajero automatico

from usuario import usuario


usuario.append("Cristian Olmedo")
usuario.append("1234")
usuario.append(1000)

recibo = list()
recibo.append(["123",600])
recibo.append(["124",6])
recibo.append(["125",300])
recibo.append(["126",765])
recibo.append(["127",645])
recibo.append(["128",64])

acciones = list()
acciones.append("Deposito")
acciones.append("Pago de recibo")   
acciones.append("Retiro")

usuario2 = list()
usuario2.append("Cristian.O")
usuario2.append("12345")
usuario2.append(3400)

def registrar(nombre,password):
    usuarioRegistrado = list()
    usuarioC = input("Ingrese su nombre:")
    usuarioRegistrado.input("Igrese su password: ")

    if usuarioC == usuario[0] and usuarioRegistrado == usuario [1]:
        print("bienvenido al cagero automatico")
        return registrar()


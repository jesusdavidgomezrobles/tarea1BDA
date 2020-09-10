class menu():
    
    print("\t.......:MENU:....")
    print("1. Ingrese Funcionario")
    print("2. Imprimir Funcionario")
    print("3. Eliminar Funcionario")
    print("4. Consultar funcionario")
    print("5. Salir")
    print()



menu = int(input("Digite un numero:"))

if  menu == 1:
    print("Teniendo en cuenta que: (1={SI} y 0={No}")
    continuar = int(input("Desea ingresar Datos de Funcionario?... Ingrese un numero ---->"))

    while continuar == 1:
        print()
        print("\t.----Datos Del Funcionario------")
        
        ident = input(' Ingrese la ID del Funcionario------>')
        nombre= input('Ingrese el Nombre del Funcionario------> ')
        cargo = input('Ingrese el Cargo del Funcionario------> ')
        salario = input('Ingrese el Salario del Funcionario------> ')
        personas = {'ID': ident, 'nombre': nombre, 'cargo': cargo, 'salario': salario}
        
        print("\n.Teniendo en cuenta que: (1={SI} y 0={No}")
        continuar = int(input("Desea continuar ingresando datos de funcionario?... Ingrese un numero---->"))
        
    print("Fin del ingredo de funcionarios")
   

if menu == 2:
    print("A continuacion se mostraran los datos del funcionario")
    print(personas)    
    

print("Estos fueron todos los datos")
 


    
        

        
         
    
        
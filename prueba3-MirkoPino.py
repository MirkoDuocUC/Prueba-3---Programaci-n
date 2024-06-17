import csv

lista_planes=[]
def agregar_plan():
    IDa=int(input("Ingrese el ID:\n"))
    Nombre=input("Ingrese el nombre del plan:\n")
    Porc_efect=int(input("Ingrese el porcentaje de efectividad:\n"))
    
    if Porc_efect>=0 and Porc_efect<=25:
        categoria="Chiste"
    elif Porc_efect>=26 and Porc_efect<=50:
        categoria="Anecdota"
    elif Porc_efect>=51 and Porc_efect<=75:
        categoria="Peligro"
    elif Porc_efect>=76 and Porc_efect<=99:
        categoria="Atencion"
    elif Porc_efect>=100:
        categoria="Esclavitud"
    
    plan={"ID":IDa, "Nombre":Nombre, "Porcent. de efectividad":Porc_efect, "Categoria":categoria}
    lista_planes.append(plan)

def listar_planes():
    for l in lista_planes:
        print("ID: ",l["ID"], "Nombre: ",l["Nombre"], "Por. Efectividad: ",l["Porcent. de efectividad"], "Categoria: ",l["Categoria"])
        
def validacion_eliminar():
    decision=input("Está seguro que desea eliminar el plan? (si/no)").lower()
    return decision=="si"

def calcular_estadisticas():
    if len(lista_planes)==0:
        print("No hay planes en la lista")
        return
    
    total_efectividad=sum(m['Porcent. de efectividad'] for m in lista_planes)
    cantidad_planes=len(lista_planes)
    promedio=total_efectividad/cantidad_planes
    pemasalto=max(m['Porcent. de efectividad'] for m in lista_planes)
    
    print(f"El porcentaje de efectividad promedio es: {promedio}")
    print(f"El porcentaje de efectividad mas alto es: {pemasalto}")
    
    


while True:
    print("---M E N U---\n")
    print("1.Agregar plan")
    print("2.Listar planes")
    print("3.Eliminar plan por ID")
    print("4.Generar bbdd")
    print("5.Cargar bbdd")
    print("6.Estadisticas")
    print("0.Salir")
    
    op=int(input("Seleccione una opción:\n"))
    
    if op==1:
        print("")
        agregar_plan()
    elif op==2:
        print("")
        listar_planes()
    elif op==3:
        print("")
        encontrado=False
        Idelet=int(input("Ingrese el ID del plan a eliminar:\n"))
        for d in lista_planes:
            if d["ID"]==Idelet:
                print("Se ha encontrado el plan")
                print("ID: ",d["ID"], "Nombre: ",d["Nombre"], "Por. Efectividad: ",d["Porcent. de efectividad"], "Categoria: ",d["Categoria"])
                if validacion_eliminar():
                    lista_planes.remove(d)
                    encontrado=True
                    print("Se ha eliminado exitosamente")
                else:
                    print("Eliminación cancelada")
        if encontrado==False:
            print("Plan no encontrado. Ingrese un plan que exista...")
        else:
            print()   
                
    elif op==4:
        print("")
        encabezados=['ID', 'Nombre', 'Porcent. de efectividad', 'Categoria']
        with open('csvprueba3.csv', 'w', newline='') as archivocsv:
            writercsv=csv.DictWriter(archivocsv, fieldnames=encabezados)
            writercsv.writeheader()
            writercsv.writerows(lista_planes)
            
    elif op==5:
        print("")
        with open('csvprueba3.csv', 'w', newline='') as archivocsv:
            lectorcsv=csv.DictReader(archivocsv)
            lista_planes.clear()
            for f in lectorcsv:
                lista_planes.append({
                    'ID': int(f['ID']),
                    'Nombre':f['Nombre'],
                    'Por. Efectividad': int(f['Porcent. de efectividad']),
                    'Categoria':f['Categoria']
                    
                })
    
        
    elif op==6:
        print("===E S T A D I S T I C A S===")
        listar_planes()
        calcular_estadisticas()
        
        
    elif op==0:
        print("ADIOS, HASTA PRONTO")
        break
        
    
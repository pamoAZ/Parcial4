from typing import List, Optional
from unittest import result
from sqlmodel import Field, Session, Relationship, SQLModel, create_engine, select, col
from math import *


class Enlace(SQLModel, table=True):
    sustancia_id: Optional[int] = Field(
        default=None, foreign_key="sustancia.id", primary_key=True)
    coeficiente_emolar:Optional[int] = Field(
        default=None, foreign_key="coeficiente.emolar", primary_key=True)

class Sustancia(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    concentraciondeDisolucion: Optional[int] = Field(default=None, index=True)

    coeficientes: List["Coeficiente"] = Relationship(back_populates="sustancias", link_model=Enlace)

class Coeficiente(SQLModel, table=True):
    emolar: Optional[float] = Field(default=None, primary_key=True)
    absorbancia: Optional[float] = Field(default=None, index=True)
    caminoptico: Optional[float] = Field(default=None, index=True)

    sustancias: List["Sustancia"] = Relationship(back_populates="coeficientes", link_model=Enlace)

sqlite_file_name = "extincionMolar.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=False)

def crear_sustancia():

        concentraciondisolfinal= pedir_absorbancia/(pedir_emolar*pedir_caminoptico)
        pedir_nombre=input("Ingrese el nombre de la sustancia:\n")
        dato=Sustancia(nombre=pedir_nombre, concentraciondeDisolucion=concentraciondisolfinal)
        with Session(engine) as session:
            session.add(dato)
            session.commit()
        



def crear_coeficiente():
        global pedir_emolar, pedir_absorbancia, pedir_caminoptico

        pedir_emolar=float(input("Ingrese el coeficiente de extincion molar(L Mol ^-1-*m^1):\n"))
        pedir_absorbancia=float(input("Ingrese la absorbancia de la disolucion(adimensional):\n"))
        pedir_caminoptico=float(input("Ingrese el camino optico del coeficiente de extincion molar(m):\n"))
        dato=Coeficiente(emolar=pedir_emolar,absorbancia=pedir_absorbancia,caminoptico=pedir_caminoptico)

        with Session(engine) as session:
            session.add(dato)
            session.commit()

def menu():
    booleano=True
    while booleano:
        entrada=input("Seleccione una opcion:\n 1. coeficiente de Extincion molar y sustancia\n 2. Mostrar datos\n"\
                    " 3. Filtrar datos\n 4. Actualizar archivos\n 5. Eliminar datos\n 6. Salir\n Opción: ")
        if entrada == "1":          
            crear_coeficiente()
            crear_sustancia()
        elif entrada == "2":
            booleano_2=True
            while booleano_2:
                entrada_2=input("¿Que tabla quiere mostrar?:\n 1. Mostrar tabla sustancia\n 2. Mostrar tabla de coeficientes de Extincion molar\n3. Salir\n Opción: ")
                if entrada_2 == "1":
                    leer_datos_sustancia()
                elif entrada_2 == "2":
                    leer_datos_coeficiente()
                elif entrada_2 == "3":
                    booleano_2=False
                    break
                else:
                    print("Opcion invalida")
        elif entrada == "3":
            booleano_3=True
            while booleano_3:
                try:
                    entrada_3=float(input("Se va a filtrar la tabla ""coeficiente de Extincion molar"" por absorbancia menor a la que ingrese:\n"))
                    
                    filtrar_datos(entrada_3)
                    
                    booleano_3=False
                    break
                except:
                    print("Solo se permiten datos numericos")
        elif entrada == "4":
            booleano_4=True
            while booleano_4:
                try:
                    entrada_4=float(input("En la tabla ""coeficiente de Extincion Molar"", se va a actualizar dato con camino optico(m) por el que ingrese:\n"))
                    entrada_5=float(input("Ingrese el nuevo valor del camino optico (m):\n"))
                    actualizar_datos(entrada_4, entrada_5)
                    
                    booleano_4=False
                    break
                except:
                    print("Solo se permiten datos numericos")
        elif entrada == "5":
            booleano_5=True
            while booleano_5:
                try:
                    entrada_6=float(input("En la ""tabla coeficiente de Extincion Molar"", se va a borrar segun valor del coeficiente de extincion molar que ingrese:\n"))
                    
                    borrar_datos(entrada_6)
                    
                    booleano_5=False
                    break
                except:
                    print("Solo se permiten datos numericos")

        elif entrada == "6":
            booleano=False
            break
        else:
            print("Opción invalida")

def leer_datos_coeficiente():
    with Session(engine) as session:
        statement = select(Coeficiente)
        results = session.exec(statement)
        coeficientes = results.all()
        print(coeficientes)

def leer_datos_sustancia():
    with Session(engine) as session:
        statement = select(Sustancia)
        results = session.exec(statement)
        sustancias = results.all()
        print(sustancias)

def filtrar_datos(x):
    with Session(engine) as session:
        statement = select(Coeficiente).where(Coeficiente.absorbancia < x)
        results = session.exec(statement)
        for coeficiente in results:
            print(coeficiente)

def actualizar_datos(x,y):
    with Session(engine) as session:
        statement = select(Coeficiente).where(Coeficiente.caminoptico == x)
        results = session.exec(statement)
        coeficientes = results.one()
        print("coeficiente de Extincion Molar:", coeficientes)

        coeficientes.caminoptico = y
        session.add(coeficientes)
        session.commit()
        session.refresh(coeficientes)
        print("coeficiente de Extincion Molar actualizada:",coeficientes)

def borrar_datos(x):
    with Session(engine) as session:
        statement = select(Coeficiente).where(Coeficiente.emolar == x)
        results = session.exec(statement)
        coeficientes = results.one()
        print("coeficiente de Extincion Molar:", coeficientes)

        session.delete(coeficientes)
        session.commit()
        
        print("coeficiente de Extincion Molar eliminada:", coeficientes)

        statement = select(Coeficiente).where(Coeficiente.emolar == x)
        results = session.exec(statement)
        coeficiente = results.first()

        if coeficiente is None:
            print("No hay ningun coeficiente de Extincion Molar con esa característica")

def crear_extincionMolar_y_tablas():
    SQLModel.metadata.create_all(engine)

def main():
    crear_extincionMolar_y_tablas()  
    menu()


main()
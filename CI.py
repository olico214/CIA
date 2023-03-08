from tkinter import *
from tkinter import ttk
import tkinter as tk
import csv
from tkinter import filedialog
from openpyxl import Workbook
from tkinter import messagebox
import os
import openpyxl





class Buscador:
    def __init__(self):
        self.root = Tk()
        self.root.title("Buscador de CSV")
        self.root.geometry("1920x1080")
        
        
        style = ttk.Style()
        style.configure('blue.TFrame', background="#D7E6E8")
        style.configure('gris.TFrame', background="#DCDCDC")
        style.configure('rojo.TFrame', background="#EC8F8F")
        style.configure('yellow.TFrame', background="#F0E7AD")

        
        
        
        
        self.cuerpo= ttk.Frame(self.root)
        self.cuerpo.place(x=0,y=0,height=1080, width=1920)
        
        
        self.label = ttk.Label(self.root)
        self.label.place(x=10,y=40)
        
        self.text = ttk.Entry(self.root)
        self.text.place(x=10,y=60,width=200)

        self.button = ttk.Button(self.cuerpo,command=self.match, text="Buscar")
        self.button.place(x=80,y=80)
        
        self.information = ttk.Frame(self.root, style='rojo.TFrame' )
        self.information.place(x=0,y=0,height=28,width=1920)
        
        self.button2= ttk.Button(self.root,command=self.cargar, text="Cargar CSV")
        self.button2.place(x=450,y=1)
        
        self.button4= ttk.Button(self.root,command=self.exceltocsv, text="Excel to csv")
        self.button4.place(x=530,y=1)

        self.button5= ttk.Button(self.root,command=self.resetvalues, text="Limpiar Campos")
        self.button5.place(x=610,y=1)


        

        
        
        
        
        self.cuenta = ttk.Label(self.root, text="Coincidencias: 0")
        self.cuenta.place(x=10,y=130)
        
        
        
        
        
        

        # Crea el TreeView y configura su estilo
        self.tabla = ttk.Treeview(self.cuerpo, columns="resultado", style='yellow.TFrame')
        self.tabla.place(x=10, y=150, height=800, width=900)

        # Agrega las columnas y encabezados de columna
        self.tabla.heading("#0", text="Palabra Clave")
        self.tabla.column("#0", width=90)

        self.tabla.heading("resultado", text="Resultado")
        self.tabla.column("resultado", width=910)    
            
        
        
            
            
            
            #Fin de Tabla 1
        self.label2=ttk.Label(text="Ruta")
        self.label2.place(x=1500,y=130)

        self.button3= ttk.Button(self.cuerpo,command=self.copyrow, text="--->")
        self.button3.place(x=918,y=210)
            
        self.tabla2 = ttk.Treeview(self.cuerpo, columns="resultado", style='yellow.TFrame')
        self.tabla2.place(x=1000, y=150, height=150, width=900)
        
        self.tabla2.heading("#0", text="Palabra Clave")
        self.tabla2.column("#0", width=90)
        self.tabla2.heading("resultado", text="Resultado")
        self.tabla2.column("resultado", width=910)
            
        self.button3= ttk.Button(self.root,command=self.export_to_excel, text="Exporta a Excel")
        self.button3.place(x=1000,y=310)
        
    #Fin de Tabla 2
        self.datos = []
        self.file_path=""
        
        self.root.mainloop()
        


    def cargar(self):
        global curp  
        self.datos = []
        self.label2.config(text="Ruta")
        self.file_path = filedialog.askopenfilename()
        with open(self.file_path) as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                self.datos.extend(row)
        self.label2.config(text=self.file_path)
        messagebox.showinfo("Information", "Archivo cargado con exito")    

                        
                        
    def copyrow(self):
        
        for row_id in self.tabla.get_children():
            # Obtiene los valores de la fila actual
            values = self.tabla.item(row_id)["values"]
            # Inserta los valores en el segundo Treeview
            self.tabla2.insert("", "end", text=self.file_path, values=values)
        self.tabla.delete(*self.tabla.get_children())
        self.cuenta.config(text=0) 
            
            
            

    def export_to_excel(self):
        # Obtener los datos del Tree View en una lista
        data = []
        file_save = filedialog.asksaveasfilename()
        if file_save == "":
            messagebox.showinfo("Information", "Debe seleccionar un ruta")
            return 0
        for item in self.tabla2.get_children():
            values = []
            
            
            for value in self.tabla2.item(item)['values']:
                values.append(value)
            data.append(values)
        
        # Crear un nuevo archivo de Excel
        wb = Workbook()
        ws = wb.active
        nwdata = []
        for row in data:
            
            ws.append(row)
            
            

        # Guardar el archivo de Excel
        wb.save(file_save + ".xlsx")
        
        self.tabla.delete(*self.tabla.get_children())
        self.tabla2.delete(*self.tabla2.get_children())
        
        messagebox.showinfo("Information", "Exportación finalizada")                
                    
                    
                    
                    



    def exceltocsv(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path == "":
            messagebox.showinfo("Information", "Proceso Cancelado")
            return 0
        # creating or loading an excel workbook
        newWorkbook = openpyxl.load_workbook(self.file_path)
        # getting the active workbook sheet(Bydefault-->Sheet1)
        firstWorksheet = newWorkbook.active
        # Opening a output csv file in write mode
        self.file_path=""
        self.file_path = filedialog.asksaveasfilename()
        self.file_path =self.file_path + ".csv"
        if self.file_path == ".csv":
            messagebox.showinfo("Information", "Proceso Cancelado")
            return 0
        OutputCsvFile = csv.writer(open(self.file_path, 'w'), delimiter=";")
        # Traversing in each row of the worshsheet
        a=0
        for eachrow in firstWorksheet.rows:
            # Writing data of the excel file into the result csv file row-by-row
            try:
                
                OutputCsvFile.writerow([cell.value for cell in eachrow])
            except Exception as e: print(e)

        with open(self.file_path) as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                self.datos.extend(row)

        self.label2.config(text=self.file_path)
        messagebox.showinfo("Information", "Archivo cargado con exito") 





                    
    def match(self):
        nwdato = self.text.get()
        dato = nwdato.lower() 
        
        ava = 0
        self.tabla.delete(*self.tabla.get_children())
            
        if dato == "":
            self.label.configure(text="Debe escribir un caracter....")
            self.cuenta.config(text=0) 
            
            return 0
        self.label.configure(text="")
        valores = []
        for ban in self.datos:
            cadena = ban.lower()

            #print(cadena)
            if dato in cadena :  # si el dato coincide con un elemento de la lista
                campo1 = dato
                ava = ava +1
                valores.append(ban)
                self.tabla.insert("", "end", text=campo1, values=(valores))
                self.cuenta.config(text="coincidencias: " + str(ava)) 
                valores = []
                    
                    
                    
            
                
                
                
    def resetvalues(self):
        self.datos = []
        self.tabla.delete(*self.tabla.get_children())
        self.tabla2.delete(*self.tabla2.get_children())
        self.label2.config(text="Ruta")
        self.cuenta.config(text="coincidencias: 0" ) 
        

aplicacion1 = Buscador()
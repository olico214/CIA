from tkinter import *
from tkinter import ttk
import tkinter as tk
import csv
from tkinter import filedialog
from openpyxl import Workbook
from tkinter import messagebox
import os
import openpyxl
import pyperclip




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
        
        
        self.label = ttk.Label(self.root,text="Palabra Clave")
        self.label.place(x=10,y=40)
        
        self.text = ttk.Entry(self.root)
        self.text.place(x=10,y=60,width=200)

        self.button = ttk.Button(self.cuerpo,command=self.match, text="Buscar")
        self.button.place(x=80,y=80)
        
        self.information = ttk.Frame(self.root, style='gris.TFrame' )
        self.information.place(x=0,y=0,height=28,width=1920)
        
        self.button2= ttk.Button(self.root,command=self.cargar, text="Cargar CSV")
        self.button2.place(x=450,y=1)

        
        
        self.button4= ttk.Button(self.root,command=self.exceltocsv, text="Excel to csv")
        self.button4.place(x=530,y=1)

        

        self.button5= ttk.Button(self.root,command=self.resetvalues, text="Limpiar Campos")
        self.button5.place(x=610,y=1)

        self.button3= ttk.Button(self.root,command=self.export_to_excel, text="Exporta a Excel")
        self.button3.place(x=710,y=1)


        

        
        
        
        
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
        

        self.log=""

        self.popup1 = tk.Menu(self.tabla, tearoff=0)
        self.popup1.add_command(
            command=self.your_copy,
            label="Copy",
            )
        
        self.popup2 = tk.Menu(self.tabla, tearoff=0)
        self.popup2.add_command(
            command=self.transfer,
            label="Tranferir",
            )
        
        self.tabla.bind('<Button-3>', self.popup_menu)
        self.tabla.bind('<Button-1>', self.popup2_menu)
        

        
            
            
            
            #Fin de Tabla 1
        self.label2=ttk.Label(text="Ruta")
        self.label2.place(x=1500,y=1)

        self.button3= ttk.Button(self.cuerpo,command=self.copyrow, text="--->")
        self.button3.place(x=918,y=825)
            
        self.tabla2 = ttk.Treeview(self.cuerpo, columns="resultado", style='yellow.TFrame')
        self.tabla2.place(x=1000, y=750, height=150, width=900)
        
        self.tabla2.heading("#0", text="Palabra Clave")
        self.tabla2.column("#0", width=90)
        self.tabla2.heading("resultado", text="Resultado")
        self.tabla2.column("resultado", width=910)






        #Configuracion de Filtros
        self.dataframe =ttk.Frame(self.root,style='gris.TFrame',borderwidth=3, relief="solid")
        self.dataframe.place(x=1000,y=200,height=80,width=700)

        self.avanzado=ttk.Label(self.root, text="Filtro Avanzado")
        self.avanzado.place(x=1300,y=180)

        #Filtro 1
        self.campo1label = ttk.Label(self.dataframe,text="Campo 1",background='#DCDCDC')
        self.campo1label.place(x=85,y=10)
        self.campo1=ttk.Entry(self.dataframe)
        self.campo1.place(x=10,y=30,width=200)
        
        #Filtro 2
        self.campo2label = ttk.Label(self.dataframe,text="Campo 2",background='#DCDCDC')
        self.campo2label.place(x=330,y=10)
        self.campo2=ttk.Entry(self.dataframe)
        self.campo2.place(x=250,y=30,width=200)

        #Filtro 3
        self.campo3label = ttk.Label(self.dataframe,text="Campo 3",background='#DCDCDC')
        self.campo3label.place(x=560,y=10)
        self.campo3=ttk.Entry(self.dataframe)
        self.campo3.place(x=490,y=30,width=200)

        self.buttonavanzado = ttk.Button(self.root,text="Busqueda Avanzada", command=self.filter1)
        self.buttonavanzado.place(x=1300,y=300)

       


            
        
        
    #Fin de Tabla 2
        self.datos = []
        self.file_path=""
        self.valores = []
        
        self.root.mainloop()


    
        

    def your_copy (self):
        selections = self.tabla.selection()  # get hold of selected rows

        copied_string = ""
        for row in selections:
            values = self.tabla.item(row, 'values')  # get values for each selected row

            for item in values:
                copied_string += f"{item}  "

        pyperclip.copy(copied_string)

    def popup_menu(self,event):
        self.tabla.identify_row(event.y)
        self.popup1.post(event.x_root, event.y_root)





    def transfer(self):
        selections = self.tabla.selection()  # get hold of selected rows

        copied_string = ""
        for row in selections:
            value1 = self.tabla.item(row, 'values')  # get values for each selected row

            #for item in values:
                #copied_string += f"{item}  "

        self.tabla2.insert("", "end", text=self.file_path, values=value1)
        
    def popup2_menu(self,event):
        self.tabla.identify_row(event.y)
        self.popup2.post(event.x_root, event.y_root)

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
                    
                    
                    
            
                
    def filter1(self):
        try:
            campo1 = self.campo1.get()
            campo2 = self.campo2.get()
            campo3 = self.campo3.get()
            

            if campo1 == "":
                return 0
            varian = 3
            
            while varian > 0:
                campo = ""
                if len(campo3)>0:
                    varian =3
                    campo = campo3
                    campo3=""
                elif len(campo2)>0:
                    varian =2
                    campo = campo2
                    campo2=""
                elif len(campo1)>0:
                    varian =0
                    campo = campo1
                    campo1=""

                
                campo = campo.lower()
                
                
                self.cuenta.config(text="coincidencias: 0" )
                ava = 0
                valores = []
                valor = []
                for row_id in self.tabla.get_children():
                    valor.extend( self.tabla.item(row_id)["values"])
                self.tabla.delete(*self.tabla.get_children())    
                for ban in valor:
                    
                    ban = ban.lower()
                    if campo in ban:

                        ava = ava +1
                        valores.append(ban)
                        self.tabla.insert("", "end", text=campo, values=(valores))
                        self.cuenta.config(text="coincidencias: " + str(ava)) 
                        valores = []
                #self.tabla.delete(*self.tabla.get_children())
        except:        
            print("Proceso no valido")

                        
    def resetvalues(self):
        self.datos = []
        self.tabla.delete(*self.tabla.get_children())
        self.tabla2.delete(*self.tabla2.get_children())
        self.label2.config(text="Ruta")
        self.cuenta.config(text="coincidencias: 0" ) 
        self.campo1.delete(0,'end')
        self.campo2.delete(0,'end')
        self.campo3.delete(0,'end')
        



        

            

aplicacion1 = Buscador()
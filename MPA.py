from tkinter import *
from tkinter import ttk
import tkinter as tk




class model_IA():
    def stringtobytes(self):
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


        self.button6= ttk.Button(self.root,command=self.convertbyt, text="Analizar IA")
        self.button6.place(x=1800,y=720)






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
        
aplication = model_IA()
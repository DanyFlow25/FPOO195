from tkinter import messagebox
import sqlite3
import bcrypt

class Controlador:
    def conexion(self):
        try:
            conex = sqlite3.connect("C:/Users/Danie/Documents/UPQ/CUATRIMESTRE 5/Programación Orientada a objetos/Git/FPOO195/Tkinter y SQLite/db 195.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo conectar")

    def encriptapass(self, cont):
        passPlana = cont.encode()
        sal = bcrypt.gensalt()
        passHash = bcrypt.hashpw(passPlana, sal)
        return passHash

    def insertUsuario(self, nom, corr, cont):
        conexion = self.conexion()
        if nom == "" or corr == "" or cont == "":
            messagebox.showwarning("Cuidado", "Inputs vacíos")
            conexion.close()
        else:
            cursor = conexion.cursor()
            conH = self.encriptapass(cont)
            datos = (nom, corr, conH)
            sqlinsert = "INSERT INTO tbUsuarios(nombre, correo, contrasena) VALUES (?, ?, ?)"
            
            cursor.execute(sqlinsert, datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Registro exitoso!")

    def buscarUsuario(self, id):
        conex = self.conexion()
        
        if id == '':
            messagebox.showwarning("Cuidado", "Inputs vacíos, no seas tibio")
            conex.close()
        else:
            try:
                cursor = conex.cursor()
                sqlSelect = f"Select * from tbUsuarios where id={id}"
                cursor.execute(sqlSelect)
                usuario = cursor.fetchall()
                conex.close()
                return usuario
            except sqlite3.OperationalError:
                print("No se pudo ejecutar la búsqueda") 
# Creación de la función para Consultar Usuarios            
    def consultarUsuarios(self):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "select * from tbUsuarios"
            cursor.execute(sqlSelect)
            usuarios = cursor.fetchall()
            conexion.close()
            return usuarios
        
        except sqlite3.OperationalError:
            print("Error al consultar usuarios")

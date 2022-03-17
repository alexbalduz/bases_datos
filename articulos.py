import mysql.connector

class Articulos:

    def abrir(self):
        conexion=mysql.connector.connect(host="ec2-34-224-226-38.compute-1.amazonaws.com",user="ufcvyyxsydvutt",passwd="739b1428db36ed90efd2b19a3b1423af8065b762b31fdfd56afead3455330b9c",database="da704k77u522r")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(descripcion, precio) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
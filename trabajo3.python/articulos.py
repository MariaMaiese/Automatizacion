import mysql.connector

class Articulos:
        def abrir(self):
                conexion1=mysql.connector.connect(host="localhost", user="root", passwd="",database="tarea3")
                return conexion1

        def consulta(self,datos):
                conexion=self.abrir()
                cursor=conexion.cursor()
                sql = "select nombre_producto, descripcion from productos where sku=%s"
                cursor.execute(sql,datos)
                conexion.close()
                return cursor.fetchall()


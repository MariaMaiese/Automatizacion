import mysql.connector

class Cliente:
        def abrir(self):
                conexion1=mysql.connector.connect(host="localhost", user="root", passwd="",database="tarea3")
                return conexion1

        def consulta(self,mantisa):
                conexion=self.abrir()
                cursor=conexion.cursor()
                #self.dv = datos[len(datos)-1]
                #self.mantisa = datos[:-1]
                sql = f"select id_cliente,nombre_cliente,apellido_pat, apellido_mat from clientes where mantisa = {mantisa}" 
                cursor.execute(sql)
                conexion.close()
                return cursor.fetchall()
 
        def recuperar_datos(self,idcliente):
                conexion=self.abrir()
                cursor=conexion.cursor()
                sql=f"""select ventas.id_venta, ventas.fecha_venta,ventas.cantidad, productos.nombre_producto, ventas.total_venta, ventas.id_cliente from ventas 
                inner join productos on productos.id_producto = ventas.id_producto
                where id_cliente = {idcliente}"""
                cursor.execute(sql)
                conexion.close()
                return cursor.fetchall()
 
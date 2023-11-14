from .entities.users import User

class ModelUsers:
    @classmethod
    def login(self, db, user):
       
        try:
            
            cursor = db.connection.cursor()
            cursor.execute("call sp_verifyIdentity(%s, %s)", (user.username, user.password))
      
            
            row = cursor.fetchone()
            if row and len(row) >= 5:
                print("Resultados de la consulta:", row)
                user = User(row[0], row[1], row[2], row[4], row[3])
                return user
            else:
                user = None  # Otra acción apropiada en tu lógica
        except Exception as ex:
            print("Error en el modelo de usuarios:", ex)
            raise Exception(ex)



import mysql.connector


class Personas():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='qqwdwsedy6y55bwq',
                password='bgwgnj19klw9wsgx',
                host='s554ongw9quh1xjs.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                port=3306,
                database='hd331w2qe3rpldjj'
            )

            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)
    def select(self):
        try:
            self.connect()
            query = ("SELECT * FROM students;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                r = {
                    'matricula':row[1],
                    'nombre':row[2],
                    'pri_ap':row[3],
                    'seg_ap':row[4],
                    'age':row[5],
                    'fdate':row[6],
                    'gender':row[7],
                    'state':row[8]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result
    def view(self,matricula):
        try:
            self.connect()
            query = ("SELECT * FROM students WHERE matricula = %s;")
            values = (matricula,)
            self.cursor.execute(query,values)
            result = []
            for row in self.cursor:
                diccionario = {
                   'matricula':row[1],
                    'nombre':row[2],
                    'pri_ap':row[3],
                    'seg_ap':row[4],
                    'age':row[5],
                    'fdate':row[6],
                    'gender':row[7],
                    'state':row[8]
                }
                result.append(diccionario)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)

    def insert(self, matricula, nombre, pri_ap, seg_ap, age, fdate, gender, state):
        try:
            self.connect()
            query = ("INSERT INTO students(matricula,nombre,pri_ap,seg_ap,age,fdate,gender,state) values(%s,%s,%s,%s,%s,%s,%s,%s);")
            values = (matricula,nombre,pri_ap,seg_ap,age,fdate,gender,state)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, matricula, nombre, pri_ap, seg_ap, age, fdate, gender, state):
        try:
            self.connect()
            query = ("UPDATE students SET nombre=%s, pri_ap=%s,seg_ap=%s,age=%s,fdate=%s,gender=%s,state=%s WHERE matricula=%s;")
            values = (nombre, pri_ap, seg_ap, age, fdate, gender, state,matricula )
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

            
    def delete(self, matricula):
        try:
            self.connect()
            query = ("DELETE FROM students WHERE matricula= %s;")
            values = (matricula,)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

objeto = Personas()
objeto.connect() 
#objeto.insert("1718110388","lupita","espinoza","riveros","20","2000/04/05","Femenino","Hidalgo")
for row in objeto.select():
    print(row)
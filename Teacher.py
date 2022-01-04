# import psycopg2
# conn = psycopg2.connect(
   # database="postgres", user='postgres', password='root', host='127.0.0.1', port= '5432'
# )
# print(conn)

#Creating a cursor object using the cursor() method
# cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
# cursor.execute("select version()")

# Fetch a single row using fetchone() method.
# data = cursor.fetchone()
# print("Connection established to: ",data)

#Closing the connection
# conn.close()
# Connection established to: (
#    'PostgreSQL 11.5, compiled by Visual C++ build 1914, 64-bit',
# )


class Employee:
   fb='yes'
   t='ajay'
   print(fb)
   # print(t)
   def __int__(self):
      self.price
      self.model
      print(self.model)
   @classmethod
   def view(self,p,m):
      self.price=p
      self.model=m
      print('total price:',self.price)
      print('model name:',self.model)
s=Employee()
# Employee.view('vivo',10)
# Employee.t
# Employee.fb
s.t
s.view('h',6)
# Employee.fb





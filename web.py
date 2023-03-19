#!C:\Users\USER\AppData\Local\Programs\Python\Python310\python.exe
print("Content-Type: text/html\n\n")
import cgi

# import sys
# sys.path.append("c:\users\user\appdata\local\programs\python\python310\lib\site-packages")

import random
import psycopg2
import psycopg2.extras

form = cgi.FieldStorage()
entries = form.getvalue("entries")
select1 = form.getvalue("select")

# Configuration Values - 
hostname = 'localhost'
database = 'contacts'
username = 'postgres'
pwd = 'babin2002'
port_id = 5432

# Setting Up Connection - 
connection = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port = port_id
)

curr = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

curr.execute("DELETE FROM contactNumbers;")

def databaseOperations(req):

    for i in range(1,req+1):
        curr.execute("INSERT INTO contactNumbers VALUES (" + str(i) + "," + str(random.randint(7000000000,9999999999)) + ");")

    curr.execute("SELECT * FROM contactNumbers;")
    return curr.fetchall()

output = databaseOperations(int(entries))

connection.commit()

curr.close()
connection.close()

result_page = '''<table>
                    <thead>
                        <tr>
                        <th>ID</th>
                        <th>Contact Number</th>
                        </tr>
                    </thead>
                    <tbody>'''
for record in output:
    result_page += "<tr> <td>%s</td> <td>%s</td> </tr>" % (record['id'], record['contact'])

result_page += "</tbody> </table>"
print("<h1>Records Entered Successfully</h1>")

print(result_page)
import sqlite3

con = sqlite3.connect('coffee.db')
cur = con.cursor()
List = []
Catlist = []

cur.execute('''SELECT * FROM Tbl WHERE Category == "Coffee"''')
List.append(cur.fetchall())
Coffee = "Coffee"
Catlist.append(Coffee)
cur.execute('''SELECT * FROM Tbl WHERE Category == "Tea"''')
List.append(cur.fetchall())
Tea = "Tea"
Catlist.append(Tea)
cur.execute('''SELECT * FROM Tbl WHERE Category == "Dairy"''')
List.append(cur.fetchall())
Dairy = "Dairy"
Catlist.append(Dairy)
cur.execute('''SELECT * FROM Tbl WHERE Category == "Condiments"''')
List.append(cur.fetchall())
Condiments = "Condiments"
Catlist.append(Condiments)
cur.execute('''SELECT * FROM Tbl WHERE Category == "Paper"''')
List.append(cur.fetchall())
Paper = "Paper"
Catlist.append(Paper)

Catlist.sort()

Category = "Category"
Product = "Product"
Supplier = "Supplier"
print(f"{Category:^15}{Product:^30}{Supplier:^20}")
print("="*14 + " " + "="*29 + " " + "="*19)
for k in Catlist:
    for j in List:
        for i in j:
            if i[2] == k:
                if j.index(i) == 0:
                    print(f"{i[2]:15} {i[1]:30} {i[3]:20}")
                else:
                    print(f"{' '*15} {i[1]:30} {i[3]:20}")
    print()
import mysql.connector

def create_record(id, nama, tempat_tinggal):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="data"
    )

    mycursor = mysb.cursor()

    sql = "INSERT INTO data_diri (id, nama, tempat_tinggal) VALUES (%s, %s, %s)"
    val = (id, nama, tempat_tinggal)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mysb.close()

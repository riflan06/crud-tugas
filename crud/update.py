import mysql.connector

def update_record(id,  nama, tempat_tinggal ):
    try:
        mysb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="data"
        )

        mycursor = mysb.cursor()

        sql = "UPDATE data_diri SET id = %s, nama = %s, tempat_tinggal = %s WHERE id = %s"
        val = (id, nama, tempat_tinggal, id)
        print("Executing SQL:", sql % val)  # Debug statement
        mycursor.execute(sql, val)

        mysb.commit()
        
        print(mycursor.rowcount, "record(s) affected")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        mycursor.close()
        mysb.close()

# Example usage

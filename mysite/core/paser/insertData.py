import psycopg2

def insertCheckBox(list_of_lists):
    conn = psycopg2.connect(database="aaadb", user='teamaaa', password='aaapass', host='localhost', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    print("Records inserted........")

    conn.close()
    return 1
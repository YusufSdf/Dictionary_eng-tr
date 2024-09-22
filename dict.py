import mysql.connector
import random
import os

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Yusuf2005.",
    database = "eng-tr"
)

cursor = db.cursor()


cont = input("giriş - çıkış: ").lower()
while cont == "giriş":
    os.system("cls")
    menü = input("kelimeleri gör: 1\nkelime ekle: 2\nkelime düzelt: 3\nkelime sor: 4\n")
    os.system("cls")

    if menü == "1": #kelime görme
        cursor.execute("SELECT id,tr,eng FROM dict")
        res = cursor.fetchall()
        print(res)

    elif menü == "2": # kelime ekleme
        os.system("cls")
        english = input("ingilizce kelime: ")
        türkçe = input("türkçe karşılığı: ")
        sql = cursor.execute("INSERT INTO dict VALUES(%s,%s,%s)",(None,english,türkçe))
        db.commit()


    # elif menü == "3":
    #     delete = input("silmek istenilen id= ")
    #     sql = cursor.execute("DELETE FROM dict WHERE id=(%s)",(delete))
    #     db.commit()


    elif menü == "3": #kelime düzelt
        os.system("cls")
        english = input("ingilizce kelime: ")
        türkçe = input("türkçe karşılığı: ")
        id = input("id: ")
        sql = cursor.execute("UPDATE dict SET eng=%s, tr=%s WHERE id=%s",(english,türkçe,id))
        db.commit()

    elif menü == "4": # kelime sorma
        os.system("cls")
        whl = True
        while whl == True:
            os.system("cls")
            cursor.execute("SELECT COUNT(*) FROM dict")
            result = cursor.fetchall()
            word_id = random.randint(1,result[0][0])

            cursor.execute("SELECT eng FROM dict WHERE id=%s",([word_id]))
            eng = cursor.fetchone()

            cursor.execute("SELECT tr FROM dict WHERE id=%s",([word_id]))  
            tr= cursor.fetchone()    

            print(tr[0])
            translate = input("İngilizcesi: ").lower()
            if translate == eng[0]:
                print("Doğru")
            else:
                print("Yanlış")

                whl = False


    cont = input("giriş - çıkış: ").lower()

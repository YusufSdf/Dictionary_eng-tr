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


def results():
    cursor.execute("SELECT id,tr,eng FROM dict")
    res = cursor.fetchall()
    print(res)

def correction():
    english = input("ingilizce kelime: ")
    türkçe = input("türkçe karşılığı: ")
    id = input("id: ")
    sql = cursor.execute("UPDATE dict SET eng=%s, tr=%s WHERE id=%s",(english,türkçe,id))
    db.commit()


def addWord():
    english = input("ingilizce kelime: ")
    cursor.execute("SELECT eng FROM dict")
    control = cursor.fetchall()
    for i in control:
        if i[0] == english:
            print("Bu kelime zaten var!")
            break
        else:
            türkçe = input("türkçe karşılığı: ")
            sql = cursor.execute("INSERT INTO dict VALUES(%s,%s,%s)",(None,english,türkçe))
            db.commit()
            break

def question():
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
while cont == "giriş":
    os.system("cls")
    menü = input("kelimeleri gör: 1\nkelime ekle: 2\nkelime düzelt: 3\nkelime sor: 4\n")
    os.system("cls")

    if menü == "1": #kelime görme
        results()

    elif menü == "2": # kelime ekleme
        os.system("cls")
        addWord()


    # elif menü == "5":
    #     delete = input("silmek istenilen id= ")
    #     sql = cursor.execute("DELETE FROM dict WHERE id=(%s)",([delete]))
    #     db.commit()


    elif menü == "3": #kelime düzelt
        os.system("cls")
        correction()

    elif menü == "4": # kelime sorma
        os.system("cls")
        question()

    cont = input("giriş - çıkış: ").lower()

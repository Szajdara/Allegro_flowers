import sqlite3

conn = sqlite3.connect('my_database_flowers.db')
cursor = conn.cursor()

# Dodanie kolumny name (jeśli jej jeszcze nie ma)
try:
    cursor.execute("ALTER TABLE flowers ADD COLUMN user TEXT")
    print("Dodano kolumnę 'user'.")
except sqlite3.OperationalError:
    print("Kolumna 'user' już istnieje.")

conn.commit()
conn.close()



# import sqlite3
# import os

# conn = sqlite3.connect("my_database_flowers.db")
# cursor = conn.cursor()

# # Ścieżka do zdjęcia (zmień na swoją)
# image_filename = "żurawkafire.jpg"
# image_path = f"images/{image_filename}"  

# # Dodanie kwiatu do bazy
# cursor.execute('''
#     INSERT INTO flowers (id, name, color, price, mrozoodpornosc, wysokosc, szerokość, image_path, opis) 
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
# ''', (24, "Żurawka", "Czerwony", 18, "wysoka", 25, 25, image_path, "'Cajun Fire' to z pewnością odmiana zasługująca na uznanie. Otóż jest to żurawka, która zmienia kolory w trakcie sezonu! Wiosną liście są czerwone, latem prawie czarne, a jesienią kasztanowe. Co więcej w czerwcu i lipcu na ciemnych łodygach pojawiają się liczne białe kwiaty! Odmiana ta jest atrakcyjna przez cały sezon i stale przykuwa uwagę miłośników roślin."))

# conn.commit()
# conn.close()

# print(f"Dodano nowy wpis z obrazkiem: {image_path}")



# import sqlite3

# # Połączenie z bazą danych (lub utworzenie jej, jeśli nie istnieje)
# conn = sqlite3.connect("my_database_flowers.db")  
# cursor = conn.cursor()

# # Tworzenie tabeli 'flowers'
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS flowers (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         color TEXT,
#         price REAL,
#         mrozoodpornosc TEXT,
#         wysokosc INTEGER,
#         szerokość INTEGER,
#         image_path TEXT,
#         opis TEXT,
#         rating INTEGER DEFAULT 0
#     )
# ''')

# # Zapisanie zmian i zamknięcie połączenia
# conn.commit()
# conn.close()

# print("Tabela 'flowers' została dodana do bazy danych.")

# import sqlite3

# conn = sqlite3.connect("my_database_flowers.db")
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM Flowers")
# rows = cursor.fetchall()

# if rows:
#     print("Dane w tabeli 'users':")
#     for row in rows:
#         print(row)
# else:
#     print("Tabela 'users' jest pusta.")

# conn.close()

# import sqlite3

# # Połączenie z bazą danych (lub jej utworzenie, jeśli nie istnieje)
# conn = sqlite3.connect("my_database_flowers.db")
# cursor = conn.cursor()

# # Dodanie nowej kolumny do tabeli (np. 'users')
# try:
#     cursor.execute("ALTER TABLE Flowers ADD COLUMN name TEXT;")
#     conn.commit()
#     print("Kolumna dodana pomyślnie!")
# except sqlite3.Error as e:
#     print("Błąd:", e)

# # Zamknięcie połączenia
# conn.close()



# import sqlite3

# # Połączenie z bazą danych
# conn = sqlite3.connect("my_database.db")
# cursor = conn.cursor()

# # Słownik z danymi: {id: wartość dla condition}
# dane_do_aktualizacji = {
#     1: "trained as a barista, famous on TikTok™, has a child, WARNING: won’t text back",
#     2: "only cheated on one boyfriend, horse girl, sometimes actually does feel like a plastic bag",
#     3: "is really into the color red, believes that Epstein didn’t kill himself, recently started a podcast"
# }

# # Aktualizacja danych dla każdego id
# try:
#     for id_wiersza, condition_value in dane_do_aktualizacji.items():
#         cursor.execute("UPDATE Users SET description = ? WHERE id = ?;", (condition_value, id_wiersza))
    
#     conn.commit()
#     print("Dane zostały zaktualizowane pomyślnie!")
# except sqlite3.Error as e:
#     print("Błąd:", e)

# # Zamknięcie połączenia
# conn.close()




# import sqlite3

# # Połączenie z bazą danych
# conn = sqlite3.connect("my_database.db")
# cursor = conn.cursor()

# # Dodanie kolumny 'condition' typu TEXT
# try:
#     cursor.execute("ALTER TABLE Users ADD COLUMN height ;")
#     conn.commit()
#     print("Kolumna 'color' została dodana pomyślnie!")
# except sqlite3.Error as e:
#     print("Błąd:", e)

# # Zamknięcie połączenia
# conn.close()


# import sqlite3

# # Устанавливаем соединение с базой данных
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()

# # Добавляем нового пользователя
# cursor.execute('INSERT INTO Users (id, name, age, price, rating) VALUES (?, ?, ?, ?, ?)', ('8', 'Franek', 33, 333, None))

# # Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()

# import sqlite3;
# def insert_file_path(record_id, file_path):
#     conn = sqlite3.connect('my_database.db')
#     cursor = conn.cursor()

#     cursor.execute("UPDATE Users SET file_path = ? WHERE id = ?", (file_path, record_id))

#     conn.commit()
#     conn.close()

# # Przykładowe użycie (wstawienie ścieżki do rekordu o ID 1)
# insert_file_path(8, "images/franek.jpg")


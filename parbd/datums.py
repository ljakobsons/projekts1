import datetime

with open("Rezultats.txt", "w", encoding="UTF-8") as f:
    f.write("Larss Jākobsons\n")
    f.write(f"Datums: {datetime.datetime.now().strftime('%Y-%m-%d')}")

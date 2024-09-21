with open("quetes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
a = input("11?")

with open("quetes.txt", "a", encoding="utf-8") as file:
    file.write(f"({a})\n")

while True:
    an = input("12?").lower()
    if an=="y":
            q = input("22?")
            a = input("11?")

            with open("quetes.txt", "a", encoding="utf-8") as file:
                file.write(f"{q}\n(){a}\n")
    else:
         break

with open("quetes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
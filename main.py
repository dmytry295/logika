with open("quotes.txt","r",encoding= "utf-8") as file:
    data = file.read()
    print(data)

author = input("Хто написав ці рядки?")

with open("quotes.txt","a",encoding= "utf-8") as file:
    file.write("author + \n")
answer = input("Бажаєте додати ще одну цитату? (так / ні) - ")
answer = answer.lower()

while True:
    if answer == "так":
        quotes = input("Введіть цитату:")
        author = input("Введіть автора:")

        file = open ("quotes.txt","a", encoding = "utf-8")
        file.write(quotes + "\n")
        file.write("( "+ author + ")"+ "\n")
        file.close()

    else :
        break


print("зчитуємо фінальний файл:")
with open("quotes.txt","r",encoding= "utf-8") as file:
    for line in file: 
        print(line)






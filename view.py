from file1 import create, read, read_one, update, delete, read_category
import tabulate


def main():
    n = int(input("""1: Yangi maxsulot qo'shish
2: Barcha maxsulotlarni ko'rish
3: Bitta maxsulotni ko'rish
4: Maxsulot ma'lumotlarini o'zgartish
5: Maxsulotni o'chirish
6: Kategoriya bo'yicha saralash
7: Dasturdan chiqish

Buyruq raqam kiriting: """))

    if(n == 1):
        print("\nYangi maxsulot qo'shish")
        name = input("Maxsulot nomimi kiriting: ")
        price = float(input("Maxsulot narxini kiriting: "))
        create(name, price)
        print("Maxsulot qo'shildi\n")

    elif(n == 2):
        print("\nBarcha maxsulotlarni ko'rish")
        headers = ["ID", "Product", "Price", "Category"]
        data = read()
        table = tabulate.tabulate(data, headers, tablefmt="grid")
        print(table, "\n")

    elif(n == 3):
        print("\nBitta maxsulot ko'rish")
        id = int(input("Maxsulot id'sini kiriting: "))
        print(read_one(id), "\n")

    elif(n == 4):
        print("\nMaxsulot ma'lumotlarini o'zgartish")
        id = int(input("Maxsulot id'sini kiriting: "))
        name = input("Maxsulotning yangi nomini kiriting: ")
        price = float(input("Maxsulotning yangi narxini kiriting: "))
        update(id, name, price)
        print("Maxsulot ma'lumotlari o'zgartirildi\n")

    elif(n == 5):
        print("\nMaxsulotni o'chirish")
        id = int(input("Maxsulot id'sini kiriting: "))
        delete(id)
        print("Maxsulot o'chirildi\n")

    elif(n == 6):
        print("Kategoriya bo'yicha saralash")
        id = int(input("Kategoriya id'sini kiriting: "))
        headers = ["ID", "Product", "Price", "Category"]
        data = read_category(id)
        table = tabulate.tabulate(data, headers, tablefmt="grid")
        print(table, "\n")

    else:
        return 0
    main()

main()
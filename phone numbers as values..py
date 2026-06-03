phone_book = {}


n = int(input())

for _ in range(n):
    command = input().split()
    
    if command[0] == "ADD":
        name = command[1]
        phone_number = command[2]

        phone_book[name] = phone_number
    
    elif command[0] == "REMOVE":
        name = command[1]
        phone_book.pop(name, None)
    
    elif command[0] == "DISPLAY":
        if not phone_book:
            print("No contacts")
        else:
            for name in sorted(phone_book.keys()):
                print(f"{name}: {phone_book[name]}")

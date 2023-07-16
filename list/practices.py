def httpRequest(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 200:
            return "OK"

#print(httpRequest(400))

current_choice = "-"
empty_list = []
available_parts = ["Salir", "Teclado", "Mouse", "Monitor", "CPU", "Impresora"]

while current_choice != "0":
    if current_choice in "12345":
        print(f"Adding #{current_choice}")
        match current_choice:
            case "1":
                empty_list.append("Teclado")
            case "2":
                empty_list.append("Mouse")
            case "3":
                empty_list.append("Monitor")
            case "4" :
                empty_list.append("CPU")
            case _:
                empty_list.append("Impresora")
    else:
        for part in available_parts:
            print(f"#{available_parts.index(part)}: #{part}")
    current_choice = input("Elige la opción a agregar:")
print(empty_list)
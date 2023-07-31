def httpRequest(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 200:
            return "OK"

#print(httpRequest(400))

# current_choice = "-"
# empty_list = []
# available_parts = ["Teclado", "Mouse", "Monitor", "CPU", "Impresora"]
# valid_options = []

# for i in range(1, len(available_parts) + 1):
#     valid_options.append(str(i))
# print (valid_options)

# while current_choice != "0":
#     if current_choice in "12345":
#         index = int(current_choice) -1
#         chosen_part = available_parts[index]
#         if chosen_part in empty_list:
#             print(f"Removing #{current_choice}")
#             empty_list.remove(chosen_part)
#         else:
#             print(f"Adding #{current_choice}")
#             empty_list.append(chosen_part)        
#     else:
#         for number, part in enumerate(available_parts):
#             print(f"#{number + 1}: #{part}")
#     current_choice = input("Elige la opción a agregar:")
# print(empty_list)

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# flowers = []
# shrubs = []

# for i in data:
#     if "Flower" in i:
#         f = i.split("-")[0].rstrip()
#         flowers.append(f)
#     else:
#         shrubs.append(i.split("-")[0].rstrip())
# print(flowers)
# print(shrubs)



ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)

#Deleting elements

data = [4, 5, 104, 130, 175, 198, 200, 230, 250, 300]
min_value = 100
max_value = 200

#Deleting min value
stop = 0
for index, value in enumerate(data):
  if value >= min_value:
    stop = index
    break

print(data)
del data[:stop]
print(data)


#Deleting max value
start = 0
for index in range(len(data) -1, -1, -1):
  if data[index] > max_value:
    start = index
    break

print(data)
del data[start:]
print(data)


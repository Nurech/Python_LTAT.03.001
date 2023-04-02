inventory = {}

done = False

while not done:
    response = input('Enter a word (done to quit): ')
    if response == 'done':
        done = True
        break

    if response in inventory:
        print(response + " means " + inventory[response])
    else:
        print('There is no information for', response)
        res = input("What does " + response + " mean? ")
        inventory[response] = res

print("Total number of words in the dictionary:", len(inventory))

for word, translation in inventory.items():
    print(f"{word} means {translation}")

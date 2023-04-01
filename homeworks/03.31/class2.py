height_str = input("Enter heights: ") or "195 167 165 190 172 182 187 189 168 174"
heights = [int(h) for h in height_str.split()]

people = []

for i in range(len(heights)):
    person = {}
    person['height'] = heights[i]
    person['index'] = i
    person['seen'] = []
    for j in range(len(heights)):
        if person['height'] > heights[j] and i > j:
            person['seen'].append(j)
    people.append(person)

print(people)
farthest_person = max(people, key=lambda x: len(x['seen']))
print(f"Person {farthest_person['index'] + 1} with height {farthest_person['height']} can see the farthest.")

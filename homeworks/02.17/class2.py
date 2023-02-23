

print("Enter data:")
room_length = float(input("room length = "))
room_width = float(input("room width = "))
room_height = float(input("room height = "))
length_of_wallpaper = float(input("length of wallpaper in a roll = "))
width_of_wallpaper = float(input("width of the wallpaper in a roll = "))

perimeter = 2*room_length + 2*room_width
total_strips = perimeter/width_of_wallpaper
rolls_needed = total_strips/length_of_wallpaper

print("You have to buy", int(round(rolls_needed)), "rolls of wallpaper.")

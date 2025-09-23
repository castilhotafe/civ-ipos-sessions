def sing_the_song(number_of_bottles: int):
    end_of_the_song = 0
    for _ in range(number_of_bottles):
        if number_of_bottles > end_of_the_song:
            if number_of_bottles > 1:
                print(f"{number_of_bottles} bottles of beer on the wall, {number_of_bottles} bottles of beer,"
                      f" take one down, pass it around")
            else:
                print(f"{number_of_bottles} bottle of beer on the wall, {number_of_bottles} bottle of beer,"
                      f" take one down, pass it around")
            number_of_bottles = number_of_bottles - 1
        if number_of_bottles > 1:
            print(f"{number_of_bottles} bottles of beer.")
        elif number_of_bottles == 1:
            print("1 bottle of beer.")
        else:
            print("No more bottles of beer.")

sing_the_song(99)
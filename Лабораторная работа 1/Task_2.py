# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44
number_of_pages = 100
number_of_lines = 50
number_of_letters = 25
size_of_one_letter = 4
disk_size_in_bytes = disk_size*1024*1024
size_of_one_book = (number_of_lines * number_of_letters
                    * number_of_pages * size_of_one_letter)
print("Количество книг, помещающихся на дискету:",
      int(disk_size_in_bytes // size_of_one_book))

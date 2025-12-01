# TODO Найдите количество книг, которое можно разместить на дискете
all_mem = 1.44 * 1024 * 1024
total_page = 100
total_str = 50
len_sym = 25
memory = 4
print("Количество книг, помещающихся на дискету:", int(all_mem // (memory * len_sym *  total_str * total_page)))

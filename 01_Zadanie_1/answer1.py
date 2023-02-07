def check_character(a_string, search_char):
    count = 0
    for char in a_string:
        if char == search_char:
            count += 1

    return count


print(check_character('Order of the Phoenix', 'o'))

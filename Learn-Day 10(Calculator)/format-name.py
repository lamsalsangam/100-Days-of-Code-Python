def format_name(f_name, l_name):
    f = f_name.lower().capitalize()
    l = l_name.lower().capitalize()
    return f"{f} {l}"


f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
formatted_string = format_name(f_name, l_name)
print(formatted_string)

def get_template():
    file_path = r'c:\LessonsPython\Lesson1\template.html'
    with open(file_path, 'r', encoding='utf-8') as template_file:
        template_lines = template_file.readlines()
        print(template_lines)
        return template_lines



def get_greeting(my_name, my_age):
    my_str_template = 'My name is {name}. I\'m {number} years old.'
    str2 = my_str_template.replace('{name}', my_name)
    str2 = str2.replace('{number}', my_age)
    return str2


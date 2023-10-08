def get_template():
    file_path = r'c:\LessonsPython\Lesson1\template.html'
    with open(file_path, 'r', encoding='utf-8') as template_file:
        template_lines = template_file.readlines()
        print(template_lines)
        return template_lines

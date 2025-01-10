username = [input("Как вас зовут? ")]
content = [input("Введите содержание заметки: ")]
status = [input("Введите статус: ")]
created_data = input("Введите дату создания (формат ДД-ММ-ГГГГ): ")
issue_data = input("Введите дату изменения (формат ДД-ММ-ГГГГ): ")
temp_created_data = [created_data[0:5]]
temp_issue_data = [issue_data[0:5]]
title_1 = [input("Введите заголовок 1: ")]
title_2 = [input("Введите заголовок 2: ")]
title = [title_1 + title_2]
note = username + content + status + temp_created_data + temp_issue_data + title
print(note)

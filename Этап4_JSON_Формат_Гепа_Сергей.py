# Импорт модуля
import json
# Заметка
note = [
            {
            "username": "Алексей",
            "title": "Список покупок",
            "content": "Купить продукты",
            "status": "новая",
            "created_date": "27-11-2024",
            "issue_date": "30-11-2024"
            }
        ]
# Функция для сохранения заметки в формате JSON
def save_notes_json(notes, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(notes, file, indent=4, ensure_ascii=False)
    except Exception as inform:
        print(f'Произошла ошибка: {inform}')
save_notes_json(note, 'notes.json')
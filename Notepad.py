import json
import os
import random
from datetime import datetime

def load_notes():
    if os.path.exists('notes.json'):
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    else:
        notes = []
    return notes

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

def add_note(notes, title, body):
    id = str(random.randint(1, 1000000))
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    updated_at = created_at

    note = {'id': id, 'title': title, 'body': body, 'created_at': created_at, 'updated_at': updated_at}
    notes.append(note)
    save_notes(notes)
    print('Заметка успешно сохранена')

def read_notes(notes):
    return notes

def update_note(notes, id, title, body):
    note_found = False
    for note in notes:
        if note['id'] == id:
            note['title'] = title
            note['body'] = body
            note['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_notes(notes)
            print('Заметка успешно обновлена')
            note_found = True
            break

    if not note_found:
        print('Заметка с указанным ID не найдена')

def delete_note(notes, id):
    note_found = False
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            save_notes(notes)
            print('Заметка успешно удалена')
            note_found = True
            break

    if not note_found:
        print('Заметка с указанным ID не найдена')

def select_notes_by_date(notes, start_date, end_date):
    selected_notes = []
    for note in notes:
        note_date = datetime.strptime(note['created_at'], '%Y-%m-%d %H:%M:%S')
        if start_date <= note_date <= end_date:
            selected_notes.append(note)
    return selected_notes

def selected_note(note):
    print('\nВыбранная заметка:')
    print(f'ID: {note['id']}')
    print(f'Заголовок: {note['title']}')
    print(f'Содержание: {note['body']}')
    print(f'Дата создания: {note['created_at']}')
    print(f'Дата обновления: {note['updated_at']}')

def main():
    notes = load_notes()

    while True:
        print('\nВведите одну из команд (добавить, все заметки, обновить, удалить, выбор по дате, выход):')
        command = input().strip().lower()

        if command == 'добавить':
            title = input('Введите заголовок заметки: ')
            body = input('Введите содержание заметки: ')
            add_note(notes, title, body)

        elif command == 'все заметки':
            if notes:
                print('\nСписок заметок:\n')
                for note in notes:
                    print(f'ID: {note['id']}')
                    print(f'Заголовок: {note['title']}')
                    print(f'Содержание: {note['body']}')
                    print(f'Дата создания: {note['created_at']}')
                    print(f'Дата обновления: {note['updated_at']}\n')
            else:
                print('Заметок пока нет.')

        elif command == 'обновить':
            id = input('Введите ID заметки для обновления: ')
            title = input('Введите новый заголовок заметки: ')
            body = input('Введите новое содержание заметки: ')
            update_note(notes, id, title, body)

        elif command == 'удалить':
            id = input('Введите ID заметки для удаления: ')
            delete_note(notes, id)

        elif command == 'выбор по дате':
            start_date_str = input('Введите начальную дату в формате 2024-23-03: ')
            end_date_str = input('Введите конечную дату в формате 2024-23-03: ')

            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
                selected_notes = select_notes_by_date(notes, start_date, end_date)

                if selected_notes:
                    for note in selected_notes:
                        selected_note(note)
                else:
                    print('Заметок в указанном диапазоне не найдено.')

            except ValueError:
                print('Неверный формат даты. Используйте формат 2024-23-03.')

        elif command == 'выход':
            print('Завершение работы.')
            break

        else:
            print('Неверная команда. Пожалуйста, введите корректную команду (добавить, все заметки, обновить, удалить, выбор по дате, выход).')

main()

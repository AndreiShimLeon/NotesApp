from Model.Note import Note

from os import path


class Saver:

    def save_note(self, note: Note):
            flag = True if path.exists("notes.csv") else False
            with open('notes.csv', 'a') as data:
                if not flag:
                    line = "id;date;title;text\n"
                    data.write(line)
                data.write(str(note.note['id']))
                data.write(';')
                data.write(str(note.note['date']))
                data.write(';')
                data.write(str(note.note['title']))
                data.write(';')
                data.write(str(note.note['text']))
                data.write('\n')

    def load_notes(self) -> list:
        notes = []
        try:
            with open('notes.csv', 'r') as data:
                next(data)
                for line in data:
                    note_info = line.removesuffix("\n").split(';')
                    notes.append(note_info)
            return notes
        except:
            return -1


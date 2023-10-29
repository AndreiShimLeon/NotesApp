import datetime
from os import path


class Note:
    note_id = 1

    def set_date(self) -> str:
        date = str(datetime.datetime.today().date())
        time = str(datetime.datetime.today().time())[:8]
        return "{} {}".format(date, time)

    def __init__(self, title: str, text: str):
        try:
            with open('notes.csv', 'r') as data:
                last_line = data.readlines()[-1]
                Note.note_id = int(last_line.split(";")[0]) + 1
        except FileNotFoundError as e:
            print("First note has been created!")
        finally:
            id = Note.note_id
        date = self.set_date()
        if title =="":
            title = "No title " + str(id)
        self.note = {"id": id, "date": date, "title": title, "text": text}

    def correction(self, new_text: str, new_title: str = 'n'):
        self.note["date"] = self.set_date()
        self.note["text"] = new_text
        if new_title.lower() != 'n':
            self.note["title"] = new_title

    def to_string(self):
        return "Note #{} Time stamp {}\n>> {} <<\n{}\n".format(*self.note.values())


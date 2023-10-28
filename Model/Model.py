import datetime


class Note:
    note_id = 1

    def get_id(self) -> int:
        return self.note_id
    def set_id(self, id: int):
        Note.note_id = id

    def set_date(self) -> str:
        date = str(datetime.datetime.today().date())
        time = str(datetime.datetime.today().time())[:8]
        return "{} {}".format(date, time)

    def __init__(self, title: str, text: str):
        id = Note.note_id
        Note.note_id += 1
        date = self.set_date()
        self.note = {"id": id, "date": date, "title": title, "text": text}

    def correction(self, new_text: str, new_title: str = 'n'):
        self.note["date"] = self.set_date()
        self.note["text"] = new_text
        if new_title.lower() != 'n':
            self.note["title"] = new_title

    def to_string(self):
        return "Заметка {} от {}\n>> {} <<\n{}\n".format(*self.note.values())


# print(type(str(datetime.datetime.today())))
# print(str(datetime.datetime.today()).upper().replace('2',"fuck"))


if __name__ == '__main__':
    note1 = Note("Новая заметка 1 ", "This is text in my note")
    note2 = Note("Новая заметка 2", "This is text in my note")
    note3 = Note("Новая заметка 3", "This is text in my note")
    note4 = Note("Новая заметка 3", "This is text in my note")
    note4.set_id(10)
    note5 = Note("Новая заметка 3", "This is text in my note")
    note6 = Note("Новая заметка 3", "This is text in my note")
    note7 = Note("Новая заметка 3", "This is text in my note")
    note8 = Note("Новая заметка 3", "This is text in my note")
    note9 = Note("Новая заметка 3", "This is text in my note")
    note10 = Note("Новая заметка 3", "This is text in my note")
    note11 = Note("Новая заметка 3", "This is text in my note")
    note12 = Note("Новая заметка 3", "This is text in my note")

    print(note1.to_string())
    print(note2.to_string())
    print(note4.to_string())
    print(note5.to_string())
    print(note12.to_string())
    text = "Это новый текст"
    title = "Это новый заголовок"
    note1.correction(new_title=title, new_text=text)
    # print(note1.to_string())

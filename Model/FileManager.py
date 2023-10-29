from datetime import datetime

from Model.Note import Note

from os import path


class FileManager:

    def save_note(self, note: Note) -> None:
        """
        The function of writing notes to the notes.csv file.
        If the file does not exist, then a file with headers is created
        :param note: an instance of the Note class
        :return: None
        """
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
        """
        Downloading the list of notes from the notes.csv file.
        :return: -1, if the file does not exist, a list of notes, if the file exists and is filled with notes
        """
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

    def search_note(self, id: str = '0', title: str = 'n', text_fragment: str = 'n') -> list:
        """
        !important! Only one of the parameters should be different from the default value
        The function of searching in the list of notes for a note in which one of the parameters matches
        :param id: if id = 0, we do not search by id
        :param title: if title ='n', we do not search by title
        :param text_fragment: if text_fragment = 'n', we do not search for a text fragment
        :return: a note in the form of a list [id, date, title, text]
        """
        notes = self.load_notes()
        result = []
        if type(notes) is list:
            try:
                if int(id) != 0:
                    for note in notes:
                        if int(note[0]) == int(id):
                            result.append(note)
            except TypeError as e:
                print("ID is a number")
            if title != 'n':
                for note in notes:
                    if note[2].lower().find(title.lower()) != -1:
                        result.append(note)
            if text_fragment != 'n':
                for note in notes:
                    if note[3].lower().find(text_fragment.lower()) != -1:
                        result.append(note)
            if len(result) == 0: print("Note not found")
            return result
        else:
            print("List of notes is empty")
            return result  # empty list

    @classmethod
    def correct_note(cls, note: list, new_title: str, new_text: str) -> None:
        """
        This function corrects note in the file notes.csv by replacing the old one with a new one
        New title (optional) and new text(obligatory)
        :param note: list type: [id, date, title, text]
        :param new_title: if 'n' has been entered, the old title remains
        :param new_text: replaces the old one
        :return: None
        """
        new_note = note.copy()
        if new_title.lower() != 'n':
            new_note[2] = new_title
        new_note[3] = new_text
        date = str(datetime.today().date())
        time = str(datetime.today().time())[:8]
        new_note[1] = "{} {}".format(date, time)
        with open('notes.csv', 'r') as data:
            content = data.read()
        old_note_line = ";".join(note)
        new_note_line = ";".join(new_note)
        content = content.replace(old_note_line, new_note_line)
        with open("notes.csv", "w") as write_file:
            write_file.write(content)

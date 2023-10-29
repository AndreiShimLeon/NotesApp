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

    def search_note(self, id: str = 0, title: str = 'n', text_fragment: str = 'n') -> list:
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
                        if int(note[0]) == id:
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

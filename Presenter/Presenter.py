from Model.Note import Note
from Model.FileManager import FileManager
from View.Viewer import Viewer


class Message:
    intro_message = ("Please choose action:\n"
                     "\t1. Add note\n"
                     "\t2. Search\n"
                     "\t3. Display all notes\n"
                     "\t4. Exit\n>>>")

    choice_error_message = "Please use only numbers when choosing actions\n"
    choice_repeat = "Please make the right choice\n"
    bye_message = "Goodbye!"
    title_message = "Enter the title:\n"
    text_message = "Enter the text of the note:\n"
    new_title_message = "Enter a new note title (to skip, type 'N'):\n"
    new_text_message = "Enter the corrected text of the note:\n"
    search_choice_message = ("\t\t 1. Search by ID\n"
                             "\t\t 2. Search by title\n"
                             "\t\t 3. Search by text\n"
                             "\t\t 4. Return\n>>>")
    id_search_message = "\t\t Enter ID for search:\n>>>"
    title_search_message = "\t\t Enter Title for search:\n>>>"
    text_search_message = "\t\t Enter Text for search:\n>>>"
    search_result_more_than_one = "\t\t There are more than one search results.\n\t\t For correction/deletion please try to repeat the query"


class Presenter:
    def __init__(self):
        self.viewer = Viewer()
        self.file_manager = FileManager()

    def start(self):
        flag = True
        while flag:
            # User is proposed to make the choice: 1. Add note 2. Search 3. Display all notes 4. Exit
            try:
                choice = int(Viewer.get_data(self.viewer, message=Message.intro_message))
                if choice < 1 or choice > 4:
                    raise IndexError

                # User has chosen to add a note
                if choice == 1:
                    title = Viewer.get_data(self.viewer, message=Message.title_message)
                    text = Viewer.get_data(self.viewer, message=Message.text_message)
                    note = Note(title, text)
                    FileManager.save_note(self.file_manager, note)
                # User has chosen to find a note
                elif choice == 2:
                    search_result = []
                    search_choice = int(Viewer.get_data(self.viewer, message=Message.search_choice_message))
                    if search_choice < 1 or search_choice > 4:
                        raise IndexError
                    else:
                        # User has chosen to find a note by ID
                        if search_choice == 1:
                            search_id = Viewer.get_data(self.viewer, message=Message.id_search_message)
                            search_result = FileManager.search_note(self.file_manager, id=search_id)
                        # User has chosen to find a note by title
                        elif search_choice == 2:
                            search_title = Viewer.get_data(self.viewer, message=Message.title_search_message)
                            search_result = FileManager.search_note(self.file_manager, title=search_title)
                        # User has chosen to find a note by text fragment
                        elif search_choice == 3:
                            search_text = Viewer.get_data(self.viewer, message=Message.text_search_message)
                            search_result = FileManager.search_note(self.file_manager, text_fragment=search_text)
                        # User has chosen to return to the main menu
                        elif search_choice == 4:
                            continue
                        if len(search_result) > 1:
                            Viewer.print_in_console(self.viewer, message=Message.search_result_more_than_one)
                            Viewer.print_list_in_console(self.viewer, notes=search_result, message="Found notes: ")
                        else:
                            Viewer.print_list_in_console(self.viewer, notes=search_result, message="Found note: ")
                            Viewer.print_in_console(self.viewer, message=Message.search_result_more_than_one)

                            if search_choice < 1 or search_choice > 4:
                                pass
                # User have chosen to display all notes
                elif choice == 3:
                    info = FileManager.load_notes(self.file_manager)
                    Viewer.print_list_in_console(self.viewer, notes=info)
                # User have chosen to close the application
                elif choice == 4:
                    flag = False
                    Viewer.print_in_console(self.viewer, message=Message.bye_message)
            except ValueError as e:
                Viewer.print_in_console(self.viewer, message=Message.choice_error_message)
                continue
            except IndexError as e:
                Viewer.print_in_console(self.viewer, message=Message.choice_repeat)
                continue

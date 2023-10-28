from Model.Note import Note
from Model.Saver import Saver
from View.Viewer import Viewer


class Message:
    intro_message = ("Выберите действие:\n"
                     "\t1. Новая заметка;\n"
                     "\t2. Поиск заметки;\n"
                     "\t3. Список заметок;\n"
                     "\t4. Завешить работу.\n>>>")

    choice_error_message = "Пожалуйста, при выборе действий используйте только числа.\n"
    choice_repeat = "Пожалуйста, сделайте правильный выбор.\n"
    bye_message = "До свидания!"
    title_message = "Введите заголовок:\n"
    text_message = "Введите текст заметки:\n"
    new_title_message = "Введите новый заголовок заметки (чтобы пропустить, введите 'N'):\n"
    new_text_message = "Введите скорректированный текст заметки:\n"


class Presenter:
    def __init__(self):
        self.viewer = Viewer()
        self.saver = Saver()

    def start(self):
        #TODO: проверка последнего ID в файле, изменение классового поля ID
        flag = True
        while flag:
            # Пользователь делает выбор 1. нов зам 2. поиск 3. выход
            try:
                choice = int(Viewer.get_data(self.viewer, message=Message.intro_message))
                if choice < 1 or choice > 4:
                    raise IndexError
            except ValueError as e:
                Viewer.print_in_console(self.viewer, message=Message.choice_error_message)
                continue
            except IndexError as e:
                Viewer.print_in_console(self.viewer, message=Message.choice_repeat)
                continue
            if choice == 1:
                title = Viewer.get_data(self.viewer, message=Message.title_message)
                text = Viewer.get_data(self.viewer, message=Message.text_message)
                note = Note(title, text)
                # TODO: запись в файл
                Saver.save_note(self.saver, note)
            if choice == 2:
                # TODO: Поиск заметки по ID, заголовку, времени/дате создания,
                pass
                new_title = Viewer.get_data(self.viewer, message=Message.new_title_message)
                new_text = Viewer.get_data(self.viewer, message=Message.new_text_message)
                note.correction(new_text=new_text, new_title=new_title)
            # TODO чтение списка заметок
            if choice == 3:
                info = Saver.load_notes(self.saver)
                Viewer.print_list_in_console(self.viewer, notes=info)

            if choice == 4:
                flag = False
                Viewer.print_in_console(self.viewer, message=Message.bye_message)

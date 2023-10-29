from struct import unpack


class Viewer:

    def print_in_console(self, message: str):
        self.mes = message
        print(self.mes)

    def print_list_in_console(self, notes: list):
        print("Notes list:")
        try:
            for note in notes:
                print("\t", note[0], note[1], note[2])
        except TypeError as e:
            print("empty")

    def get_data(self, message: str):
        self.mes = message
        return input(self.mes)

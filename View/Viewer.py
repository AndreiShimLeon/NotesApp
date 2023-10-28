class Viewer:

    def print_in_console(self, message: str):
        self.mes = message
        print(self.mes)

    def get_data(self, message: str):
        self.mes = message
        return input(self.mes)

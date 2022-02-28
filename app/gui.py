import easygui_qt as eg
from datetime import date, datetime


class NexusGUI():

    def __init__(self):
        self.title = 'Nexus statsdata query generator'
        self.status = 0
        message = """
        <h1 style="text-align: center;">Instrucciones</h1>
        <ul>
        <li>Selecciona un archivo excel con los valores y el timestamp de la variable.</li>
        <li>Introduce el tag_id y el driver_id de la variable</li>
        <li>Introduce la fecha de inicio y la fecha de fin</li>
        <li>El resultado de la query se copia en el portapapeles</li>
        </ul>
        """
        eg.show_html(self.title, message)

    def options_old(self):
        labels = ['tag_id', 'driver_id', 'start_year', 'end_year']
        reply = eg.get_many_strings(self.title, labels)
        print(reply)
        try:
            tag_id = int(reply['tag_id'])
            driver_id = int(reply['driver_id'])
            start_year = int(reply['start_year'])
            end_year = int(reply['end_year'])
        except:
            eg.show_message(title=self.title, message='Wrong input format')
            self.status = 1
        return tag_id, driver_id, start_year, end_year

    def options(self):
        labels = ['tag_id', 'driver_id']
        reply = eg.get_many_strings(self.title, labels)
        print(reply)
        try:
            tag_id = int(reply['tag_id'])
            driver_id = int(reply['driver_id'])
        except:
            eg.show_message(title=self.title, message='Wrong input format')
            self.status = 1
        return tag_id, driver_id

    def get_dates(self):
        start_date = eg.get_date('Select start date')
        end_date = eg.get_date('Select end date')
        start_date = datetime.combine(start_date, datetime.min.time())
        end_date = datetime.combine(end_date, datetime.min.time())
        return start_date, end_date

    def get_path(self):
        path = eg.get_file_names()
        return path[0][0]

    def show_message_done(self):
        eg.show_message('Done. The program will close')

    def choose_vble(self, names):
        reply = eg.get_choice(title=self.title, message='Multiple names found. Select one',
                              choices=names)
        return reply

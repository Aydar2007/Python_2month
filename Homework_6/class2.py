class data:
    def __init__(self):
        self._full_name = ""
        self._email = ""
        self._file_name = ""
        self._color = ""

    def get_full_name(self):
        return self._full_name

    def set_full_name(self, value):
        self._full_name = value

    def get_email(self):
        return self._email

    def set_email(self, value):
        self._email = value

    def get_file_name(self):
        return self._file_name

    def set_file_name(self, value):
        self._file_name = value

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value

data_list = []
with open("MOCK_DATA.txt","w") as f:
    f.write(f"AYDAR MOLLOJANOV,123123@mail.ru,djdiwld,123213")

with open("MOCK_DATA.txt", "r") as file:
    for l in file:
        info = l.strip().split(",")
        new_data = data()
        new_data.set_full_name(info[0])
        new_data.set_email(info[1])
        new_data.set_file_name(info[2])
        new_data.set_color(info[3])
        data_list.append(new_data)

with open("full_names.txt", "w") as file:
    for d in data_list:
        file.write(d.get_full_name() + "\n")

with open("emails.txt", "w") as file:
    for d in data_list:
        file.write(d.get_email() + "\n")

with open("file_names.txt", "w") as file:
    for d in data_list:
        file.write(d.get_file_name() + "\n")

with open("colors.txt", "w") as file:
    for d in data_list:
        file.write(d.get_color() + "\n")
    
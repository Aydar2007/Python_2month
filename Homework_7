import re

class data:
    def __init__(self):
        self._full_name = ""
        self._email = ""
        self._file_name = ""
        self._color = ""

    def name(self):
        return self._full_name

    def name(self, value):
        self._full_name = value

    def email(self):
        return self._email

    def email(self, value):
        self._email = value

    def file_name(self):
        return self._file_name

    def file_name(self, value):
        self._file_name = value

    def color(self):
        return self._color

    def color(self, value):
        self._color = value

final_file=data


list=""


with open ("MOCK_DATA.txt","r") as file:
    list = file.read()
list=re.sub(r'\n',"-", list)
list=re.sub(r'\t',"-", list)
list=re.sub(r'-',",", list)
list1=re.split(r',', list)

email_lists=[]


with open ("EMAIL.txt","w") as file:
    while True:
        for email_lists in list1:
            if "@" in email_lists:
                email_lists=email_lists
                final_file.email=email_lists
                file.write(f"\n{email_lists}")
        break


with open ("Color.txt","w") as file:
    while True:
        for color_lists in list1:
            if "#" in color_lists:
                color_lists=color_lists
                final_file.color=color_lists
                file.write(f"\n{color_lists}")
        break


with open ("file_name.txt","w") as file:
    while True:
        for file_name_lists in list1:          
            if ".ppt" in file_name_lists:
                file_name_lists=file_name_lists
                file.write(f"\n{file_name_lists}")
                final_file.color=color_lists
            elif ".avi" in file_name_lists:
                file_name_lists=file_name_lists
                file.write(f"\n{file_name_lists}")
                final_file.color=color_lists
            elif ".doc" in file_name_lists:
                file_name_lists=file_name_lists
                file.write(f"\n{file_name_lists}")
                final_file.color=color_lists
            elif ".png" in file_name_lists:
                file_name_lists=file_name_lists
                file.write(f"\n{file_name_lists}")
                final_file.color=color_lists
            elif ".jpeg" in file_name_lists:
                file_name_lists=file_name_lists
                file.write(f"\n{file_name_lists}")
                final_file.color=color_lists
            elif ".mov" in file_name_lists:
                file_name_lists=file_name_lists
                file.write(f"\n{file_name_lists}")
                final_file.color=color_lists
            elif ".gif" in file_name_lists:
                file_name_lists=file_name_lists
                file.write(f"\n{file_name_lists}")
                final_file.color=color_lists
            elif ".xls" in file_name_lists:
                file_name_lists=file_name_lists
                file.write(f"\n{file_name_lists}")        
                final_file.color=color_lists
            elif ".mp3" in file_name_lists:
                file_name_lists=file_name_lists
                file.write(f"\n{file_name_lists}")   
                final_file.color=color_lists
            elif ".pdf" in file_name_lists:
                file_name_lists=file_name_lists
                file.write(f"\n{file_name_lists}")
                final_file.color=color_lists
            elif ".tiff" in file_name_lists:
                file_name_lists=file_name_lists
                file.write(f"\n{file_name_lists}")
                final_file.color=color_lists
            elif ".mpeg" in file_name_lists:
                file_name_lists=file_name_lists
                file.write(f"\n{file_name_lists}")
                final_file.color=color_lists
            elif ".txt" in file_name_lists:
                final_file.color=color_lists
                file_name_lists=file_name_lists
                file.write(f"\n{file_name_lists}")
        break


with open ("Color.txt","r") as file:
    final_file.color=file.read()
with open ("file_name.txt","r") as file:
    final_file.file_name=file.read()
with open ("EMAIL.txt","r") as file:
    final_file.email=file.read()


name_list=[]


with open ("name.txt","w") as file:
    while True:
        for name_lists in list1:
            name_lists=name_lists
            if name_lists not in final_file.email and name_lists not in final_file.color and name_lists not in final_file.file_name:
                name_list=name_lists
                file.write(f"\n{name_list}")
        break


with open("name.txt","r") as file:
    final_file.name=file.read()








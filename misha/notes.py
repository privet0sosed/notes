from PyQt5 import Qt
from PyQt5.QtWidgets import *
import json

app = QApplication([])

notes = {
    "Ласкаво просимо!": {
        "text": "Це додаток для заміток",
        "tags": ["інструкція", "замітки"]
    }
}

with open("notes_data.json", "w") as file:
    json.dump(notes, file)

notes_win = QWidget()
notes_win.setWindowTitle("Розумні замітки")
notes_win.resize(900, 600)

list_notes = QListWidget()
list_notes_label = QLabel("Список заміток")

button_note_create = QPushButton("Створити замітку")
button_note_del = QPushButton("Видалити замітку")
button_note_save = QPushButton("Зберегти замітку")

filed_tag = QLineEdit("")
filed_tag.setPlaceholderText("Введіть тег")

field_text = QTextEdit()

button_tag_add = QPushButton("Додати до замітки")
button_tag_del = QPushButton("Видалити з замітки")
button_tag_search = QPushButton("Шукати замітку")

list_tags = QListWidget()
list_tags_label = QLabel("Список тегів")

layout_notes = QHBoxLayout()

col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(filed_tag)

row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)
notes_win.setLayout(layout_notes)

def add_note():
    note_name, ok = QInputDialog.getText(
        notes_win, "Додати замітку", "Назва замітки"
    )
    if ok and note_name != "":
        notes[note_name] = {"text": "", "tags": []}
        list_notes.addItem(note_name)
        list_tags.addItem(notes[note_name]["tags"])

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["text"])
    list_tags.clear()
    field_text.setText(notes[key]["tags"])

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["text"] = field_text.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("None selected!")

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("None selected!")

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = filed_tag.text()
        if not tag in notes[key]["tags"]:
            notes[key]["tags"].append(tag)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("None selected!")

def del_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["tags"].remove()
        list_tags.clear()
        list_tags.addItems(notes[key]["tags"])
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("None selected!")

list_notes.itemClicked.connect(show_note)

notes_win.show()

with open("notes_data.json", "r") as file:
    notes = json.load(file)

# list_notes.addItem(notes)

app.exec_()
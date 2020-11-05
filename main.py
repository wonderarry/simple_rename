from PyQt5 import QtWidgets, QtCore
import design
import os

class Main_app(QtWidgets.QMainWindow, design.Ui_MainWindow):


    def delete_element(self):
        self.main_list.takeItem(self.main_list.currentRow())


    def append_element(self):
        item_name = QtWidgets.QFileDialog.getOpenFileName(self, "Choose file...")
        if item_name:
            self.main_list.addItem(item_name[0])


    def ascending_sort(self):
        self.main_list.sortItems(0)


    def descending_sort(self):
        self.main_list.sortItems(1)


    def move_upwards(self):
        curr_item = self.main_list.takeItem(self.main_list.currentRow())
        self.main_list.insertItem(self.main_list.currentRow() - 1, curr_item)
        self.main_list.setCurrentRow(self.main_list.currentRow() - 2)


    def move_downwards(self):
        curr_item = self.main_list.takeItem(self.main_list.currentRow())
        self.main_list.insertItem(self.main_list.currentRow() + 1, curr_item)
        self.main_list.setCurrentRow(self.main_list.currentRow() + 2)

    def rename(self):
        end_folder = os.path.dirname(self.main_list.item(0).text())
        name_list = [os.path.basename(self.main_list.item(i).text()) for i in range(0, self.main_list.count())]
        for i in range(len(name_list)):
            new_name = self.name_mask.text() + str(int(self.name_base.value()) + i * int(self.name_incr.value())) + '.' + name_list[i].split('.')[-1]
            os.system('cd /d "' + end_folder + '" & ren "' + name_list[i] + '" "' + new_name + '"')
            self.main_list.item(i).setText(os.path.dirname(self.main_list.item(i).text()) + '\\' + new_name)


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #Clearing the list
        self.clear_list.clicked.connect(self.main_list.clear)
        #Removing an item
        self.rem_elem.clicked.connect(self.delete_element)
        #Appending an item
        self.add_elem.clicked.connect(self.append_element)
        #Sorting the list
        self.sort_list_asc.clicked.connect(self.ascending_sort)                 #Ascending order
        self.sort_list_desc.clicked.connect(self.descending_sort)               #Descending order
        #Moving items in the list
        self.move_up.clicked.connect(self.move_upwards)
        self.move_down.clicked.connect(self.move_downwards)
        #Executing
        self.do_execute.clicked.connect(self.rename)




def main():
    app = QtWidgets.QApplication([])
    window = Main_app()
    window.setWindowFlags(window.windowFlags() & QtCore.Qt.CustomizeWindowHint)
    window.setWindowFlags(window.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

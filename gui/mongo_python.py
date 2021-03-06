from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
from gui import main
from lib import customModel
from lib import databaseOperations


class PythonMongoDB(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(PythonMongoDB, self).__init__()
        self.setupUi(self)

        self.user_data = databaseOperations.get_all_data()
        self.model = customModel.CustomTableModel(self.user_data)
        self.delegate = customModel.InLineEditDelegate()
        self.tableView.setModel(self.model)
        self.tableView.setItemDelegate(self.delegate)
        self.tableView.setItemDelegateForColumn(1, customModel.ProfilePictureDelegate())
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.context_menu)
        self.tableView.verticalHeader().setDefaultSectionSize(70)
        self.tableView.setColumnWidth(0, 10)
        self.tableView.hideColumn(0)
        #self.tableView_2.setModel(self.model)
       # self.tableView_3.setModel(self.model)

    def context_menu(self):
        menu = QtWidgets.QMenu()
        add_data = menu.addAction("Add New Data")
       # add_data.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
        add_data.triggered.connect(lambda: self.model.insertRows())
        if self.tableView.selectedIndexes():
            remove_data = menu.addAction("Remove Data")
            #remove_data.setIcon(QtGui.QIcon(":/icons/images/remove.png"))
            remove_data.triggered.connect(lambda: self.model.removeRows(self.tableView.currentIndex()))
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    my_app = PythonMongoDB()
    my_app.show()
    app.exec_()

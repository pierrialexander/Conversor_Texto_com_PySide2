from conversor_design import *
from PySide2 import QtWidgets


def main(ui):

    def funcao():
        if ui.radio_maiusculo.isChecked():
            texto = ui.textEdit_origem.toPlainText()
            ui.textEdit_resultado.setText(texto.upper())
        if ui.radio_minusculo.isChecked():
            texto = ui.textEdit_origem.toPlainText()
            ui.textEdit_resultado.setText(texto.lower())
        if ui.radio_primeira.isChecked():
            texto = ui.textEdit_origem.toPlainText()
            ui.textEdit_resultado.setText(texto.title())

    def b():
       ui.textEdit_origem.clear()
       ui.textEdit_resultado.clear()

    ui.button_converter.clicked.connect(funcao)

    ui.pushButton.clicked.connect(b)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())

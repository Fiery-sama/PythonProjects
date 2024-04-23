# importing the required modules
import sys
import os
# importing the required classes from the PyQt5 module
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, \
                            QLabel, QPlainTextEdit, QStatusBar, QToolBar, \
                            QVBoxLayout, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QFontDatabase, QIcon, QKeySequence
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtPrintSupport import QPrintDialog

# creating the subclass of the QMainWindow class
class Application(QMainWindow):
    # defining the initializing function
    def __init__(self):
        super().__init__()
        # configuring the title of the window
        self.setWindowTitle("My Notepad - JAVATPOINT")
        # configuring the width and height of the window
        self.window_width, self.window_height = self.geometry().width(), self.geometry().height()
        # setting the Icon of the window
        self.setWindowIcon(QIcon('./icons/notepad.ico'))
        # using the resize() to set the size of the application
        self.resize(self.window_width * 2, self.window_height * 2)

        # defining some filter types
        self.filter_types = 'Text Document (*.txt);; Python (*.py);; Mardown (*.md)'
        # defining the default location in the directory
        self.destination = None

        # defining the font style and size
        fixed_fonts = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixed_fonts.setPointSize(11)

        # creating an object of the QVBoxLayout class
        main_layout = QVBoxLayout()

        # Text Editor
        # creating an object of the QPlainTextEdit class
        self.text_editor = QPlainTextEdit()
        # setting the font style of the editor
        self.text_editor.setFont(fixed_fonts)
        # adding the text text_editor object to the main layout of the window
        main_layout.addWidget(self.text_editor)

        # Status bar
        # creating the status bar using the statusBar() method
        self.status_bar = self.statusBar()

        # App Container
        # creating an object of the QWidget class
        app_container = QWidget()
        # using the setLayout() method to set the main layout to the container
        app_container.setLayout(main_layout)
        self.setCentralWidget(app_container)

        #--------------------------------------
        # Creating a File Menu
        #--------------------------------------
        filemenu = self.menuBar().addMenu('&File')
        
        #--------------------------------------
        # Creating a File ToolBar
        #--------------------------------------
        filetoolbar = QToolBar('File')
        filetoolbar.setIconSize(QSize(30, 30))
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, filetoolbar)

        # creating the menu options like open, save, save as, and print

        # calling the user-defined make_action() function to create the action to open the file...
        open_doc_opt = self.make_action(self, './icons/open_document.ico', 'Open File...', 'Open File...', self.fileOpen)
        # using the setShortcut() method to set a shortcut to execute the 'open' command
        open_doc_opt.setShortcut(QKeySequence.Open)

        # calling the user-defined make_action() function to create the action to save the file
        save_doc_opt = self.make_action(self, './icons/save.ico', 'Save', 'Save', self.fileSave)
        # using the setShortcut() method to set a shortcut to execute the 'save' command
        save_doc_opt.setShortcut(QKeySequence.Save)

        # calling the user-defined make_action() function to create the action to save file as...
        save_doc_as_opt = self.make_action(self, './icons/save_as.ico', 'Save As...', 'Save As...', self.fileSaveAs)
        # using the setShortcut() method to set a shortcut to execute the 'save as' command
        save_doc_as_opt.setShortcut(QKeySequence('Ctrl+Shift+S'))

        # calling the user-defined make_action() function to create the action to print the file
        print_opt = self.make_action(self, './icons/printer.ico', 'Print', 'Print', self.printFile)
        # using the setShortcut() method to set a shortcut to execute the 'print' command
        print_opt.setShortcut(QKeySequence.Print)

        # using the addActions() method to add all the created actions to the 'File' menu and toolbar
        filemenu.addActions([open_doc_opt, save_doc_opt, save_doc_as_opt, print_opt])
        filetoolbar.addActions([open_doc_opt, save_doc_opt, save_doc_as_opt, print_opt])

        #--------------------------------------
        # Creating an Edit Menu
        #--------------------------------------
        editmenu = self.menuBar().addMenu('&Edit')
        
        #--------------------------------------
        # Creating an Edit Tool bar
        #--------------------------------------
        edittoolbar = QToolBar('Edit')
        edittoolbar.setIconSize(QSize(30, 30))
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, edittoolbar)

        # calling the user-defined make_action() function to create the action to undo the current operation
        undo_opt = self.make_action(self, './icons/undo.ico', 'Undo', 'Undo', self.text_editor.undo)
        # using the setShortcut() method to set a shortcut to execute the 'undo' command
        undo_opt.setShortcut(QKeySequence.Undo)
        
        # calling the user-defined make_action() function to create the action to redo the current operation
        redo_opt = self.make_action(self, './icons/redo.ico', 'Redo', 'Redo', self.text_editor.redo)
        # using the setShortcut() method to set a shortcut to execute the 'redo' command
        redo_opt.setShortcut(QKeySequence.Redo)

        # calling the user-defined make_action() function to create the action to clear the text
        clear_opt = self.make_action(self, './icons/clear.ico', 'Clear', 'Clear', self.resetContent)

        # using the addActions() method to add all the created actions to the 'Edit' menu and toolbar
        editmenu.addActions([undo_opt, redo_opt, clear_opt])
        edittoolbar.addActions([undo_opt, redo_opt, clear_opt])

        # adding the separator
        editmenu.addSeparator()
        edittoolbar.addSeparator()

        # calling the user-defined make_action() function to create the action to cut the selected text
        cut_opt = self.make_action(self, './icons/cut.ico', 'Cut', 'Cut', self.text_editor.cut)
        # using the setShortcut() method to set a shortcut to execute the 'cut' command
        cut_opt.setShortcut(QKeySequence.Cut)

        # calling the user-defined make_action() function to create the action to copy the selected text
        copy_opt = self.make_action(self, './icons/copy.ico', 'Copy', 'Copy', self.text_editor.copy)
        # using the setShortcut() method to set a shortcut to execute the 'copy' command
        copy_opt.setShortcut(QKeySequence.Copy)

        # calling the user-defined make_action() function to create the action to paste the copied text
        paste_opt = self.make_action(self, './icons/paste.ico', 'Paste', 'Paste', self.text_editor.paste)
        # using the setShortcut() method to set a shortcut to execute the 'paste' command
        paste_opt.setShortcut(QKeySequence.Paste)

        # calling the user-defined make_action() function to create the action to select to entire text
        select_all_opt = self.make_action(self, './icons/select_all.ico', 'Select All', 'Select all', self.text_editor.selectAll)
        # using the setShortcut() method to set a shortcut to execute the 'select all' command
        select_all_opt.setShortcut(QKeySequence.SelectAll)

        # using the addActions() method to add all the created actions to the 'Edit' menu and toolbar
        editmenu.addActions([cut_opt, copy_opt, paste_opt, select_all_opt])
        edittoolbar.addActions([cut_opt, copy_opt, paste_opt, select_all_opt])

        # adding the separator
        editmenu.addSeparator()
        edittoolbar.addSeparator()

        # calling the user-defined make_action() function to create the action to wrap the text to next line
        wraptext_opt = self.make_action(self, './icons/text_wrap.ico', 'Wrap Text', 'Wrap text', self.toggleWrapText)
        # using the setShortcut() method to set a shortcut to execute the 'wrap text' command
        wraptext_opt.setShortcut('Ctrl+Shift+W')

        # using the addActions() method to add the above created action to the 'Edit' menu and toolbar
        editmenu.addActions([wraptext_opt])
        edittoolbar.addActions([wraptext_opt])

        # calling the user-defined updateTitle() function
        self.updateTitle()

    # defing the function to toggle the wrap text operation
    def toggleWrapText(self):
        # toggling the wrap text operation using the setLineWrapMode() method
        self.text_editor.setLineWrapMode(not self.text_editor.lineWrapMode())

    # defining the function to reset the content
    def resetContent(self):
        # setting the entire content to empty string
        self.text_editor.setPlainText('')
        
    # defining the function to open the file
    def fileOpen(self):
        # setting the destination of the file to be opened
        destination, _ = QFileDialog.getOpenFileName(
            parent = self,
            caption = 'Open File...',
            directory = '',
            filter = self.filter_types
        )

        # reading the content of the file using the try-except method
        if destination:
            try:    
                with open(destination, 'r') as f:
                    text = f.read()
                    f.close()
            except Exception as e:
                self.dialogMessage(str(e))
            else:
                self.path = destination
                self.text_editor.setPlainText(text)
                self.updateTitle()

    # defining the function to save the file
    def fileSave(self):
        # calling the fileSaveAs() function, if the path is None
        if self.destination is None:
            self.fileSaveAs()
        # else save the file to the given path using the try-except method
        else:
            try:
                text = self.text_editor.toPlainText()
                with open(self.destination, 'w') as f:
                    f.write(text)
                    f.close()
            except Exception as e:  
                self.dialogMessage(str(e))

    # defining the function to save file as... to the directory
    def fileSaveAs(self):
        # setting the destination where the file will be saved
        destination, _ = QFileDialog.getSaveFileName(
            self,
            'Save File as...',
            '',
            self.filter_types
        )                               
        text = self.text_editor.toPlainText()

        # saving the file using the try-except method
        if not destination:
            return
        else:
            try:
                with open(destination, 'w') as f:
                    f.write(text)
                    f.close()
            except Exception as e:
                self.dialogMessage(str(e))
            else:
                self.destination = destination
                self.updateTitle()

    # defining the function to print the file
    def printFile(self):
        # creating an object of the QPrintDialog() class
        print_dialog = QPrintDialog()
        # printing the file
        if print_dialog.exec_():
            self.text_editor.print_(print_dialog.printer())

    # defining the function to open a dialog box displaying the message
    def dialogMessage(self, msg):
        # creating an object of the QMessageBox() class
        dialog = QMessageBox(self)
        # setting the message to the dialog box
        dialog.setText(msg)
        # setting the icon of the dialog box
        dialog.setIcon(QMessageBox.Critical)
        # displaying the dialog box
        dialog.show()

    # defining the function to update the title of the file
    def updateTitle(self):
        # setting the window title
        self.setWindowTitle('{0} - My Notepad - JAVATPOINT'.format(os.path.basename(self.destination) if self.destination else 'Untitled'))

    # defining the function to create the actions of the menu and toolbar
    def make_action(self, parent_obj, icon_destination, name_of_action, status_tip, triggered_method):
        # creating an object of the QAction() class
        act = QAction(QIcon(icon_destination), name_of_action, parent_obj)
        # updating the message in the status bar
        act.setStatusTip(status_tip)
        # calling the different functions designated to different actions
        act.triggered.connect(triggered_method)
        # returning the action
        return act

# creating an object of the QApplication class
the_app = QApplication(sys.argv)

# creating an object of the Application class
notepad_app = Application()

# using the show() method to display the window
notepad_app.show()

# using the exit() function of the sys module to close the application
sys.exit(the_app.exec_())
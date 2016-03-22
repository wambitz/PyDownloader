from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class Downloader(QDialog):
    # Constructor
    def __init__(self):
        QDialog.__init__(self)

        # Application layout format
        layout = QVBoxLayout()

        # Objects within layout
        url = QLineEdit()
        save_location = QLineEdit()
        progress = QProgressBar()
        download = QPushButton("Download")

        # Modify widgets properties
        url.setPlaceholderText("URL")
        save_location.setPlaceholderText("File save location")

        # Add objects to layout
        layout.addWidget(url)
        layout.addWidget(save_location)
        layout.addWidget(progress)
        layout.addWidget(download)

        self.setLayout(layout)
        self.setWindowTitle("PyDownloader")                 # Main window title
        self.setFocus()                                     # Removes focus from QLineEdit()


# Call main window
app = QApplication(sys.argv)
dialog = Downloader()
dialog.show()
app.exec_()

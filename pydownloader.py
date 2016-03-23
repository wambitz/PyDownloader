from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import urllib.request


class Downloader(QDialog):
    # Constructor
    def __init__(self):
        QDialog.__init__(self)

        # Application layout format
        layout = QVBoxLayout()

        # Objects within layout
        self.url = QLineEdit()
        self.save_location = QLineEdit()
        progress = QProgressBar()
        download = QPushButton("Download")
        browse = QPushButton("Browse")

        # Modify widgets properties
        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File save location")
        progress.setValue(0)                                # Set progress bar to 0%
        progress.setAlignment(Qt.AlignHCenter)              # Puts the % value in the middle of the bar

        # Add objects to layout
        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(progress)
        layout.addWidget(download)


        # Set layout behavior
        self.setLayout(layout)
        self.setWindowTitle("PyDownloader")                 # Main window title
        self.setFocus()                                     # Removes focus from QLineEdit()
        
        # Event and event handler as parameter
        download.clicked.connect(self.download)
        browse.clicked.connect(self.browse_file)
        
    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Savefile As..",
                                                directory=".", filter="All Files (*.*)")
        
    # Download functionality
    def download(self):
        url = self.url.text()                               # save url in variable
        save_location = self.save_location.text()           # local machine path
        try: 
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "The download failed")
            return
        
        # After download status information and return to widget default values
        QMessageBox.information(self, "Information", "The download is complete")
        self.progress.setValue(0)        
        self.save_location.setText("")
        
    def report(self, block_num, block_size, total_size):
        read_so_far = block_num * block_size
        if total_size > 0:
            percent = read_so_far * 100 / total_size
            self.progress.setValue(int(percent))
            
# Call main window
app = QApplication(sys.argv)
dialog = Downloader()
dialog.show()
app.exec_()

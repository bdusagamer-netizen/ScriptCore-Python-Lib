"""Viewer utilities (PySide6 QWebEngineView) for ScriptCore."""
import sys
import os
import tempfile
from .core import Subfile
from typing import List

from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QListWidget, QListWidgetItem, QVBoxLayout
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView


class App(QMainWindow):
    def __init__(self, subfiles: List[Subfile]):
        super().__init__()
        self.setWindowTitle('ScriptCore Viewer')
        self.setGeometry(100, 100, 1200, 700)
        self.subfiles = subfiles
        
        # Main container
        container = QWidget()
        layout = QHBoxLayout(container)
        
        # Left panel: file list
        left_panel = QVBoxLayout()
        self.listbox = QListWidget()
        for i, sf in enumerate(subfiles):
            label = f"{sf.FileID or '<no id>'} ({sf.FileType})"
            item = QListWidgetItem(label)
            self.listbox.addItem(item)
            if sf.is_main:
                self.listbox.setCurrentRow(i)
        self.listbox.itemSelectionChanged.connect(self.on_select)
        left_panel.addWidget(self.listbox)
        left_container = QWidget()
        left_container.setLayout(left_panel)
        left_container.setMaximumWidth(300)
        
        # Right panel: viewer (web or text)
        self.web = QWebEngineView()
        
        layout.addWidget(left_container)
        layout.addWidget(self.web)
        self.setCentralWidget(container)
        
        # Show is_main file on startup
        main_index = 0
        for idx, sf in enumerate(subfiles):
            if sf.is_main:
                main_index = idx
                break
        self.show_index(main_index)

    def on_select(self):
        idx = self.listbox.currentRow()
        if idx >= 0:
            self.show_index(idx)

    def show_index(self, idx: int):
        sf = self.subfiles[idx]
        if sf.FileType.lower() == ".html":
            # Render HTML in QWebEngineView
            with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
                f.write(sf.code)
                temp_path = f.name
            self.web.load(QUrl.fromLocalFile(os.path.abspath(temp_path)))
        else:
            # Show text content
            content = f"FileID: {sf.FileID}\nFileType: {sf.FileType}\n\n{sf.code}"
            self.web.setHtml(f"<pre>{content}</pre>")


def launch_viewer(subfiles: List[Subfile]):
    app = QApplication.instance() or QApplication(sys.argv)
    w = App(subfiles)
    w.show()
    sys.exit(app.exec())


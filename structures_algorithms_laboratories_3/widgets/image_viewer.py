from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from structures_algorithms_laboratories_3.algorithms import bellman_shortest_path


class ImageViewer(QWidget):
    def __init__(self, graph, image_path):
        super().__init__()
        self.graph = graph
        self.nodes_count = len(graph)
        self.image_path = image_path
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        image_label = QLabel(self)
        image_label.setPixmap(QPixmap(self.image_path))

        source_layout = QHBoxLayout()
        source_layout.addWidget(QLabel("Source: ", self))
        self.source_edit = QLineEdit()
        source_layout.addWidget(self.source_edit)

        dest_layout = QHBoxLayout()
        dest_layout.addWidget(QLabel("Destination: ", self))
        self.dest_edit = QLineEdit()
        dest_layout.addWidget(self.dest_edit)

        self.calc_button = QPushButton("Calculate shortest distance", self)
        self.calc_button.clicked.connect(self.calc_button_slot)

        self.res_label = QLabel(self)

        layout.addWidget(image_label)
        layout.addLayout(source_layout)
        layout.addLayout(dest_layout)
        layout.addWidget(self.calc_button)
        layout.addWidget(self.res_label)

        self.setLayout(layout)

        self.setFixedSize(self.layout().sizeHint())
        self.setWindowTitle("Graph")

    @QtCore.Slot()
    def calc_button_slot(self):
        if not self.validate_edits():
            self.res_label.setText("Wrong inputs")
            return

        source, dest = int(self.source_edit.text()), int(self.dest_edit.text())
        self.res_label.setText(
            f"Shortest distance: {bellman_shortest_path(self.graph, source, dest)}"
        )

    def validate_edits(self):
        src_text, dest_text = self.source_edit.text(), self.dest_edit.text()

        if not src_text or not dest_text:
            return False
        if not src_text.isdigit() or not dest_text.isdigit():
            return False

        source = int(src_text)
        dest = int(dest_text)

        if dest >= self.nodes_count:
            return False

        if not (source >= 0 and source <= dest):
            return False

        return True

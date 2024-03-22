import tempfile
from PySide6.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from structures_algorithms_laboratories_3.utils import create_graph, read_square_matrix
from structures_algorithms_laboratories_3.widgets import ImageViewer


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Choose file with graph matrix")
        self.button.clicked.connect(self.choose_file)

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        self.setLayout(layout)

    def choose_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(
            self, "Choose file with graph matrix", "", "All Files (*)"
        )

        if file_path:
            try:
                graph = read_square_matrix(file_path)
                digraph = create_graph(graph)

                graph_file = tempfile.NamedTemporaryFile(suffix=".png")
                digraph.render(outfile=graph_file.name, format="png")
                self.viewer = ImageViewer(graph, graph_file.name)
                self.viewer.show()
                self.hide()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Wrong file format\n\n{e}")
                return

"""Main window for the MagicSquare PyQt application."""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from src.boundary.failure_result import FailureResult
from src.boundary.gui.grid_panel import GridPanel
from src.boundary.gui.random_puzzle import generate_random_puzzle
from src.control.magic_square_control import MagicSquareControl

_SAMPLE_G1_GRID: list[list[int]] = [
    [16, 2, 3, 13],
    [5, 0, 11, 8],
    [9, 6, 0, 12],
    [4, 14, 15, 1],
]


class MagicSquareMainWindow(QMainWindow):
    """4x4 partial magic square solver UI."""

    def __init__(self) -> None:
        super().__init__()
        self._control = MagicSquareControl()
        self.setWindowTitle("MagicSquare 4×4")
        self.setMinimumSize(420, 520)
        self._build_ui()

    def _build_ui(self) -> None:
        """Compose title, grid, actions, and status area."""
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(14)

        title = QLabel("4×4 마방진 — 빈칸 2개 채우기")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)

        hint = QLabel(
            "빈칸은 비워 두고, 1~16 숫자를 직접 입력하세요. "
            "행·열·대각선 합이 34가 되도록 빈칸을 채웁니다."
        )
        hint.setWordWrap(True)
        layout.addWidget(hint)

        self._grid_panel = GridPanel()
        layout.addWidget(self._grid_panel, alignment=Qt.AlignmentFlag.AlignCenter)

        button_row = QHBoxLayout()
        button_row.setSpacing(10)

        solve_btn = QPushButton("해결")
        solve_btn.setMinimumHeight(36)
        solve_btn.clicked.connect(self._on_solve)
        button_row.addWidget(solve_btn)

        sample_btn = QPushButton("샘플 불러오기")
        sample_btn.setMinimumHeight(36)
        sample_btn.clicked.connect(self._on_load_sample)
        button_row.addWidget(sample_btn)

        random_btn = QPushButton("랜덤 퍼즐")
        random_btn.setMinimumHeight(36)
        random_btn.clicked.connect(self._on_load_random)
        button_row.addWidget(random_btn)

        clear_btn = QPushButton("초기화")
        clear_btn.setMinimumHeight(36)
        clear_btn.clicked.connect(self._on_clear)
        button_row.addWidget(clear_btn)

        layout.addLayout(button_row)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(separator)

        self._status_label = QLabel("격자를 입력한 뒤 「해결」을 누르세요.")
        self._status_label.setWordWrap(True)
        layout.addWidget(self._status_label)

        layout.addStretch()

    def _on_solve(self) -> None:
        """Validate input via control layer and display the outcome."""
        grid = self._grid_panel.read_grid()
        result = self._control.solve(grid)

        if isinstance(result, FailureResult):
            self._show_failure(result)
            return

        self._grid_panel.apply_solution(result)
        row_a, col_a, val_a, row_b, col_b, val_b = result
        self._status_label.setStyleSheet("color: #1b5e20;")
        self._status_label.setText(
            "해결 완료 — "
            f"({row_a},{col_a})={val_a}, "
            f"({row_b},{col_b})={val_b}  "
            f"[{', '.join(str(v) for v in result)}]"
        )

    def _show_failure(self, failure: FailureResult) -> None:
        """Present boundary validation failure in status and dialog."""
        self._status_label.setStyleSheet("color: #b71c1c;")
        self._status_label.setText(f"[{failure.code}] {failure.message}")
        QMessageBox.warning(
            self,
            "입력 오류",
            f"{failure.message}\n\n(코드: {failure.code})",
        )

    def _on_load_sample(self) -> None:
        """Load the G1 sample puzzle from test fixtures."""
        self._grid_panel.set_grid(_SAMPLE_G1_GRID)
        self._status_label.setStyleSheet("")
        self._status_label.setText(
            "샘플 퍼즐을 불러왔습니다. 「해결」을 눌러 빈칸을 채우세요."
        )

    def _on_load_random(self) -> None:
        """Fill the grid with a random valid two-blank puzzle."""
        self._grid_panel.set_grid(generate_random_puzzle())
        self._status_label.setStyleSheet("")
        self._status_label.setText(
            "랜덤 퍼즐을 생성했습니다. 「해결」을 눌러 빈칸을 채우세요."
        )

    def _on_clear(self) -> None:
        """Reset the grid and status message."""
        self._grid_panel.clear_grid()
        self._status_label.setStyleSheet("")
        self._status_label.setText("격자를 입력한 뒤 「해결」을 누르세요.")

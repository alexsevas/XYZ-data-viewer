# v0.0.1
# conda activate cv311, hydro_env

import sys
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QSlider, QLabel, QComboBox, QFileDialog, QGroupBox,
    QSizePolicy
)
from PyQt5.QtCore import Qt
from vispy.scene import SceneCanvas, Markers, XYZAxis
from vispy.color import get_colormap, BaseColormap



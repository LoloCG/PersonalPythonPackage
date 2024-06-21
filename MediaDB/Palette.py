
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

def dark_palette():
    palette = QPalette()

    # Set the window and background colors
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, QColor(220, 220, 220))
    palette.setColor(QPalette.Base, QColor(42, 42, 42))
    palette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
    palette.setColor(QPalette.ToolTipBase, QColor(220, 220, 220))
    palette.setColor(QPalette.ToolTipText, QColor(220, 220, 220))
    
    # Set the text colors
    palette.setColor(QPalette.Text, QColor(20, 20, 20))
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    
    # Adjust button colors
    palette.setColor(QPalette.Button, QColor(80, 80, 80))
    palette.setColor(QPalette.ButtonText, QColor(20, 20, 20))  # White text for buttons

    return palette

def neon_palette():
    palette = QPalette()

    # Set the window and background colors
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(42, 42, 42))
    palette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    
    # Set the text colors
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(75, 75, 75))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    
    # Adjust button colors
    palette.setColor(QPalette.Button, QColor(50, 50, 50))
    palette.setColor(QPalette.ButtonText, QColor(200, 200, 200))  # White text for buttons

    return palette
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):


  def __init__(self):
      super().__init__()
      self.initUI()


  def initUI(self):
      # 윈도우 창 이름, 아이콘 설정
      self.setWindowTitle('PacMan')
      self.setWindowIcon(QIcon('resource/icon.png'))

      # 윈도우 창 크기 설정
      screen_rect = app.desktop().screenGeometry()
      screen_width, screen_height = screen_rect.width(),screen_rect.height()
      window_width, window_height = 1024, 1024
      self.setGeometry((screen_width//2)-(window_width//2), (screen_height//2)-(window_height//2), window_width, window_height)

      # 튤팁 나타내기
      QToolTip.setFont(QFont('SansSerif', 10))
      self.setToolTip('This is a <b>QWidget</b> widget')

      # 버튼 만들기
      btn = QPushButton('Button', self)
      btn.setToolTip('This is a <b>QPushButton</b> widget')
      btn.move(window_width//2, window_height//2)
      btn.resize(btn.sizeHint())
      btn.clicked.connect(QCoreApplication.instance().quit)




      self.show()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())

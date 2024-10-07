import sys

# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget
# 导入我们生成的界面
from ui import Ui_Form
 
# 继承QWidget类，以获取其属性和方法
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.count = 0

        self.ui.pushButton_plus.clicked.connect(self.on_pushButton_plus_clicked)
        self.ui.pushButton_minud.clicked.connect(self.on_pushButton_minud_clicked)

    def on_pushButton_plus_clicked(self):
        self.count += 1
        self.ui.label.setText(f"功德+{self.count}")

    def on_pushButton_minud_clicked(self):
        self.count -= 1
        self.ui.label.setText(f"功德-{self.count}")

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)
 
    # 初始化并展示我们的界面组件
    window = MyWidget()
    window.show()
    
    # 结束QApplication
    sys.exit(app.exec_())

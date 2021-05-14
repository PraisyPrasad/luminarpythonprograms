#methods are important not class
class Pycharm:
    def open(self):
        print("open method in pycharm")
    def run(self):
        print("run finaly in pycharm")
    def debug(self):
        print("debugging using pycharm")

class Vscode:
    def open(self):
        print("open method in vscode")
    def run(self):
        print("run finaly in vscode")
    def debug(self):
        print("debugging using vscode")

class Programer:
    def coding(self,ide):
        ide.open()
        ide.run()
        ide.debug()
py=Pycharm()
vs=Vscode()
pg=Programer()
pg.coding(vs)
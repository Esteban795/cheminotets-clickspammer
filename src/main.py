import pywinauto
import time

EXE = "jp2launcher.exe"
app = pywinauto.Application().connect(path=EXE)
while True:
    app.BienvenueSurCheminot.Button.click()
    time.sleep(1)
    
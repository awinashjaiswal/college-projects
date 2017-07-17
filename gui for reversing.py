__author__ = 'awinash'
from PyQt4 import QtGui,QtCore, Qt
import sys
import os
import cv2
from reverser import Ui_Form
class operate(QtGui.QMainWindow):

    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.cv2=cv2
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.reverse.clicked.connect(self.button)
        self.ui.browse.clicked.connect(self.browse_folder)
        self.ui.progressBar.setValue(0)


    def browse_folder(self):
        self.ui.listWidget.clear()
        self.directory=QtGui.QFileDialog.getExistingDirectory(self,"pick a folder")
        if self.directory:
            for filename in os.listdir(self.directory):
                self.ui.listWidget.addItem(filename)
            os.chdir(self.directory)


    def button(self):
        file= self.ui.listWidget.currentItem().text()
        fname=str(file)
        fname="./"+fname
        print fname
        fourcc = cv2.cv.CV_FOURCC(*'XVID')

        cap=self.cv2.VideoCapture("./"+fname)
        ret,frame=cap.read()
        col,row,ch=frame.shape
        len=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
        cv2.namedWindow('reverser', cv2.WND_PROP_FULLSCREEN)
        out = cv2.VideoWriter('output.avi',fourcc, 15.0, (row,col))


        for i in xrange(1,len):
            self.data=float(i*100/len)
            self.ui.progressBar.setValue(self.data)
            cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES,len-i)
            ret,frame=cap.read()
            self.cv2.imshow("reverser",frame)
            out.write(frame)
            if cv2.waitKey(30) & 0xFF==27:
                break
        self.cv2.destroyAllWindows()
        out.release()
        cap.release()
        self.ui.progressBar.setValue(0)



def main():

    app=QtGui.QApplication(sys.argv)
    ex=operate()
    ex.show()

    sys.exit(app.exec_())
main()

__author__ = 'awinash'
__author__ = 'awinash'
import time
import pyttsx
import sys
from PyQt4 import QtGui,QtCore, Qt
from tic_tac import Ui_Form
from play import Ui_Forme
count=0
engine=pyttsx.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',rate-100)
def loss(self,self1):
    print "loss"
    self.ui.status.setText("!!! you loss !!!")
    engine.say("you loss")
    engine.runAndWait()


def win(self,self1):
    print "wn"
    self.ui.status.setText("!!!!you win!!!!")
    engine.say("you win")
    engine.runAndWait()
    self.destroy()

a=[['' for i in range(3)]for j in range(3)]
def check(self,self1):
    print "check"
    if(a[0][0]==a[0][1]==a[0][2]  and a[0][0]=='x'):
        print "1"
        win(self,self1)
    elif( a[0][0]==a[1][0]==a[2][0] and a[0][0]=='x' ):
        win(self,self1)
    elif(a[0][0]==a[1][1]==a[2][2] and a[0][0]=='x'):
        win(self,self1)
    elif(a[0][0]==a[0][1]==a[0][2] and a[0][0]=='o'):
        loss(self,self1)
        print "2"
    elif(a[0][0]==a[1][0]==a[2][0] and a[0][0]=='o' ):
        loss(self,self1)
    elif(a[0][0]==a[1][1]==a[2][2] and a[0][0]=='o'):
        loss(self,self1)
    elif(a[1][0]==a[1][1]==a[1][2] and a[1][0]=='x'):
        win(self,self1)
        print "3"


    elif(a[1][0]==a[1][1]==a[1][2] and a[1][0]=='o'):
        loss(self,self1)
        print "4"


    elif(a[2][0]==a[2][1]==a[2][2]  and a[2][0]=='x'):
        win(self,self1)
    elif(a[2][0]==a[1][1]==a[0][2] and a[2][0]=='x'):
        win(self,self1)
    elif(a[2][0]==a[2][1]==a[2][2]  and a[2][0]=='o'):
        loss(self,self1)
        print "6"
    elif(a[2][0]==a[1][1]==a[0][2] and a[2][0]=='o'):
        loss(self,self1)
    elif(a[2][2]==a[1][2]==a[0][2] and a[2][2]=='x'):
        win(self,self1)
        print "7"

    elif( a[2][2]==a[1][2]==a[0][2] and a[2][2]=='o'):
        loss(self,self1)
        print "8"

    elif(a[0][1]==a[1][1]==a[2][1] and a[0][1]=='x'):
        win(self,self1)
        print "9"

    elif(a[0][1]==a[1][1]==a[2][1] and a[0][1]=='o'):
        loss(self,self1)
        print "10"
    elif(a[0][0]!='' and a[0][1]!='' and a[0][2]!='' and a[1][0]!='' and a[1][1]!='' and a[1][2]!='' and a[2][0]!='' and a[2][1]!='' and a[2][2]!=''):
        self.ui.status.setText("!!! tie !!!")
        engine.say("its a tie")
        print "here"
#********** arbitary position*************
def rand():
    if(a[0][2]=='o' and a[0][0]==a[0][1]==''):
        a[0][0]='o'
    elif(a[0][2]=='o' and a[1][1]==a[2][0]==''):
        a[0][2]='o'

    elif(a[0][1]=='o' and a[0][0]==a[0][2]==''):
        a[0][0]='o'

    elif( a[0][0]=='o' and a[0][1]==a[0][2]=='' ):
                    #0 0 done
        a[0][1]='o'

    elif(a[0][0]=='o' and a[1][0]==a[2][0]==''):
        a[2][0]='o'
    elif(a[0][0]=='o' and a[1][1]==a[2][2]==''):
        a[1][1]='o'
    elif( a[1][0]=='o'and a[0][0]==a[2][0]==''):                  # 1 0 done

        a[2][0]='o'
    elif(a[1][0]=='o' and a[1][1]==a[1][2]==''):
        a[1][1]='o'                # 2 0 done
    elif(a[2][0]=='o'and a[0][0]==a[1][0]=='' ):
        a[1][0]='o'
    elif(a[2][0]=='o' and a[0][2]==a[1][1]=='' ):
        a[1][1]='o'
    elif(a[2][0]=='o' and a[2][1]==a[2][2]==''):
        a[2][2]='o'
    elif(a[2][2]=='o' and a[0][0]==a[1][1]=='' ):
                                # 22 done
        a[0][0]='o'
    elif(a[2][2]=='o' and a[0][2]==a[1][2]==''):    #1  #22
        a[0][2]='o'
    elif(a[2][2]=='o' and a[2][0]==a[2][1]=='' ):    #1 #22
        a[2][0]='o'

    elif(a[1][1]=='o' and a[0][0]==a[2][2]==''):
                #2 #1 *11
        a[2][2]='o'
    elif(a[1][1]=='o' and a[0][1]==a[2][1]==''):    #2 #2*11
        a[0][1]='o'
    elif(a[1][1]=='o' and a[0][2]==a[2][0]==''):    #2 #3*11
        a[0][2]='o'
    elif(a[1][1]=='o' and a[1][0]==a[1][2]=='' ):    #2 #4*11
        a[1][0]='o'

    elif(a[2][1]=='o' and a[2][0]==a[2][2]==''):
                                      #2 #2*21
        a[2][2]='o'
    elif(a[2][1]=='o' and a[0][1]==a[1][1]=='' ):    #1 #1*21
        a[1][1]='o'

    elif(a[1][2]=='o' and a[1][0]==a[1][1]==''):
                                            #1 #2*12
        a[1][1]='o'
    elif(a[1][2]=='o' and a[0][2]==a[2][2]==''):    #2 #1*12
        a[2][2]='o'
#**********************computer**********************************
def comp():
    if(a[0][0]==a[0][1]=='x' and a[0][2]=='' ):
        a[0][2]='o'
    else:
        if(a[0][0]==a[0][2]=='x' and a[0][1]==''):
            a[0][1]='o'
        else:
            if(a[0][1]==a[0][2]=='x' and a[0][0]=='' ):    #3
                a[0][0]='o'
            else:
                if(a[0][0]==a[2][0]=='x' and a[1][0]==''):    #
                    a[1][0]='o'
                else:
                    if(a[0][0]==a[1][0]=='x' and a[2][0]==''):    #2
                        a[2][0]='o'
                    else:
                        if(a[1][0]==a[2][0]=='x' and a[0][0]==''):    #3
                            a[0][0]='o'
                        else:
                            if(a[0][0]==a[1][1]=='x' and a[2][2]=='' ):    #1
                                a[2][2]='o'
                            else:
                                if(a[0][0]==a[2][2]=='x' and a[1][1]==''):    #2
                                    a[1][1]='o'
                                else:
                                    if(a[1][1]==a[2][2]=='x' and a[0][0]==''):    #3
                                        a[0][0]='o'
                                    else:
                                        if(a[0][1]==a[1][1]=='x' and a[2][1]=='' ):
                                            a[2][1]='o'
                                        else:
                                            if(a[0][1]==a[2][1]=='x' and a[1][1]==''):
                                                a[1][1]='o'
                                            else:
                                                if(a[1][1]==a[2][1]=='x'and a[0][1]=='' ):    #3
                                                    a[0][1]='o'

                                                else:
                                                    if(a[0][2]==a[1][1]=='x'and a[2][0]=='' ):    #1
                                                         a[2][0]='o'

                                                    else:
                                                        if(a[0][2]==a[2][0]=='x' and a[1][1]==''):    #2
                                                            a[1][1]='o'

                                                        else:
                                                            if(a[1][1]==a[2][0]=='x' and a[0][2]=='' ):    #3
                                                                 a[0][2]='o'

                                                            else:
                                                                if(a[0][2]==a[1][2]=='x' and a[2][2]==''):    #1
                                                                   a[2][2]='o'

                                                                else:
                                                                    if(a[0][2]==a[2][2]=='x' and a[1][2]==''):    #2
                                                                       a[1][2]='o'

                                                                    else:
                                                                        if(a[1][2]==a[2][2]=='x' and a[0][2]==''):    #3
                                                                           a[0][2]='o'

                                                                        else:
                                                                            if(a[1][0]==a[1][1]=='x'and a[1][2]==''  ):    #1
                                                                               a[1][2]='o'

                                                                            else:
                                                                                if(a[1][0]==a[1][2]=='x'and  a[1][1]==''):    #2
                                                                                   a[1][1]='o'

                                                                                else:
                                                                                    if(a[1][1]==a[1][2]=='x' and a[1][0]==''):    #3
                                                                                        a[1][0]='o'

                                                                                    else:
                                                                                        if(a[2][0]==a[2][1]=='x'and a[2][2]=='' ):    #1
                                                                                             a[2][2]='o'

                                                                                        else:
                                                                                            if(a[2][0]==a[2][2]=='x' and a[2][1]==''):    #2
                                                                                               a[2][1]='o'

                                                                                            else:
                                                                                                if(a[2][1]==a[2][2]=='x'and a[2][0]==''):    #3
                                                                                                    a[2][0]='o'
                                                                                                else:
                                                                                                    rand()

#**********self suggestion****************

def cself(self):
    if(a[0][0]==a[0][1]=='o' and a[0][2]==''): #1
            a[0][2]='o'
            #loss(self)

    elif(a[0][0]==a[0][2]=='o' and a[0][1]==''):  #2

            a[0][1]='o'
            #loss(self)

    elif(a[0][1]==a[0][2]=='o' and a[0][0]==''):    #3

            a[0][0]='o'
            #loss(self)

    elif(a[0][0]==a[2][0]=='o' and a[1][0]==''):    #1

            a[1][0]='o'
            #loss(self)


    elif(a[0][0]==a[1][0]=='o' and a[2][0]==''):    #2
            a[2][0]='o'
            #loss(self)


    elif(a[1][0]==a[2][0]=='o' and a[0][0]==''):    #3

        a[0][0]='o'
        #loss(self)


    elif(a[0][0]==a[1][1]=='o' and a[2][2]=='' ):    #1 #22

        a[2][2]='o'
        #loss(self)


    elif(a[0][0]==a[2][2]=='o' and a[1][1]==''):    #2 #1 *11

        a[1][1]='o'
        #loss(self)


    elif(a[1][1]==a[2][2]=='o' and a[0][0]==''):    #3

        a[0][0]='o'
        #loss(self)


    elif(a[0][1]==a[1][1]=='o' and a[2][1]=='' ):    #1 #1*21

        a[2][1]='o'
        #loss(self)


    elif(a[0][1]==a[2][1]=='o' and a[1][1]==''):    #2 #2*11

        a[1][1]='o'
        #loss(self)


    elif(a[0][0]==a[0][2]=='o' and a[0][1]==''):  #3

        a[0][1]='o'
        #loss(self)


    elif(a[0][2]==a[1][1]=='o' and a[2][0]==''):    #1

        a[2][0]='o'
        #loss(self)


    elif(a[0][2]==a[2][0]=='o' and a[1][1]==''):    #2 #3*11

        a[1][1]='o'
        #loss(self)


    elif(a[1][1]==a[2][0]=='o' and a[0][2]==''):    #3

        a[0][2]='o'
        #loss(self)


    elif(a[0][2]==a[1][2]=='o' and a[2][2]==''):    #1  #22

        a[2][2]='o'
        #loss(self)


    elif(a[0][2]==a[2][2]=='o' and a[1][2]==''):    #2 #1*12

        a[1][2]='o'
        #loss(self)


    elif(a[1][2]==a[2][2]=='o'  and a[0][2]==''):    #3

        a[0][2]='o'
        #loss(self)


    elif(a[1][0]==a[1][1]=='o' and a[1][2]=='' ):    #1 #2*12

        a[1][2]='o'
        #loss(self)


    elif(a[1][0]==a[1][2]=='o' and a[1][1]==''):    #2 #4*11

        a[1][1]='o'
        #loss(self)


    elif(a[1][1]==a[1][2]=='o' and a[1][0]==''):    #3

        a[1][0]='o'
        #loss(self)


    elif(a[2][0]==a[2][1]=='o' and a[2][2]==''):    #1 #22

        a[2][2]='o'
        #loss(self)
    elif(a[2][0]==a[2][2]=='o'and a[2][1]=='' ):    #2 #2*21

        a[2][1]='o'
        #loss(self)


    elif(a[2][1]==a[2][2]=='o' and a[2][0]==''):    #3

        a[2][0]='o'
        #loss(self)

    else:
        comp()








def cnt(self):
    if(count==1):
        if(a[0][0]==''):
            a[0][0]='o'
            self.ui.label1.setText('o')
        elif(a[0][0]!=''):
            a[1][1]='o'
            self.ui.label5.setText('o')
    else:
        cself(self)
def fll(self,self1):
            self.ui.label1.setText(a[0][0])
            self.ui.label2.setText(a[0][1])
            self.ui.label3.setText(a[0][2])
            self.ui.label4.setText(a[1][0])
            self.ui.label5.setText(a[1][1])
            self.ui.label6.setText(a[1][2])
            self.ui.label7.setText(a[2][0])
            self.ui.label8.setText(a[2][1])
            self.ui.label9.setText(a[2][2])
            check(self,self1)
class compute(QtGui.QMainWindow):

    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.push1.clicked.connect(self.pus1)
        self.ui.push2.clicked.connect(self.pus2)
        self.ui.push3.clicked.connect(self.pus3)
        self.ui.push4.clicked.connect(self.pus4)
        self.ui.push5.clicked.connect(self.pus5)
        self.ui.push6.clicked.connect(self.pus6)
        self.ui.push7.clicked.connect(self.pus7)
        self.ui.push8.clicked.connect(self.pus8)
        self.ui.push9.clicked.connect(self.pus9)







    def pus1(self,self1):
        global count
        if(a[0][0]=='' ):
            self.ui.label1.setText("x")
            a[0][0]="x"
            count+=1
            fll(self,self1)
            check(self,self1)
            self.ui.status.setText("wait....")
            cnt(self)
            fll(self,self1)
            self.ui.status.setText("your turn")
        else:
            self.ui.status.setText("allerady filled")

    def pus2(self,self1):
        global count
        if(a[0][1]=='' ):
            self.ui.label2.setText("x")
            a[0][1]="x"
            fll(self,self1)
            check(self,self1)
            count+=1
            self.ui.status.setText("wait....")
            cnt(self)
            fll(self,self1)
            self.ui.status.setText("your turn")
        else:
            self.ui.status.setText("allerady filled")

    def pus3(self,self1):
        global count
        if(a[0][2]=='' ):
            self.ui.label3.setText("x")
            a[0][2]="x"
            fll(self,self1)
            check(self,self1)
            count+=1
            self.ui.status.setText("wait....")
            cnt(self)
            fll(self,self1)
            self.ui.status.setText("your turn")
        else:
            self.ui.status.setText("allerady filled")

    def pus4(self,self1):
        global count
        if(a[1][0]=='' ):
            self.ui.label4.setText("x")
            a[1][0]="x"
            fll(self,self1)
            check(self,self1)
            count+=1
            self.ui.status.setText("wait....")
            cnt(self)
            fll(self,self1)
            self.ui.status.setText("your turn")
        else:
            self.ui.status.setText("allerady filled")

    def pus5(self,self1):
        global count
        if(a[1][1]=='' ):
            self.ui.label5.setText("x")
            a[1][1]="x"
            fll(self,self1)
            check(self,self1)
            count+=1
            self.ui.status.setText("wait....")
            cnt(self)
            fll(self,self1)
            self.ui.status.setText("your turn")
        else:
            self.ui.status.setText("allerady filled")


    def pus6(self,self1):
        global count
        if(a[1][2]=='' ):
            self.ui.label6.setText("x")
            a[1][2]="x"
            fll(self,self1)
            check(self,self1)
            count+=1
            self.ui.status.setText("wait....")
            cnt(self)
            fll(self,self1)
            self.ui.status.setText("your turn")
        else:
            self.ui.status.setText("allerady filled")

    def pus7(self,self1):
        global count
        if(a[2][0]=='' ):
            self.ui.label7.setText("x")
            a[2][0]="x"
            fll(self,self1)
            check(self,self1)
            count+=1
            self.ui.status.setText("wait....")
            cnt(self)
            fll(self,self1)
            self.ui.status.setText("your turn")
        else:
            self.ui.status.setText("allerady filled")
    def pus8(self,self1):
        global count
        if(a[2][1]=='' ):
            self.ui.label8.setText("x")
            a[2][1]="x"
            fll(self,self1)
            check(self,self1)
            count+=1
            self.ui.status.setText("wait....")
            cnt(self)
            fll(self,self1)
            self.ui.status.setText("your turn")
        else:
            self.ui.status.setText("allerady filled")
    def pus9(self,self1):
        global count
        if(a[2][2]=='' ):
            self.ui.label9.setText("x")
            a[2][2]="x"
            fll(self,self1)
            check(self,self1)
            count+=1
            self.ui.status.setText("wait....")
            cnt(self)
            fll(self,self1)
            self.ui.status.setText("your turn")
        else:
            self.ui.status.setText("allerady filled")


def main():
    app=QtGui.QApplication(sys.argv)
    ex=compute()
    ex.show()

    sys.exit(app.exec_())
main()


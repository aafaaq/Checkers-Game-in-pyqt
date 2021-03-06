# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    label_list = []
    def setupUi(self, MainWindow):
        self.board = self.make_board()
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 674)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 661))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("base.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        #self.main()
        self.set_geomatery()
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def set_geomatery(self):
        count = 0
        for x in range(0,10):
            for y in range(0,10):
                if self.board[x][y] == 1:
                    label = QtWidgets.QLabel(self.centralwidget)
                    self.label_list.append(label)
                    x_cor = (73*y)+4
                    y_cor = (66*x)+8
                    self.label_list[count].setGeometry(QtCore.QRect(x_cor,y_cor,61,51))
                    self.label_list[count].setText("")
                    self.label_list[count].setPixmap(QtGui.QPixmap("green.png"))
                    self.label_list[count].setScaledContents(True)
                    self.label_list[count].setObjectName("label_"+str(count))
                    count = count+1
                if self.board[x][y] == 2:
                    label = QtWidgets.QLabel(self.centralwidget)
                    self.label_list.append(label)
                    x_cor = (73*y)+4
                    y_cor = (66*x)+8
                    self.label_list[count].setGeometry(QtCore.QRect(x_cor,y_cor,61,51))
                    self.label_list[count].setText("")
                    self.label_list[count].setPixmap(QtGui.QPixmap("blue.png"))
                    self.label_list[count].setScaledContents(True)
                    self.label_list[count].setObjectName("label_"+str(count))
                    count = count+1       
                            
    def make_board(self):
         # making of checker board
        board = []
        r0 = [0,2,0,2,0,2,0,2,0,2]
        r2 = [0,2,0,2,0,2,0,2,0,2]
        z1 = [0,0,0,0,0,0,0,0,0,0]
        z2 = [0,0,0,0,0,0,0,0,0,0]
        r1   = [2,0,2,0,2,0,2,0,2,0]
        r3   = [2,0,2,0,2,0,2,0,2,0]
        r7 = [1,0,1,0,1,0,1,0,1,0]
        r9 = [1,0,1,0,1,0,1,0,1,0]
        r6   = [0,1,0,1,0,1,0,1,0,1]
        r8   = [0,1,0,1,0,1,0,1,0,1]

        board.append(r0)
        board.append(r1)
        board.append(r2)
        board.append(r3)
        board.append(z1)
        board.append(z2)
        board.append(r6)
        board.append(r7)
        board.append(r8)
        board.append(r9)
        return board


    def print_board(self):
        count = 0
        print()
        print("    0 1 2 3 4 5 6 7 8 9")
        for row in self.board:
            print(count,"| ", end = '')
            for index in row:
                if index == 0:
                    print(". ", end = '')
                elif index == 1:
                    print("o ", end = '') 
                elif index == 2:
                    print("??? ", end = '')
            print("|")
            count += 1 
                
    
    def swap(self,i,j,k,l):
        print("Swap from ",i,",",j," to ",k,",",l)
        temp = self.board[i][j]
        self.board[i][j] = self.board[k][l]
        self.board[k][l] = temp
        #print_board(board)


    def user_move(self,player,i,j,k,l):
        if i < 0 and 9 <= i : 
            print("Selection row is out of bounds");
            return -1;
        
        if j < 0 and 9 <= j : 
            print("Selection row is out of bounds");
            return -1;
            
        if k < 0 and 9 <= k : 
            print("Move to row is out of bounds");
            return -1;
        if l < 0 and 9 <= l : 
            print("Move to column is out of bounds");
            return -1;
        if self.board[k][l]!=0:
            print("You must move to an empty location")
            return -1
        if player == 1:
            if self.board[i][j] != 1:
                print("Move your own piece!");
                return -1;
            if i<=k:
                print("Green player must move upwards");
                return -1
            if k<(i-2):
                print("You can only move upto 2 blocks")
                return -1
        if player == 2:
            if self.board[i][j] != 2:
                print("Move your own piece!");
                return -1;
            if i>=k:
                print("Blue player must move downwards");
                return -1
            if k>(i+2):
                print("You can only move upto 2 blocks")
                return -1
        if i - k == -1 or i - k == 1:
            if j - l == 1 or j - l == -1:
                print("//////////////////")
                self.swap(i,j,k,l);
                return 0;


        if i - k == -2 or i - k == 2:
            if j - l == -2 or j - l == 2:
                if i < k: 
                    jmp_r = i + 1;
                else: 
                    jmp_r = i - 1;
                if j < l: 
                    jmp_c = j + 1;
                else:
                    jmp_c = j - 1;
                
                
                if player==1 and self.board[jmp_r][jmp_c]!=2:
                    print("Enemeny is not Blue at" ,jmp_r, jmp_c);
                    return -1;
                
                if player==2 and self.board[jmp_r][jmp_c] != 1:
                    print("Enemeny is not Green at" ,jmp_r, jmp_c);
                    return -1;
                
                self.board[jmp_r][jmp_c] = 0;
                self.swap(i,j,k,l);
                return 0;
    
    
    def check_win(self):
        one = 0
        two = 0
        for row in range(0,10):
            for col in range(0,10):
                if self.board[row][col]==1:
                    one += 1
                if self.board[row][col]==2:
                    two += 2
        
        if two == 0:
            return 1
        if one == 0:
            return 2
        return 0            
                
                                   
   
    def main(self):
        self.set_geomatery()
        while(True):
            self.print_board()
            print("Green Turn:")
            print("Selection:-")
            i = int(input("Select row : "))
            j = int(input("Select column : "))
            print("Move to: ")
            k = int(input("Move to row : "))
            l = int(input("Move to column : "))
            if self.user_move(1,i,j,k,l)==0:
                self.set_geomatery()
                break
            print("Wrong input try again")
        
        self.set_geomatery()    
        while(True):   
            self.print_board()
            print("Blue Turn:")
            print("Selection:-")
            i = int(input("Select row : "))
            j = int(input("Select column : "))
            print("Move to: ")
            k = int(input("Move to row : "))
            l = int(input("Move to column : "))
            if self.user_move(2,i,j,k,l)==0:
                break
            print("Wrong input try again")
        win = self.check_win()
        if win==2:
            print("Blue won.")
            exit()
        if win==1:
            print("Green won.")
            exit()    
    def main_2(self):
        self.set_geomatery()
        while(True):
            self.print_board()
            print("Green Turn:")
            print("Selection:-")
            i = int(input("Select row : "))
            j = int(input("Select column : "))
            print("Move to: ")
            k = int(input("Move to row : "))
            l = int(input("Move to column : "))
            if self.user_move(1,i,j,k,l)==0:
                self.set_geomatery()
                break
            print("Wrong input try again")
        
        self.set_geomatery()    
        while(True):   
            self.print_board()
            print("Computer Blue Turn:")
            x = 0
            y = 0
            k = 0
            l = 0
            found = 0
            for row in range(0,10):
                for col in range(0,10):
                    if row+1 <= 9 and col+1<=9 and col-1>=0:
                        if self.board[row][col]==2 and self.board[row+1][col+1]==0 and row+1 != 10 and col+1!=10:
                            print("...................................................................")
                            x =  row
                            y =  col 
                            k =  row+1
                            l =  col+1
                            found = 1
                            break
                        if self.board[row][col]==2 and self.board[row+1][col-1]==0 and row+1 != 10 and col-1!=0:
                            print("...................................................................")
                            x =  row
                            y =  col 
                            k =  row+1
                            l =  col-1
                            found = 1
                            break
                if found == 1:
                    break    
            if x==0 and y==0 and k == 0 and l ==0:
                print("Green won Computer cannot move.")
                exit()                   
            if self.user_move(2,x,y,k,l)==0:
                break
            print("Wrong input try again")
        
        win = self.check_win()
        if win==2:
            print("Blue won.")
            exit()
        if win==1:
            print("Green won.")
            exit()                    
                
            

    
    
    
    
    



def mood():
    print("Which mood you want to play: ")
    print("1: Player Vs Player ")
    print("2: Player Vs Computer")
    choice = int(input("-> "))
    return choice
    





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    choice = mood()
    if choice == 1:
        while(True):
            MainWindow.show()
            ui.main()
    elif choice == 2:
        while(True):
            MainWindow.show()
            ui.main_2()
    else:
        print("Wrong choice")
        MainWindow.close()                
    sys.exit(app.exec_())
    
    




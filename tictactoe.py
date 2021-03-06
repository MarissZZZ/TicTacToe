from cgitb import text
from importlib.machinery import WindowsRegistryFinder
from distutils import command
from faulthandler import disable
from tkinter import *
from tkinter import messagebox #paziņojumi, ieteikumi

mansLogs=Tk()
mansLogs.title("TicTacToe")

speletajsX=True #kuram spleletajam karta spelet, liks krustinus
count=0 #aizpilda rutinu skaitu


#--------------------------------------------------------------------------------------------

def disableButtons(): #spele beidzas, pogas izslegtas
    btn1.config(state=DISABLED) #pogas stavoklis izslegts
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)
    return 0

#--------------------------------------------------------------------------------------------

def reset():
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn1['text']=''
    btn2['text']=''
    btn3['text']=''
    btn4['text']=''
    btn5['text']=''
    btn6['text']=''
    btn7['text']=''
    btn8['text']=''
    btn9['text']=''
    btn1['background']='peachpuff3'
    btn2['background']='lightgoldenrodyellow'
    btn3['background']='peachpuff3'
    btn4['background']='lightgoldenrodyellow'
    btn5['background']='peachpuff3'
    btn6['background']='lightgoldenrodyellow'
    btn7['background']='peachpuff3'
    btn8['background']='lightgoldenrodyellow'
    btn9['background']='peachpuff3'

    global winner,count,speletajsX
    winner=False
    count=0
    speletajsX=True
    return 0

#--------------------------------------------------------------------------------------------

def btnClick(button): #padod pogui
    global speletajsX, count #kadi mainigie tiks izmantoti
    if button["text"]=='' and speletajsX==True: #spele X speletajs
        button["text"]='X' #maina uz X
        button['foreground']='red'
        speletajsX=False
        count+=1 #palielina rutinu skaitu
        checkWinner()
    elif button["text"]=='' and speletajsX==False: #spele O speletajs
        button["text"]='O' #maina uz )
        button['foreground']='blue'
        speletajsX=True
        count+=1 #palielina rutinu skaitu
        checkWinner()
    else:
        messagebox.showerror('TicTacToe', 'Šeit kāds ir ieklikšķinājis')
    return

#--------------------------------------------------------------------------------------------

def checkWinner():
    global winner
    if (btn1["text"]=="X" and btn2["text"]=="X" and btn3["text"]=="X"):
        winner=True
        btn1['background']='red'
        btn2['background']='red'
        btn3['background']='red'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs X ir uzvarētājs')
    if (btn1["text"]=="X" and btn4["text"]=="X" and btn7["text"]=="X"):
        winner=True
        btn1['background']='red'
        btn4['background']='red'
        btn7['background']='red'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs X ir uzvarētājs')
    if (btn4["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X"):
        winner=True
        btn4['background']='red'
        btn5['background']='red'
        btn6['background']='red'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs X ir uzvarētājs')
    if (btn7["text"]=="X" and btn8["text"]=="X" and btn9["text"]=="X"):
        winner=True
        btn7['background']='red'
        btn8['background']='red'
        btn9['background']='red'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs X ir uzvarētājs')
    if (btn2["text"]=="X" and btn5["text"]=="X" and btn8["text"]=="X"):
        winner=True
        btn2['background']='red'
        btn5['background']='red'
        btn8['background']='red'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs X ir uzvarētājs')  
    if (btn3["text"]=="X" and btn6["text"]=="X" and btn9["text"]=="X"):
        winner=True
        btn3['background']='red'
        btn6['background']='red'
        btn9['background']='red'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs X ir uzvarētājs') 
    if (btn1["text"]=="X" and btn5["text"]=="X" and btn9["text"]=="X"):
        winner=True
        btn1['background']='red'
        btn5['background']='red'
        btn9['background']='red'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs X ir uzvarētājs') 
    if (btn3["text"]=="X" and btn5["text"]=="X" and btn7["text"]=="X"):
        winner=True
        btn3['background']='red'
        btn5['background']='red'
        btn7['background']='red'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs X ir uzvarētājs')
    elif (btn1["text"]=="O" and btn2["text"]=="O" and btn3["text"]=="O"):
        winner=True
        btn1['background']='blue'
        btn2['background']='blue'
        btn3['background']='blue'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs O ir uzvarētājs')
    elif (btn1["text"]=="O" and btn4["text"]=="O" and btn7["text"]=="O"):
        winner=True
        btn1['background']='blue'
        btn4['background']='blue'
        btn7['background']='blue'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs O ir uzvarētājs')
    elif (btn4["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O"):
        winner=True
        btn4['background']='blue'
        btn5['background']='blue'
        btn6['background']='blue'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs O ir uzvarētājs')
    elif (btn7["text"]=="O" and btn8["text"]=="O" and btn9["text"]=="O"):
        winner=True
        btn7['background']='blue'
        btn8['background']='blue'
        btn9['background']='blue'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs O ir uzvarētājs')
    elif (btn2["text"]=="O" and btn5["text"]=="O" and btn8["text"]=="O"):
        winner=True
        btn2['background']='blue'
        btn5['background']='blue'
        btn8['background']='blue'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs O ir uzvarētājs')
    elif (btn3["text"]=="O" and btn6["text"]=="O" and btn9["text"]=="O"):
        winner=True
        btn3['background']='blue'
        btn6['background']='blue'
        btn9['background']='blue'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs O ir uzvarētājs')
    elif (btn1["text"]=="O" and btn5["text"]=="O" and btn9["text"]=="O"):
        winner=True
        btn1['background']='blue'
        btn5['background']='blue'
        btn9['background']='blue'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs O ir uzvarētājs')
    elif (btn3["text"]=="O" and btn5["text"]=="O" and btn7["text"]=="O"):
        winner=True
        btn3['background']='blue'
        btn5['background']='blue'
        btn7['background']='blue'
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēlētājs O ir uzvarētājs')
    elif count==9 and winner==False:
        winner=False
        disableButtons()
        messagebox.showinfo('TicTacToe', 'Spēles rezultāts ir neizšķirts')
    return

#--------------------------------------------------------------------------------------------

def infoLogs():
    jaunsLogs=Toplevel()
    jaunsLogs.title('Info par programmu')
    jaunsLogs.geometry('600x200')
    apraksts=Label(jaunsLogs,text='SPĒLES NOTEIKUMI')
    apraksts.grid(row=0,column=0)
    apraksts=Label(jaunsLogs,text='Spēlētāji pēc kārtas lauka brīvajās rūtiņās izvieto pa vienai savai figūrai (krustiņus vai nullītes).')
    apraksts.grid(row=1,column=0)
    apraksts=Label(jaunsLogs,text='Pirmo gājienu izlaist nav iespējams.')
    apraksts.grid(row=2,column=0)
    apraksts=Label(jaunsLogs,text='Pirmo gājienu veic spēlētājs, kurš spēlē ar krustiņiem.')
    apraksts.grid(row=3,column=0)
    apraksts=Label(jaunsLogs,text='Spēlē uzvar spēlētājs, kurš izvietojis kopā 3 savas figūras vienā rindā, kolonnā vai uz diagonāles.')
    apraksts.grid(row=4,column=0)
    apraksts=Label(jaunsLogs,text='Spēles rezultāts ir neizšķirts, ja uz spēles lauka nav palikusi neviena brīva rūtiņa un spēlē neviens nav uzvarējis.')
    apraksts.grid(row=5,column=0)
    return 0

#--------------------------------------------------------------------------------------------

btn1=Button(mansLogs,text="", width=6,height=3,font=('Helvica',24), bd=10, bg='peachpuff3', activebackground='peachpuff4', command=lambda:btnClick(btn1))
btn2=Button(mansLogs,text="", width=6,height=3,font=('Helvica',24), bd=10, bg='lightgoldenrodyellow', activebackground='lemonchiffon3', command=lambda:btnClick(btn2))
btn3=Button(mansLogs,text="", width=6,height=3,font=('Helvica',24), bd=10, bg='peachpuff3', activebackground='peachpuff4', command=lambda:btnClick(btn3))
btn4=Button(mansLogs,text="", width=6,height=3,font=('Helvica',24), bd=10, bg='lightgoldenrodyellow', activebackground='lemonchiffon3', command=lambda:btnClick(btn4))
btn5=Button(mansLogs,text="", width=6,height=3,font=('Helvica',24), bd=10, bg='peachpuff3', activebackground='peachpuff4', command=lambda:btnClick(btn5))
btn6=Button(mansLogs,text="", width=6,height=3,font=('Helvica',24), bd=10, bg='lightgoldenrodyellow', activebackground='lemonchiffon3', command=lambda:btnClick(btn6))
btn7=Button(mansLogs,text="", width=6,height=3,font=('Helvica',24), bd=10, bg='peachpuff3', activebackground='peachpuff4', command=lambda:btnClick(btn7))
btn8=Button(mansLogs,text="", width=6,height=3,font=('Helvica',24), bd=10, bg='lightgoldenrodyellow', activebackground='lemonchiffon3', command=lambda:btnClick(btn8))
btn9=Button(mansLogs,text="", width=6,height=3,font=('Helvica',24), bd=10, bg='peachpuff3', activebackground='peachpuff4', command=lambda:btnClick(btn9))

#--------------------------------------------------------------------------------------------

#liela izvelne
galvenaIzvelne=Menu(mansLogs) #izveido galveno izvelni
mansLogs.config(menu=galvenaIzvelne) #pievieno galvenajam logam

#--------------------------------------------------------------------------------------------

#Maza izvelne​
opcijas=Menu(galvenaIzvelne,tearoff=False) #maza izvelne
galvenaIzvelne.add_cascade(label='Opcijas',menu=opcijas) #lejupkritosais saraksts

#--------------------------------------------------------------------------------------------

#komandas
opcijas.add_command(label="Jauna spēle",command=reset)
opcijas.add_command(label="Iziet",command=mansLogs.quit)

galvenaIzvelne.add_command(label='Spēles noteikumi',command=infoLogs) #pievieno mazajai izvelnei

#--------------------------------------------------------------------------------------------

btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)
btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)

mansLogs.mainloop()

#--------------------------------------------------------------------------------------------
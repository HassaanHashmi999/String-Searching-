from tkinter import *
import tkinter.font as font


def KMPSearch():
    ele=[]
    top=Toplevel()
    top.title("KMPSearch")
    top.configure(bg="#52796F",bd=5,relief=RAISED,highlightbackground="#52796F",highlightcolor="#52796F",highlightthickness=3)
    top.geometry('1200x600')
    findtext=input1.get()
    frami = Frame(top,bg='#354F52',padx=10,pady=15, borderwidth=3,relief="sunken")
    frami.pack(side=TOP,fill=BOTH,expand=True)
    files=["Research#1.txt","Research#2.txt","Research#3.txt","Research#4.txt","Research#5.txt","Research#6.txt","Research#7.txt","Research#8.txt","Research#9.txt","Research#10.txt"]
    M = len(findtext)
    for file in files:
        fp=open(file,'r')
        lines=fp.readlines()
        lineno=1
        for line in lines:
            if(M_C.get()==1):
                N = len(line)
                lps = [0]*M
                j = 0 
                computeLPSArrayMC(findtext, M, lps)   
                i = 0
                while (N - i) >= (M - j):
                    if findtext[j] == line[i]:
                        i += 1
                        j += 1 
                    if j == M:
                        if (Wword.get()==0):
                            if (j == M):
                                ele1="Pattern found at index:"+str (i-j+1)+" line:"+str(lineno)+" file:"+str(file)
                                ele.append(ele1)
                        elif(Wword.get()==1):
                            for word in line.split():
                                if (j == M and word.upper()==findtext.upper()):
                                    ele1="Word:"+str(word) +" found at index:"+str (i-j+1)+" line:"+str(lineno)+" file:"+str(file)
                                    ele.append(ele1)
                        j = lps[j-1]
                    elif i < N and findtext[j] != line[i]:
                        if j!=0:
                            j=lps[j-1]
                        else:
                            i+=1
                lineno+=1
            if(M_C.get()==0):
                N = len(line)
                lps = [0]*M
                j = 0 
                computeLPSArrayMC(findtext.upper(), M, lps)   
                i = 0
                while (N - i) >= (M - j):
                    if findtext[j].upper() == line[i].upper():
                        i += 1
                        j += 1 
                    if j == M:
                        if (Wword.get()==0):
                            if (j == M):
                                ele1="Pattern found at index:"+str (i-j+1)+" line:"+str(lineno)+" file:"+str(file)
                                ele.append(ele1)
                        elif(Wword.get()==1):
                            for word in line.split():
                                if (j == M and word.upper()==findtext.upper()):
                                    ele1="Word:"+str(word) +" found at index:"+str (i-j+1)+" line:"+str(lineno)+" file:"+str(file)
                                    ele.append(ele1)
                        j = lps[j-1]
                    elif i < N and findtext[j].upper() != line[i].upper():
                        if j!=0:
                            j=lps[j-1]
                        else:
                            i+=1
                lineno+=1
    mylabel=Label(frami,text='The Word "'+str(input1.get())+'" Found using KMP Method',bg='#354F52',fg="#84A98C",pady=10)
    mylabel['font']=myFont
    mylabel.pack(side=TOP)
    scle=Scrollbar(frami,bd=2,troughcolor='#354F52',bg="#84A98C",activebackground="#2F3E46",activerelief=RAISED,highlightbackground="#52796F",highlightcolor="#52796F",highlightthickness=3)
    scle.pack(side=RIGHT,fill=Y)
    list=Listbox(frami,bd=3,yscrollcommand=scle.set,bg="#2F3E46",fg="#84A98C",relief=SUNKEN,highlightbackground="#52796F",highlightcolor="#52796F",highlightthickness=3)
    for i in ele:
        list.insert(END,i)
    list['font']=myFont
    list.pack(side=LEFT,fill=BOTH,expand=True)
    scle.config(command=list.yview)
    butt1 = Button(top,pady=15,justify=CENTER, text='QUIT',padx=50,command=top.destroy,fg="#84A98C",bg='#354F52',activeforeground="#2F3E46",activebackground="#84A98C",bd=3,highlightbackground="#52796F") 
    butt1['font']=myFont
    butt1.pack(side=TOP,pady=15)


def computeLPSArrayMC(pat, M, lps):
	len = 0 

	lps[0]
	i = 1

	while i < M:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			if len != 0:
				len = lps[len-1]
			else:
				lps[i] = 0
				i += 1

def Rabin_Karp():
    ele=[]
    top=Toplevel()
    top.title("Rabin_Karp")
    top.configure(bg="#52796F",bd=5,relief=RAISED,highlightbackground="#52796F",highlightcolor="#52796F",highlightthickness=3)
    top.geometry('1200x600')
    frami = Frame(top,bg='#354F52',padx=10,pady=15, borderwidth=3,relief="sunken")
    frami.pack(side=TOP,fill=BOTH,expand=True)
    findtext=input1.get()
    files=["Research#1.txt","Research#2.txt","Research#3.txt","Research#4.txt","Research#5.txt","Research#6.txt","Research#7.txt","Research#8.txt","Research#9.txt","Research#10.txt"]

    q=101   #prime number
    d=256   #for hashing
    M = len(findtext)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1
    if findtext != "" :#and Wword.get()==0:
        for file in files:

            fp=open(file,'r')
            lines=fp.readlines()
            lineno=1
            for line in lines:
                #print(line)
                i = 0
                j = 0
                p = 0    # hash value for pattern
                t = 0    # hash value for txt
                h = 1
                N = len(line)
                for i in range(M-1):
                    h = (h*d) % q
                if M_C.get()==0 and N>=M:
                    #print(line)
                    for i in range(M):
                        p = (d*p + ord(findtext[i].upper())) % q
                        t = (d*t + ord(line[i].upper())) % q
                    for i in range(N-M+1):
                        if p == t:
                            for j in range(M):
                                if line[i+j].upper() != findtext[j].upper():
                                    break
                                else:
                                    j += 1
                            if (Wword.get()==0):
                                if (j == M):
                                    ele1="Pattern found at index:"+str (i+1)+" line:"+str(lineno)+" file:"+str(file)
                                    ele.append(ele1)
                            elif(Wword.get()==1):
                                for word in line.split():
                                    if (j == M and word.upper()==findtext.upper()):
                                        ele1="Word:"+str(word) +" found at index:"+str (i+1)+" line:"+str(lineno)+" file:"+str(file)
                                        ele.append(ele1)
                        if i < N-M:
                            t = (d*(t-ord(line[i].upper())*h) + ord(line[i+M].upper())) % q
                            if t < 0:
                                t = t+q
                if M_C.get()==1 and N>=M:
                    for i in range(M):
                        p = (d*p + ord(findtext[i])) % q
                        t = (d*t + ord(line[i])) % q

                    for i in range(N-M+1):

                        if p == t:

                            for j in range(M):
                                if line[i+j] != findtext[j]:
                                    break
                                else:
                                    j += 1

                            if (Wword.get()==0):
                                if (j == M):
                                    ele1="Pattern found at index:"+str (i+1)+" line:"+str(lineno)+" file:"+str(file)
                                    ele.append(ele1)
                            elif(Wword.get()==1):
                                for word in line.split():
                                    if (j == M and word==findtext):
                                        ele1="Word:"+str(word) +" found at index:"+str (i+1)+" line:"+str(lineno)+" file:"+str(file)
                                        ele.append(ele1)
                        if i < N-M:
                            t = (d*(t-ord(line[i])*h) + ord(line[i+M])) % q
                            if t < 0:
                                t = t+q
                lineno+=1         
    
    
    mylabel=Label(frami,text='The Word "'+str(input1.get())+'" Found using RK Method',bg='#354F52',fg="#84A98C",pady=10)
    mylabel['font']=myFont
    mylabel.pack(side=TOP)
    scle=Scrollbar(frami,bd=2,troughcolor='#354F52',bg="#84A98C",activebackground="#2F3E46",activerelief=RAISED,highlightbackground="#52796F",highlightcolor="#52796F",highlightthickness=3)
    scle.pack(side=RIGHT,fill=Y)
    list=Listbox(frami,bd=3,yscrollcommand=scle.set,bg="#2F3E46",fg="#84A98C",relief=SUNKEN,highlightbackground="#52796F",highlightcolor="#52796F",highlightthickness=3)
    for i in ele:
        list.insert(END,i)
    list['font']=myFont
    list.pack(side=LEFT,fill=BOTH,expand=True)
    scle.config(command=list.yview)
    butt1 = Button(top,pady=15,justify=CENTER, text='QUIT',padx=50,command=top.destroy,fg="#84A98C",bg='#354F52',activeforeground="#2F3E46",activebackground="#84A98C",bd=3,highlightbackground="#52796F") 
    butt1['font']=myFont
    butt1.pack(side=TOP,pady=15)


def bruteforce():
    ele=[]
    top=Toplevel()
    top.title("Brute_Force")
    top.configure(bg="#52796F",bd=5,relief=RAISED,highlightbackground="#52796F",highlightcolor="#52796F",highlightthickness=3)
    top.geometry('1200x600')
    frami = Frame(top,bg='#354F52',padx=10,pady=15, borderwidth=3,relief="sunken")
    frami.pack(side=TOP,fill=BOTH,expand=True)
   
    findtext=input1.get()
    files=["Research#1.txt","Research#2.txt","Research#3.txt","Research#4.txt","Research#5.txt","Research#6.txt","Research#7.txt","Research#8.txt","Research#9.txt","Research#10.txt"]
    M = len(findtext)
    lineno=1
    if findtext != "" :#and Wword.get()==0:
        for file in files:
            fp=open(file,'r')
            lineno=1
            lines=fp.readlines()
            for line in lines:
            
                
                N = len(line)
                for i in range(N - M + 1):
                    j = 0
                    k=0
                    if(M_C.get()==1):
                        while(j < M):
                            if (line[i + j] != findtext[j]):
                                break
                            j += 1
                        if (Wword.get()==0):
                            if (j == M):
                                ele1="Pattern found at index:"+str (i+1)+" line:"+str(lineno)+" file:"+str(file)
                                ele.append(ele1)
                        elif(Wword.get()==1):
                            for word in line.split():
                                if (j == M and word.upper()==findtext.upper()):
                                    ele1="Word:"+str(word) +" found at index:"+str (i+1)+" line:"+str(lineno)+" file:"+str(file)
                                    ele.append(ele1)
                    if(M_C.get()==0):
                        while(k < M):
                            if (line[i + k].upper() != findtext[k].upper()):
                                break
                            k += 1
                        if (Wword.get()==0):
                            if (k == M):
                                ele1="Pattern found at index:"+str (i+1)+" line:"+str(lineno)+" file:"+str(file)
                                ele.append(ele1)
                        elif(Wword.get()==1):
                            for word in line.split():
                                if (k == M and word.upper()==findtext.upper()):
                                    ele1="Word:"+str(word) +" found at index:"+str (i+1)+" line:"+str(lineno)+" file:"+str(file)
                                    ele.append(ele1)

                lineno+=1
        #print(line[1])
    mylabel=Label(frami,text='The Word "'+str(input1.get())+'" Found using Brute Force',bg='#354F52',fg="#84A98C",pady=10)
    mylabel['font']=myFont
    mylabel.pack(side=TOP)
    scle=Scrollbar(frami,bd=2,troughcolor='#354F52',bg="#84A98C",activebackground="#2F3E46",activerelief=RAISED,highlightbackground="#52796F",highlightcolor="#52796F",highlightthickness=3)
    scle.pack(side=RIGHT,fill=Y)
    list=Listbox(frami,bd=3,yscrollcommand=scle.set,bg="#2F3E46",fg="#84A98C",relief=SUNKEN,highlightbackground="#52796F",highlightcolor="#52796F",highlightthickness=3)
    for i in ele:
        list.insert(END,i)
    list['font']=myFont
    list.pack(side=LEFT,fill=BOTH,expand=True)
    scle.config(command=list.yview)
    butt1 = Button(top,pady=15,justify=CENTER, text='QUIT',padx=50,command=top.destroy,fg="#84A98C",bg='#354F52',activeforeground="#2F3E46",activebackground="#84A98C",bd=3,highlightbackground="#52796F") 
    butt1['font']=myFont
    butt1.pack(side=TOP,pady=15)
    #top.mainloop()


def myclick():
    if(clicked.get()=="Brute Force"):
     bruteforce()
    if(clicked.get()=="RK Method  "):
     Rabin_Karp()
    if(clicked.get()=="KMP Method "):
     KMPSearch()
    #if()
    #Label(top,text=input1.get()).pack()



root = Tk()
root.configure(bg="#52796F",bd=5)
myFont = font.Font(family='Times', size=15, weight='bold')
myFont1 = font.Font(family='Times New Roman', size=10, weight='bold')
root.title("Algorithm Assignment 4")
#root.geometry('1200x600')

fram = Frame(root,bg='#354F52',padx=10,pady=15,highlightbackground="red", borderwidth=3,relief="sunken")
fram.pack(side=TOP)



clicked=StringVar()
clicked.set("Algorithm:-")


drop = OptionMenu(fram,clicked,"Brute Force","RK Method  ","KMP Method ")
drop.configure(bg="#84A98C",fg="#2F3E46",activebackground="#2F3E46",activeforeground="#84A98C",highlightbackground="#52796F")
drop['font']=myFont
drop.pack(side=LEFT,padx=[4,10])

mylab=Label(fram,text='Enter The Text to Find In the Files:',bg='#354F52',fg="#84A98C")
mylab['font']=myFont
mylab.pack(side=LEFT)



input1 = Entry(fram,width=30,bd=3,relief=FLAT)
input1['font']=myFont

input1.pack(side=LEFT,fill=BOTH,padx=[5,10])

input1.focus_set()
#print(clicked)
fram1 = Frame(root,bg="#3F5C5F",bd=3,padx=358,pady=15,relief="ridge")

Wword=IntVar()
M_C=IntVar()
ChkB1=Checkbutton(fram1,text="Match Whole Word Only",variable=Wword,bd=4,relief="ridge",bg="#2F3E46",fg="#84A98C",highlightbackground="#29393B",highlightcolor="red",activeforeground="#2F3E46",activebackground="#84A98C")
ChkB1['font']=myFont1
ChkB1.pack(side=LEFT,padx=20)
ChkB2=Checkbutton(fram1,text="Match Case",variable=M_C,bd=4,relief="ridge",bg="#2F3E46",fg="#84A98C",highlightbackground="#29393B",highlightcolor="#84A98C",activeforeground="#2F3E46",activebackground="#84A98C")
ChkB2['font']=myFont1
ChkB2.pack()
butt = Button(fram, text='Find',padx=50,command=myclick,fg="#84A98C",bg="#2F3E46",activeforeground="#2F3E46",activebackground="#84A98C",bd=3,highlightbackground="#52796F") 
butt['font']=myFont
butt.pack(side=RIGHT)
fram1.pack()

 
root.mainloop()

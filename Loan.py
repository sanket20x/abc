from tkinter import*

class customer:
    def __init__(self,root):
        self.root=root
        self.root.title('Loan Management system')
        self.root.geometry('1350x720+0+0')
        title=Label(self.root,text='Loan Management System',font=('times new rommon',40,'bold'),bg='black',fg='grey')
        title.pack(side=TOP,fill=X)
        
        Detail_F=Frame(self.root,bd=4,relief=RIDGE,bg='powderblue')
        Detail_F.place(x=11,y=110,width=510,height=610)
        lbl_id=Label(Detail_F,text='Loan Id',font=('times new rommon',18,'bold'))
        lbl_id.grid(row=0,column=0,padx=20,pady=10)
        txt_id=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief='flat' )
        txt_id.grid(row=0,column=1)
        
       
      
        

obj=customer(root)
root.mainloop()
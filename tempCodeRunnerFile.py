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
        
        lbl_name=Label(Detail_F,text='Full Name',font=('times new rommon',18,'bold'))
        lbl_name.grid(row=1,column=0,padx=20,pady=10)
        txt_name=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief='flat' )
        txt_name.grid(row=1,column=1)
        
        lbl_mob=Label(Detail_F,text='Mobile no.',font=('times new rommon',18,'bold'))
        lbl_mob.grid(row=2,column=0,padx=20,pady=10)
        txt_mob=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief='flat' )
        txt_mob.grid(row=2,column=1)
        
        lbl_ad=Label(Detail_F,text='Aadhar No',font=('times new rommon',18,'bold'))
        lbl_ad.grid(row=3,column=0,padx=20,pady=10)
        txt_ad=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief='flat' )
        txt_ad.grid(row=3,column=1)
        
        lbl_add=Label(Detail_F,text='Address',font=('times new rommon',18,'bold'))
        lbl_add.grid(row=4,column=0,padx=20,pady=10)
        txt_add=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief='flat' )
        txt_add.grid(row=4,column=1)
        
        lbl_add=Label(Detail_F,text='Pincode',font=('times new rommon',18,'bold'))
        lbl_add.grid(row=5,column=0,padx=20,pady=10)
        txt_add=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief='flat' )
        txt_add.grid(row=5,column=1)
        
        lbl_add=Label(Detail_F,text='Amount of loan',font=('times new rommon',18,'bold'))
        lbl_add.grid(row=6,column=0,padx=20,pady=10)
        txt_add=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief='flat' )
        txt_add.grid(row=6,column=1)
        
        lbl_add=Label(Detail_F,text='Number of years',font=('times new rommon',18,'bold'))
        lbl_add.grid(row=7,column=0,padx=20,pady=10)
        txt_add=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief='flat' )
        txt_add.grid(row=7,column=1)
        
        lbl_add=Label(Detail_F,text='Interest rate',font=('times new rommon',18,'bold'))
        lbl_add.grid(row=8,column=0,padx=20,pady=10)
        txt_add=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief='flat' )
        txt_add.grid(row=8,column=1)
        
        lbl_add=Label(Detail_F,text='Monthly update',font=('times new rommon',18,'bold'))
        lbl_add.grid(row=9,column=0,padx=20,pady=10)
        txt_add=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief='flat' )
        txt_add.grid(row=9,column=1)
        
        lbl_add=Label(Detail_F,text='Total Payment',font=('times new rommon',18,'bold'))
        lbl_add.grid(row=10,column=0,padx=20,pady=10)
        txt_add=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief='flat' )
        txt_add.grid(row=10,column=1)
        
        RFrame=Frame(self.root,bd=4,relief=RIDGE,bg='powderblue')
        
      
        
root=Tk()
obj=customer(root)
root.mainloop()
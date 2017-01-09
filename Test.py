__author__ = 'fissalalsharef'

from xlrd import *
from Tkinter import*
from searchengine import *



DataBase = {}

class Searchengine():
    def __init__(self):
        self.Interface()


    def Convert_The_Data_into_Dict(self):
        inpu = ['Dataset.xlsx']
        for name in inpu:
            book = open_workbook(name)
            for i in book.sheets():
                for row in range(1,i.nrows):
                    data = []
                    for col in range(i.ncols):
                        s = str((i.cell(row,col).value))
                        data.append(s)
                    a = '|'.join(data)
                    (name,rating,camera,price) = a.split('|')
                    DataBase.setdefault(name,{})
                    DataBase[name].setdefault(price,{})
                    DataBase[name][price].setdefault(camera,{})
                    DataBase[name][price][camera] = float(rating)

        return DataBase


    def wordIndex(self):
        List = []
        Dic = self.Convert_The_Data_into_Dict()
        for key in Dic:
            List.append(key.split())

        return List


    def normalize_For_Ranking(self):
        Dic = self.Convert_The_Data_into_Dict()
        Dic_for_norm = {}
        sum = 0
        for Name in Dic:
            Dic_for_norm.setdefault(Name,1)
            # print Dic[Name].keys()
            for price in Dic[Name]:
                for camera in Dic[Name][price]:
                    sum = sum + ((float(Dic[Name].keys()[0]))/(float(Dic[Name].keys()[0])/Dic[Name][price][camera]))
                Dic_for_norm[Name] = 0.15+0.85*sum

        c = searcher('')
        norm = c.normalizescores(Dic_for_norm)
        return norm


    def search(self):
        Dic = self.Convert_The_Data_into_Dict()
        global a
        a = []
        global final_output
        wordindex = self.wordIndex()
        normalization = self.normalize_For_Ranking()
        word_input = self.getwords.get()
        # word_input = 'samsung galaxy'
        list_of_input_words = []
        list_of_wordlocation = []
        list_of_final_result = []
        list_of_final_result1 = []
        final_output = []
        words = word_input.lower().split(' ')

        for word in words:
            list_of_input_words.append(word)

        for list in wordindex:
            for word in list:
                word = word.lower()
                if word in list_of_input_words:
                    joining = " ".join(str(w) for w in list)
                    list_of_wordlocation.append(joining)

        convert_to_tuple = [(v, k) for k, v in normalization.items()]
        sort_The_tuble = sorted(convert_to_tuple,reverse=True)

        if self.Radio_Values3.get() == 0:
            self.All_Result_Of_Mobiles.delete(0,END)
            for name in Dic:
                if name in list_of_wordlocation:
                    for price in Dic[name]:
                        if self.No1.get() <= float(price) <= self.No2.get():
                            list_of_final_result.append(name)

            self.All_Result_Of_Mobiles.delete(0,END)
            count = 1
            for indx in sort_The_tuble:
                if indx[1] in list_of_final_result:
                    final_output.append(indx)

                    output = "%d:   %s          %s\n" %(count, indx[0],indx[1])
                    self.All_Result_Of_Mobiles.insert(END,output)
                    count += 1

        if self.Radio_Values3.get() == 1:
            self.All_Result_Of_Mobiles.delete(0,END)
            for name in Dic:
                if name in list_of_wordlocation:
                    for price in Dic[name]:
                        for camera in Dic[name][price]:
                            if self.No3.get() <= float(Dic[name][price][camera]) <= self.No4.get() :
                                list_of_final_result1.append(name)

            count = 1
            for indx in sort_The_tuble:
                if indx[1] in list_of_final_result1:
                    final_output.append(indx)
                    output = "%d:   %s          %s\n" %(count, indx[0],indx[1])
                    self.All_Result_Of_Mobiles.insert(END,output)
                    count += 1


    def add_baket(self):
        try:
            Dic = self.Convert_The_Data_into_Dict()
            v = self.All_Result_Of_Mobiles.curselection()
            for i in range(len(v)):
                a.append(final_output[v[i]])
            self.Amount_of_Items_inthe_basket.delete(0.0,END)
            self.Amount_of_Items_inthe_basket.insert(END,len(a))
            price = 0.0
            for i in a:
                name = i[1]
                if name in Dic:
                    price += float(Dic[name].keys()[0])

            self.amount_of_money.delete(0,END)
            output = "%s  $" %(price)
            self.amount_of_money.insert(END,output)
        except:
            pass


    def Error_Message(self):
        error_Window = Toplevel()
        error_Massage = Label(error_Window,text = """Please Insert at least\n a word to search""",font="Times 40 bold",fg = "red", bg = "black")
        error_Massage.pack()



    def show_basket(self):
        try:
            if len(a) == 0:
                self.Error_Message()

            show_markets = Toplevel()
            show_markets.geometry('450x350')
            canvas2 = Listbox(show_markets, bg="light blue", fg="black")
            canvas2.pack(side = 'top',fill='both',expand='yes')
            count = 1
            for i in a:
                output = "%d:   %s          %s\n" %(count, i[0],i[1])
                canvas2.insert(END,output)
                count += 1
        except:
            pass

    def show_basket1(self):
        try:
            if len(a) == 0:
                self.Error_Message()

            show_markets = Toplevel()
            show_markets.geometry('450x350')
            canvas2 = Listbox(show_markets, bg="light blue", fg="black")
            canvas2.pack(side = 'top',fill='both',expand='yes')
            labeling = Label(show_markets, text="Please enter you id card",bg="yellow",fg="black", width=30)
            labeling.place(relx=0.3,rely=0.3)

            entry = Text(show_markets, width=20,height=1, font=("Times 15", 15), bg='white')
            entry.place(relx=0.3, rely=0.38)

            checkout = Button(show_markets,text="Checkout",bg="yellow", width=20,height=1,command=self.welcoming)
            checkout.place(relx=0.64,rely=0.87)

            QuitButton = Button(show_markets, text="Quit",bg="red",fg="black",command=self.root.quit)
            QuitButton.place(relx=0.01,rely=0.01)

        except:
            pass


    def welcoming(self):
        show_markets = Toplevel()
        Wlcome_Message = Label(show_markets,text = """Thank you for your time\nIt's done!""",font="Times 40 bold",fg = "red", bg = "black")
        Wlcome_Message.pack()

    def Interface(self):

        self.root = Tk()
        self.root.geometry("750x750")
        self.root.resizable(width=False,height=False)

        self.getwords = StringVar()
        self.No1 = IntVar()
        self.No2 = IntVar()
        self.No3 = IntVar()
        self.No4 = IntVar()
        self.Radio_Values3 = IntVar()

        #Background part
        self.Background = Label(self.root,bg="black")
        self.Background.place(relx = 0.0,rely = 0.0,width = 1000,height = 1000)

        self.Title = Label(self.root,text = 'Search Engine Application',font = "Times 30 bold")
        self.Title.place(relx = 0.20,rely = 0.001)

        self.entry = Entry(self.root, width = 50, font = ("Times 7",20), textvariable=self.getwords)
        self.entry.place(relx = 0.01, rely = 0.1)

        self.Combobox = Label(self.root,text = """Choose the\n   price of\n mobiles:""",bg = "Light Blue",font = "Times 10 bold")
        self.Combobox.place(relx = 0.01,rely=0.18,width=75,height = 50)

        self.Price_Of_Mobiles = Label(self.root,text = "Price:",font = "Times 10 bold", bg = "Light Blue")
        self.Price_Of_Mobiles.place(relx = 0.12, rely= 0.2)
        self.Valueof_Mobiles_price = Entry(self.root, textvariable= self.No1)
        self.Valueof_Mobiles_price.place(relx = 0.18,rely = 0.2,width = 25, height = 25)
        self.dash = Label(self.root, text="--",bg='black',fg='white')
        self.dash.place(relx=0.22,rely=0.2)
        self.Valueof_Mobiles_price1 = Entry(self.root, textvariable= self.No2)
        self.Valueof_Mobiles_price1.place(relx = 0.25,rely = 0.2,width = 25, height = 25)

        self.Combobox = Label(self.root,text = """Choose the\n  Rating of\n mobiles:""",bg = "Light Blue",font = "Times 10 bold")
        self.Combobox.place(relx = 0.01,rely=0.26,width=75,height = 50)

        self.Rating_Of_Mobiles = Label(self.root,text = "Rating-/5:",font = "Times 10 bold", bg = "Light Blue")
        self.Rating_Of_Mobiles.place(relx = 0.12, rely= 0.28)
        self.Valueof_Mobile_Rating = Entry(self.root, textvariable= self.No3)
        self.Valueof_Mobile_Rating.place(relx = 0.21,rely = 0.28,width = 25, height = 25)
        self.dash1 = Label(self.root, text="--",bg='black',fg='white')
        self.dash1.place(relx=0.25,rely=0.28)
        self.Valueof_Mobile_Rating1 = Entry(self.root, textvariable= self.No4)
        self.Valueof_Mobile_Rating1.place(relx = 0.28,rely = 0.28,width = 25, height = 25)

        self.button_for_searching = Button(self.root, text = 'Search',height = 1,font=("Times 15", 15), bg='blue', command=self.search)
        self.button_for_searching.place(relx = 0.86, rely = 0.20)

        self.All_Result_Of_Mobiles = Listbox(self.root,selectmode=EXTENDED,font = ("Times 7",10))
        self.All_Result_Of_Mobiles.place(relx = 0.01 ,rely = 0.43,height = 190,width=700)

        self.button_for_adding_to_thebasket = Button(self.root, text = 'Add To Basket',command = self.add_baket,height = 1,font=("Times 15", 15), bg='blue')
        self.button_for_adding_to_thebasket.place(relx = 0.71, rely = 0.62)

        self.button_for_viewing_thebasket = Button(self.root, text= 'View Basket',command = self.show_basket, height = 1,font=("Times 15", 15), bg='blue')
        self.button_for_viewing_thebasket.place(relx=0.02,rely=0.7)

        self.Quantity_of_items = Label(self.root, text="Quantity", height=1, font=("Times 15", 15), bg='light blue')
        self.Quantity_of_items.place(relx = 0.87,rely = 0.001)

        self.Amount_of_Items_inthe_basket = Text(self.root, height=1,width=3)
        self.Amount_of_Items_inthe_basket.place(relx=0.9,rely=0.045)

        self.Background_of_CheckList = Label(self.root,bg = "light yellow")
        self.Background_of_CheckList.place(relx =0.7 ,rely = 0.7,width = 200,height=180)

        self.Button_For_chackout = Button(self.root, text="Proceed to checkout",bg="yellow", width=20,height=1, command=self.show_basket1)
        self.Button_For_chackout.place(relx=0.74,rely=0.87)

        self.label_for_Total_price = Label(self.root, text="Subtotal: ",fg="white",bg="black", width=12)
        self.label_for_Total_price.place(relx=0.71,rely=0.72)

        self.amount_of_money = Entry(self.root, bg= "light blue")
        self.amount_of_money.place(relx = 0.84,rely = 0.72,width = 60, height = 22)

        self.Types_of_classifying = Radiobutton(self.root,variable = self.Radio_Values3,value = 0)
        self.Types_of_classifying.place(relx = 0.4,rely = 0.2,width = 25, height = 25)

        self.Types_of_classifying1 = Radiobutton(self.root,variable = self.Radio_Values3,value = 1)
        self.Types_of_classifying1.place(relx = 0.4,rely = 0.28,width = 25, height = 25)

        mainloop()



Application = Searchengine()






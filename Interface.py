from Tkinter import*
import ttk
from PIL import ImageTk,Image


class MasterCard:

    def __init__(self,root):
        self.name = StringVar()

        root.title('MozzA v1.0')
        root.geometry('815x480+250+100')
        photo = ImageTk.PhotoImage(file = 'front.ppm')
        canvas = Canvas(root)
        canvas.pack(side = 'top',fill='both',expand = 'yes')
        canvas.create_image(423,250,image = photo)
        canvas.image = photo
        button_SignInFront = Button(root, text = 'Sign In',command = self.SignIn,anchor = N,height = 1,width = 30)
        button_SignInFront_windows = canvas.create_window(300,200,anchor = NW,window = button_SignInFront)
        button_SignUpFront = Button(root, text = 'Sign Up',command = self.SignUp,anchor = N,height = 1,width = 30)
        button_SignUpFront_windows = canvas.create_window(300,240,anchor = NW,window = button_SignUpFront)

    def SignIn(self):
        signIn = Toplevel()
        signIn.title('Sign In')
        signIn.geometry('815x480')
        photo2 = ImageTk.PhotoImage(file = 'signin.ppm')
        canvas2 = Canvas(signIn)
        canvas2.pack(side = 'top',fill='both',expand='yes')
        canvas2.create_image(423,250,image = photo2)
        canvas2.image = photo2
        label1 = Label(signIn,bg = 'white',text = 'Please Enter Your Username')
        label1_windows = canvas2.create_window(300,160,anchor = NW,window = label1)
        entery1 = Entry(signIn,textvariable = self.name,width = 40)
        entery1_windows = canvas2.create_window(300,200,anchor = NW, window = entery1)



    def SignUp(self):
        signup = Toplevel()
        signup.title('Sign Up')
        signup.geometry('815x480')
        photo3 = ImageTk.PhotoImage(file = 'signup.ppm')
        canvas3 = Canvas(signup)
        canvas3.pack(side = 'top',fill = 'both',expand = 'yes')
        canvas3.create_image(423,250,image = photo3)
        canvas3.image = photo3


root = Tk()
MasterCard(root)
root.mainloop()
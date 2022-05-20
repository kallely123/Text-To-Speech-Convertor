# from gtts import gTTS
# import os
# text=" ഒരിടത്തൊരിടത്ത്"
# output=gTTS(text=text,lang='ml',slow="true")
# output.save("output.mp3")
# os.system("start output.mp3")
#
# from gtts import gTTS
# import os
# text=open('demo.txt','r',encoding='utf-8')
# t=text.read()
# output=gTTS(text=t,lang='ml',slow=False)
# output.save('output.mp3')
# os.system('start output.mp3')

from tkinter import *
from gtts import gTTS
import os
root=Tk()
def audio1():
    text=display.get()
    output=gTTS(text=text,lang='en',slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')
label=Label(root,text="Enter text here in english:",fg="blue")
label.grid(row=0,column=0)
display=Entry(root,bg="pink",fg="blue")
display.grid(row=1,columnspan=15)
button=Button(root,text="Click here to convert audio",bg="ivory",fg="green",command=audio1)
button.grid(row=2,column=0)

root.mainloop()

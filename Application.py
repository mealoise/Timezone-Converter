from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.ampm = 0
        self.create_widget1()
        self.create_widget2()

    def create_widget1(self):
        self.bttn = Button(self)
        self.bttn["text"] = "Good Morning"
        self.bttn["command"] = self.update_count
        self.bttn.grid(row=2, column=2)

    def create_widget2(self):
        self.bttn2 = Button(self)
        self.bttn2["text"] = "Nighty Nite"
        self.bttn2["command"] = self.update_count
        self.bttn2.grid(row=2, column=6)

    def update_count(self):
        self.bttn_clicks += 1
        if self.bttn_clicks > 0:
            self.bttn["highlightbackground"] = "green"
            self.bttn.configure(bg="green")
        if self.ampm % 2 == 0:
            if self.bttn_clicks < 12:
                self.bttn["text"] = str(self.bttn_clicks) + ":00" + " PM"
            elif self.bttn_clicks == 12:
                self.bttn["text"] = str(self.bttn_clicks) + ":00" + " AM"
                self.bttn_clicks += 1
                self.ampm += 1
            elif self.bttn_clicks == 13:
                self.bttn_clicks = 0
        if self.ampm % 2 == 1:
            if self.bttn_clicks < 12:
                self.bttn["text"] = str(self.bttn_clicks) + ":00" + " AM"
            elif self.bttn_clicks == 12:
                self.bttn["text"] = str(self.bttn_clicks) + ":00" + " PM"
                self.ampm += 1
                self.bttn_clicks += 1
            elif self.bttn_clicks == 13:
                self.bttn_clicks = 0

    def update_count2(self):
        self.bttn_clicks += 1
        if self.bttn_clicks > 0:
            self.bttn2["highlightbackground"] = "green"
            self.bttn2.configure(bg="green")
        if self.ampm % 2 == 0:
            if self.bttn_clicks < 12:
                self.bttn2["text"] = str(self.bttn_clicks) + ":00" + " PM"
            elif self.bttn_clicks == 12:
                self.bttn2["text"] = str(self.bttn_clicks) + ":00" + " AM"
                self.bttn_clicks += 1
                self.ampm += 1
            elif self.bttn_clicks == 13:
                self.bttn_clicks = 0
        if self.ampm % 2 == 1:
            if self.bttn_clicks < 12:
                self.bttn2["text"] = str(self.bttn_clicks) + ":00" + " AM"
            elif self.bttn_clicks == 12:
                self.bttn2["text"] = str(self.bttn_clicks) + ":00" + " PM"
                self.ampm += 1
                self.bttn_clicks += 1
            elif self.bttn_clicks == 13:
                self.bttn_clicks = 0

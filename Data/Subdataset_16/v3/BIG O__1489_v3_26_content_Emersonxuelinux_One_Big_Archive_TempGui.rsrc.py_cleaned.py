import wx
class class1(wx.App):
    def fonk1(self):
        b1 = class2(None, b2="Temperature Converter")
        self.SetTopWindow(b1)
        b1.Show(True)
        return True
class class2(wx.Frame):
    def fonk2(self, parent, b2):
        super().fonk2(parent, b2 = b2, size=(450, 300), style=wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER)
        self.CreateStatusBar()
        self.fonk3()
        self.fonk4()
    def fonk3(self):
        b3 = wx.Menu()
        b4 = b3.Append(wx.ID_EXIT, "E&xit", "Terminate the program")
        b5 = wx.Menu()
        b6 = b5.Append(wx.ID_ANY, "&Celsius to Fahrenheit")
        b7 = b5.Append(wx.ID_ANY, "&Fahrenheit to Celsius")
        b8 = wx.MenuBar()
        b8.Append(b3, "&File")
        b8.Append(b5, "&Convert")
        self.SetMenuBar(b8)
        self.Bind(wx.EVT_MENU, self.OnExit, b4)
        self.Bind(wx.EVT_MENU, self.OnConvertCtoF, b6)
        self.Bind(wx.EVT_MENU, self.OnConvertFtoC, b7)
    def fonk4(self):
        b9 = wx.Panel(self)
        b10 = wx.BoxSizer(wx.VERTICAL)
        self.b11 = wx.TextCtrl(b9, size=(74, -1))
        self.b12 = wx.SpinCtrl(b9, value='0', min=-1000, max=1000)
        b13 = wx.Button(b9, label="Celsius to Fahrenheit >>>")
        b14 = wx.Button(b9, label="<<< Fahrenheit to Celsius")
        b15 = wx.StaticText(b9, label="Celsius")
        b16 = wx.StaticText(b9, label="Fahrenheit")
        b13.Bind(wx.EVT_BUTTON, self.OnConvertCtoF)
        b14.Bind(wx.EVT_BUTTON, self.OnConvertFtoC)
        b10.Add(b15, 0, wx.ALL, 5)
        b10.Add(self.b11, 0, wx.ALL, 5)
        b10.Add(b13, 0, wx.ALL, 5)
        b10.Add(b14, 0, wx.ALL, 5)
        b10.Add(self.b12, 0, wx.ALL, 5)
        b10.Add(b16, 0, wx.ALL, 5)
        b9.SetSizerAndFit(b10)
    def fonk5(self, event):
        self.Close(True)
    def fonk6(self, event):
        try:
            b17 = float(self.b11.GetValue())
            b18 = (b17 * 9/5) + 32
            self.b12.SetValue(int(b18))
        except ValueError:
            wx.MessageBox("Please enter a valid number", "Error", wx.OK | wx.ICON_ERROR)
    def fonk7(self, event):
        try:
            b18 = self.b12.GetValue()
            b17 = (b18 - 32) * 5/9
            self.b11.SetValue(f"{b17:.2f}")
        except ValueError:
            wx.MessageBox("Please enter a valid number", "Error", wx.OK | wx.ICON_ERROR)
if b19 = = "__main__":
    b20 = class1(False)
    b20.MainLoop()
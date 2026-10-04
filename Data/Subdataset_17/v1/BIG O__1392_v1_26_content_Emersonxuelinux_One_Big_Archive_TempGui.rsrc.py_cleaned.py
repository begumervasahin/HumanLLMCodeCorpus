import wx
class TemplateApp(wx.App):
    def OnInit(self):
        frame = TemplateFrame(None, title="Standard Template with File->Exit menu")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
class TemplateFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(450, 300), style=wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER)
        self.CreateStatusBar()
        filemenu = wx.Menu()
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")
        convertmenu = wx.Menu()
        menuConvertCtoF = convertmenu.Append(wx.ID_ANY, "&Celsius to Fahrenheit")
        menuConvertFtoC = convertmenu.Append(wx.ID_ANY, "&Fahrenheit to Celsius")
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        menuBar.Append(convertmenu, "&Convert")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnConvertCtoF, menuConvertCtoF)
        self.Bind(wx.EVT_MENU, self.OnConvertFtoC, menuConvertFtoC)
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.tfCel = wx.TextCtrl(panel, pos=(14, 76), size=(74, -1))
        self.spinFahr = wx.SpinCtrl(panel, value='0', pos=(292, 78), min=0, max=100)
        btnCtoF = wx.Button(panel, label="Celcius to Fahrenheit >>>", pos=(107, 70))
        btnFtoC = wx.Button(panel, label="<<< Fahrenheit to Celcius", pos=(107, 104))
        staticText1 = wx.StaticText(panel, label="Celsius", pos=(31, 105))
        staticText2 = wx.StaticText(panel, label="Fahrenheit", pos=(284, 105))
        btnCtoF.Bind(wx.EVT_BUTTON, self.OnConvertCtoF)
        btnFtoC.Bind(wx.EVT_BUTTON, self.OnConvertFtoC)
        sizer.Add(self.tfCel, 0, wx.ALL, 5)
        sizer.Add(self.spinFahr, 0, wx.ALL, 5)
        sizer.Add(btnCtoF, 0, wx.ALL, 5)
        sizer.Add(btnFtoC, 0, wx.ALL, 5)
        panel.SetSizerAndFit(sizer)
        self.Show(True)
    def OnExit(self, event):
        self.Close(True)
    def OnConvertCtoF(self, event):
        try:
            celsius = float(self.tfCel.GetValue())
            fahrenheit = (celsius * 9/5) + 32
            self.spinFahr.SetValue(fahrenheit)
        except ValueError:
            wx.MessageBox("Please enter a valid number", "Error", wx.OK | wx.ICON_ERROR)
    def OnConvertFtoC(self, event):
        try:
            fahrenheit = self.spinFahr.GetValue()
            celsius = (fahrenheit - 32) * 5/9
            self.tfCel.SetValue(str(round(celsius, 2)))
        except ValueError:
            wx.MessageBox("Please enter a valid number", "Error", wx.OK | wx.ICON_ERROR)
if __name__ == "__main__":
    app = TemplateApp(False)
    app.MainLoop()
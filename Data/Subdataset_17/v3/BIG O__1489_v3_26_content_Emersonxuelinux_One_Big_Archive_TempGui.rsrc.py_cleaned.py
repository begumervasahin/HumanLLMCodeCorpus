import wx
class TemperatureConverterApp(wx.App):
    def OnInit(self):
        frame = TemperatureConverterFrame(None, title="Temperature Converter")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
class TemperatureConverterFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(450, 300), style=wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER)
        self.CreateStatusBar()
        self.createMenuBar()
        self.createUI()
    def createMenuBar(self):
        fileMenu = wx.Menu()
        menuExit = fileMenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")
        convertMenu = wx.Menu()
        menuConvertCtoF = convertMenu.Append(wx.ID_ANY, "&Celsius to Fahrenheit")
        menuConvertFtoC = convertMenu.Append(wx.ID_ANY, "&Fahrenheit to Celsius")
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(convertMenu, "&Convert")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnConvertCtoF, menuConvertCtoF)
        self.Bind(wx.EVT_MENU, self.OnConvertFtoC, menuConvertFtoC)
    def createUI(self):
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.tfCel = wx.TextCtrl(panel, size=(74, -1))
        self.spinFahr = wx.SpinCtrl(panel, value='0', min=-1000, max=1000)
        btnCtoF = wx.Button(panel, label="Celsius to Fahrenheit >>>")
        btnFtoC = wx.Button(panel, label="<<< Fahrenheit to Celsius")
        staticText1 = wx.StaticText(panel, label="Celsius")
        staticText2 = wx.StaticText(panel, label="Fahrenheit")
        btnCtoF.Bind(wx.EVT_BUTTON, self.OnConvertCtoF)
        btnFtoC.Bind(wx.EVT_BUTTON, self.OnConvertFtoC)
        sizer.Add(staticText1, 0, wx.ALL, 5)
        sizer.Add(self.tfCel, 0, wx.ALL, 5)
        sizer.Add(btnCtoF, 0, wx.ALL, 5)
        sizer.Add(btnFtoC, 0, wx.ALL, 5)
        sizer.Add(self.spinFahr, 0, wx.ALL, 5)
        sizer.Add(staticText2, 0, wx.ALL, 5)
        panel.SetSizerAndFit(sizer)
    def OnExit(self, event):
        self.Close(True)
    def OnConvertCtoF(self, event):
        try:
            celsius = float(self.tfCel.GetValue())
            fahrenheit = (celsius * 9/5) + 32
            self.spinFahr.SetValue(int(fahrenheit))
        except ValueError:
            wx.MessageBox("Please enter a valid number", "Error", wx.OK | wx.ICON_ERROR)
    def OnConvertFtoC(self, event):
        try:
            fahrenheit = self.spinFahr.GetValue()
            celsius = (fahrenheit - 32) * 5/9
            self.tfCel.SetValue(f"{celsius:.2f}")
        except ValueError:
            wx.MessageBox("Please enter a valid number", "Error", wx.OK | wx.ICON_ERROR)
if __name__ == "__main__":
    app = TemperatureConverterApp(False)
    app.MainLoop()
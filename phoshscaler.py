#----------------------------------------------------------------------
# Phosh Scaler
# by Jake Day
# v1.0
# App to set the DPI/Scale for Phosh on Mobile Linux distros
#----------------------------------------------------------------------

import subprocess, wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, pos=(150, 150), size=(300, 420))

        self.CreateStatusBar()

        self.panel = wx.Panel(self)

        self.defaultbtn = wx.Button(self.panel, -1, "Default Dpi (2x Scale)")
        self.defaultbtn.SetBackgroundColour('#ffffff')
        self.defaultbtn.SetForegroundColour('#444444')

        self.lowbtn = wx.Button(self.panel, -1, "Low Dpi (1.75x Scale)")
        self.lowbtn.SetBackgroundColour('#ffffff')
        self.lowbtn.SetForegroundColour('#444444')

        self.mediumbtn = wx.Button(self.panel, -1, "Medium Dpi (1.5x Scale)")
        self.mediumbtn.SetBackgroundColour('#ffffff')
        self.mediumbtn.SetForegroundColour('#444444')

        self.highbtn = wx.Button(self.panel, -1, "High Dpi (1.25x Scale)")
        self.highbtn.SetBackgroundColour('#ffffff')
        self.highbtn.SetForegroundColour('#444444')

        self.ultrahighbtn = wx.Button(self.panel, -1, "Ultra High Dpi (1x Scale)")
        self.ultrahighbtn.SetBackgroundColour('#ffffff')
        self.ultrahighbtn.SetForegroundColour('#444444')

        self.restartbtn = wx.Button(self.panel, -1, "Restart Phosh")
        self.restartbtn.SetBackgroundColour('#ffffff')
        self.restartbtn.SetForegroundColour('#444444')

        self.Bind(wx.EVT_BUTTON, self.OnDefaultDpi, self.defaultbtn)
        self.Bind(wx.EVT_BUTTON, self.OnLowDpi, self.lowbtn)
        self.Bind(wx.EVT_BUTTON, self.OnMediumDpi, self.mediumbtn)
        self.Bind(wx.EVT_BUTTON, self.OnHighDpi, self.highbtn)
        self.Bind(wx.EVT_BUTTON, self.OnUltraHighDpi, self.ultrahighbtn)
        self.Bind(wx.EVT_BUTTON, self.OnRestartPhosh, self.restartbtn)
        
        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.AddSpacer(10)
        sizer.Add(self.defaultbtn, 1, wx.EXPAND|wx.ALIGN_CENTER, 10)
        sizer.AddSpacer(10)
        sizer.Add(self.lowbtn, 1, wx.EXPAND|wx.ALIGN_CENTER, 10)
        sizer.AddSpacer(10)
        sizer.Add(self.mediumbtn, 1, wx.EXPAND|wx.ALIGN_CENTER, 10)
        sizer.AddSpacer(10)
        sizer.Add(self.highbtn, 1, wx.EXPAND|wx.ALIGN_CENTER, 10)
        sizer.AddSpacer(10)
        sizer.Add(self.ultrahighbtn, 1, wx.EXPAND|wx.ALIGN_CENTER, 10)
        sizer.AddSpacer(10)
        sizer.Add(self.restartbtn, 1, wx.EXPAND|wx.ALIGN_CENTER, 10)

        self.panel.SetSizerAndFit(sizer)
        self.panel.Layout()

    def OnClose(self, evt):
        self.Close()

    def OnDefaultDpi(self, evt):
        wlr = subprocess.Popen(['wlr-randr', '--output', 'DSI-1', '--scale', '2'])

    def OnLowDpi(self, evt):
        wlr = subprocess.Popen(['wlr-randr', '--output', 'DSI-1', '--scale', '1.75'])

    def OnMediumDpi(self, evt):
        wlr = subprocess.Popen(['wlr-randr', '--output', 'DSI-1', '--scale', '1.5'])

    def OnHighDpi(self, evt):
        wlr = subprocess.Popen(['wlr-randr', '--output', 'DSI-1', '--scale', '1.25'])

    def OnUltraHighDpi(self, evt):
        wlr = subprocess.Popen(['wlr-randr', '--output', 'DSI-1', '--scale', '1'])

    def OnRestartPhosh(self, evt):
        rsp = subprocess.Popen(['sudo', 'systemctl', 'restart', 'phosh'])

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, "Phosh Scaler")
        self.SetTopWindow(frame)

        frame.Show(True)

        return True

app = MyApp()
app.MainLoop()

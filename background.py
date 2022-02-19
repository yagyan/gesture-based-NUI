import win32gui
while(True):
    windowTile = ""
    while(True):
        newWindowTile = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if(newWindowTile != windowTile):
            windowTile = newWindowTile
            print(windowTile)

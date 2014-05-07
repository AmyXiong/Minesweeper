import wx
import random

class MSframe(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,wx.ID_ANY, "MineSweeper!!!")
		self.panel = wx.Panel(self)
		
		ButtonsRow = []
		a = 10
		b = 50
		for i in range (1,10):
			Column = []
			ButtonsRow.append(Column)
			a += 30
			b = 50
			for j in range (1,10):
				btn = wx. Button(self.panel, pos=(a, b),size=(30,30))
				b += 30
				Column.append(btn)
				
		for i in range (10):
			x = random.randint(0,10)
			y = random.randint(0,10)
			ButtonsRow[x[y]] = 1
		
	def OnClickbtn(self,e):
		if btn != 1:
			number = 0
			#for btn in ButtonsRow:
			
			
	
MineSweeper = wx.App(False)
frame = MSframe(None)
frame.Show(True)
MineSweeper.MainLoop()
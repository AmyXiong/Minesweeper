import wx
import random

class MSButton(wx.Button):
	def __init__(self,x, y,isMine,number, parent, pos, size):
		wx.Button.__init__(self,parent, pos = pos, size = size)
		self.isMine = isMine
		self.x = x
		self.y = y
		self.number = 0
		

class MSframe(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,wx.ID_ANY, "MineSweeper!!!")
		self.panel = wx.Panel(self)
		
		self.ButtonsRow = []
		a = 10
		b = 50
		for x in range (0,9):
			Column = []
			self.ButtonsRow.append(Column)
			a += 30
			b = 50
			for y in range (0,9):
				btn = MSButton( x, y,False,0,self.panel,pos=(a, b),size=(30,30))
				b += 30
				Column.append(btn)
				btn.Bind(wx.EVT_BUTTON, self.OnClickbtn)

		for i in range(10):
			p = random.randint(0,8)
			q = random.randint(0,8)
			self.ButtonsRow[p][q].isMine = True
			print p,q
			
		for column in self.ButtonsRow:
			for button in column:
				for i in range(-1,1):
					for j in range (-1,1):
						if self.ButtonsRow[button.x+i][button.y+j].isMine:
							button.number += 1
		self.BombIconFile = wx.Image("Minesweeper_Icon.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		
	def OnClickbtn(self,e):
		clickedButton = e.GetEventObject()
		if not clickedButton.isMine:
			if clickedButton.number != 0:
				clickedButton.number = str(clickedButton.number)
				clickedButton.SetLabel(clickedButton.number)
			else:
				clickedButton.Disable()
				for i in range(-1,1):
					for j in range (-1,1):
						evt = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.GetId())
						evt.SetEventObject(self.ButtonsRow[clickedButton.x+i][clickedButton.y+j])
						self.ButtonsRow[clickedButton.x+i][clickedButton.y+j].GetEventHandler().ProcessEvent(evt)

		else:
			print "is a mine"
			for column in self.ButtonsRow:
				for button in column:
					if button.isMine == True:
						button.SetBitmapLabel(self.BombIconFile)
			
		
	
	
						
	
MineSweeper = wx.App(False)
frame = MSframe(None)
frame.Show(True)
MineSweeper.MainLoop()

__author__ = "Saulius Bartkus"
__copyright__ = "Copyright 2017"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Saulius Bartkus"
__email__ = "saulius181@yahoo.com"
__status__ = "Production"

from tkinter import *
import random
EMPTY_COLOR = "pink"

class game_controller(object):
#Define las posiciones en el tablero del enemigo "AI"
	def ai_deploy(self):
		self.canvas.data["aiBoard"]	= {  
   0:{  
      0:{  
         'presence':None,
         'ref':101
      },
      1:{  
         'presence':None,
         'ref':102
      },
      2:{  
         'presence':None,
         'ref':103
      },
      3:{  
         'presence':None,
         'ref':104
      },
      4:{  
         'presence':None,
         'ref':105
      },
      5:{  
         'presence':None,
         'ref':106
      },
      6:{  
         'presence':None,
         'ref':107
      },
      7:{  
         'presence':None,
         'ref':108
      },
      8:{  
         'presence':None,
         'ref':109
      },
      9:{  
         'presence':'Frigate',
         'ref':110
      }
   },
   1:{  
      0:{  
         'presence':None,
         'ref':111
      },
      1:{  
         'presence':'Destroyer',
         'ref':112
      },
      2:{  
         'presence':'Destroyer',
         'ref':113
      },
      3:{  
         'presence':None,
         'ref':114
      },
      4:{  
         'presence':'AircraftCarrier',
         'ref':115
      },
      5:{  
         'presence':'AircraftCarrier',
         'ref':116
      },
      6:{  
         'presence':'AircraftCarrier',
         'ref':117
      },
      7:{  
         'presence':'AircraftCarrier',
         'ref':118
      },
      8:{  
         'presence':'AircraftCarrier',
         'ref':119
      },
      9:{  
         'presence':None,
         'ref':120
      }
   },
   2:{  
      0:{  
         'presence':None,
         'ref':121
      },
      1:{  
         'presence':None,
         'ref':122
      },
      2:{  
         'presence':None,
         'ref':123
      },
      3:{  
         'presence':None,
         'ref':124
      },
      4:{  
         'presence':None,
         'ref':125
      },
      5:{  
         'presence':None,
         'ref':126
      },
      6:{  
         'presence':None,
         'ref':127
      },
      7:{  
         'presence':None,
         'ref':128
      },
      8:{  
         'presence':None,
         'ref':129
      },
      9:{  
         'presence':None,
         'ref':130
      }
   },
   3:{  
      0:{  
         'presence':None,
         'ref':131
      },
      1:{  
         'presence':'Destroyer',
         'ref':132
      },
      2:{  
         'presence':'Destroyer',
         'ref':133
      },
      3:{  
         'presence':None,
         'ref':134
      },
      4:{  
         'presence':None,
         'ref':135
      },
      5:{  
         'presence':'Battleship',
         'ref':136
      },
      6:{  
         'presence':'Battleship',
         'ref':137
      },
      7:{  
         'presence':'Battleship',
         'ref':138
      },
      8:{  
         'presence':'Battleship',
         'ref':139
      },
      9:{  
         'presence':None,
         'ref':140
      }
   },
   4:{  
      0:{  
         'presence':'Frigate',
         'ref':141
      },
      1:{  
         'presence':None,
         'ref':142
      },
      2:{  
         'presence':None,
         'ref':143
      },
      3:{  
         'presence':None,
         'ref':144
      },
      4:{  
         'presence':None,
         'ref':145
      },
      5:{  
         'presence':None,
         'ref':146
      },
      6:{  
         'presence':None,
         'ref':147
      },
      7:{  
         'presence':None,
         'ref':148
      },
      8:{  
         'presence':None,
         'ref':149
      },
      9:{  
         'presence':None,
         'ref':150
      }
   },
   5:{  
      0:{  
         'presence':None,
         'ref':151
      },
      1:{  
         'presence':'Destroyer',
         'ref':152
      },
      2:{  
         'presence':'Destroyer',
         'ref':153
      },
      3:{  
         'presence':None,
         'ref':154
      },
      4:{  
         'presence':'Battleship',
         'ref':155
      },
      5:{  
         'presence':'Battleship',
         'ref':156
      },
      6:{  
         'presence':'Battleship',
         'ref':157
      },
      7:{  
         'presence':'Battleship',
         'ref':158
      },
      8:{  
         'presence':None,
         'ref':159
      },
      9:{  
         'presence':'Frigate',
         'ref':160
      }
   },
   6:{  
      0:{  
         'presence':None,
         'ref':161
      },
      1:{  
         'presence':None,
         'ref':162
      },
      2:{  
         'presence':None,
         'ref':163
      },
      3:{  
         'presence':None,
         'ref':164
      },
      4:{  
         'presence':None,
         'ref':165
      },
      5:{  
         'presence':None,
         'ref':166
      },
      6:{  
         'presence':None,
         'ref':167
      },
      7:{  
         'presence':None,
         'ref':168
      },
      8:{  
         'presence':None,
         'ref':169
      },
      9:{  
         'presence':None,
         'ref':170
      }
   },
   7:{  
      0:{  
         'presence':None,
         'ref':171
      },
      1:{  
         'presence':'Destroyer',
         'ref':172
      },
      2:{  
         'presence':'Destroyer',
         'ref':173
      },
      3:{  
         'presence':None,
         'ref':174
      },
      4:{  
         'presence':'Frigate',
         'ref':175
      },
      5:{  
         'presence':None,
         'ref':176
      },
      6:{  
         'presence':'Cruiser',
         'ref':177
      },
      7:{  
         'presence':'Cruiser',
         'ref':178
      },
      8:{  
         'presence':'Cruiser',
         'ref':179
      },
      9:{  
         'presence':None,
         'ref':180
      }
   },
   8:{  
      0:{  
         'presence':None,
         'ref':181
      },
      1:{  
         'presence':None,
         'ref':182
      },
      2:{  
         'presence':None,
         'ref':183
      },
      3:{  
         'presence':None,
         'ref':184
      },
      4:{  
         'presence':None,
         'ref':185
      },
      5:{  
         'presence':None,
         'ref':186
      },
      6:{  
         'presence':None,
         'ref':187
      },
      7:{  
         'presence':None,
         'ref':188
      },
      8:{  
         'presence':None,
         'ref':189
      },
      9:{  
         'presence':None,
         'ref':190
      }
   },
   9:{  
      0:{  
         'presence':None,
         'ref':191
      },
      1:{  
         'presence':'Frigate',
         'ref':192
      },
      2:{  
         'presence':None,
         'ref':193
      },
      3:{  
         'presence':'Cruiser',
         'ref':194
      },
      4:{  
         'presence':'Cruiser',
         'ref':195
      },
      5:{  
         'presence':'Cruiser',
         'ref':196
      },
      6:{  
         'presence':None,
         'ref':197
      },
      7:{  
         'presence':'Cruiser',
         'ref':198
      },
      8:{  
         'presence':'Cruiser',
         'ref':199
      },
      9:{  
         'presence':'Cruiser',
         'ref':200
      }
   }
}
#Funcion que determina a donde disparará la AI enemiga
	def ai(self):
      #Elige una posicion al azar de una lista de posiciones posibles
		ai_pick = random.choice(self.canvas.data["aiHitList"])
      #Elimina de la lista cada posicion a la que dispara
		self.canvas.data["aiHitList"].remove(ai_pick)
		#Las celdas a las que disparó la IA se les marca como hit o "disparadas"
		self.canvas.addtag_withtag("hit", self.canvas.data["playerBoard"][ai_pick[0]][ai_pick[1]]["ref"])
      #Se cargan los nuevos datos al tablero
		self.canvas.data["play"] = True
		self.redraw_board()

	#Funcion para iniciar el juego
	def start(self):
      #Si no hay un juego en curso, iniciarlo y poner al usuario a ubicar sus barcos
		if self.canvas.data["play"] == None:
			self.canvas.data["play"] = True
			self.currentDeploy = self.canvas.data["shipTypes"]["typeList"][0]
			self.deploy_state()

      #Si el juego se abandonó, seguir la ejecucion
		elif self.canvas.data["play"] == False:
			pass
		else:
			pass
   #Funcion que establece como el jugador desplegará sus barcos
	def deploy_state(self):
      #Si el jugador aun no ha desplegado todos sus barcos, seguir desplegando
		if self.canvas.data["shipTypes"][self.currentDeploy]["count"] != self.canvas.data["shipTypes"][self.currentDeploy]["player"]:
			self.canvas.data["stage"] = "deploy"
		else:
			nextIndex = self.canvas.data["shipTypes"]["typeList"].index(self.currentDeploy) + 1
			if nextIndex < len(self.canvas.data["shipTypes"]["typeList"]):
				self.currentDeploy = self.canvas.data["shipTypes"]["typeList"][nextIndex]
            #Cuando el jugador termine de desplegar todos sus barcos, incia a jugar
			else:
				self.canvas.data["stage"] = "play"
#				self.redraw_board()
			
	#Funcion que define como se abandona una partida
	def quit(self):
		self.root.destroy()
		
   #Funcion que define que hacer en caso de clickear una celda del tablero para atacar
	def on_click1(self, event=None):
		if self.canvas.data["play"]:
#			deploy_list = self.get_deploy_list()
#			print(deploy_list["valid"])
			if self.canvas.data["stage"] == "deploy":
				if self.get_deploy_list()["valid"]:
					_y = int( self.canvas.gettags(CURRENT)[2] )
					_x = int( self.canvas.gettags(CURRENT)[3] )
					
			
					if self.canvas.data["deployDir"] == "horizontal":
						for x in range(_x, _x + self.canvas.data["shipTypes"][self.currentDeploy]["size"]):

							self.canvas.itemconfig(self.canvas.data["playerBoard"][_y][x]["ref"], fill="#0000FF")
							self.canvas.data["playerBoard"][_y][x]["presence"] = self.currentDeploy
						self.canvas.data["shipTypes"][self.currentDeploy]["player"] +=1
						self.deploy_state()

					else:
						for y in range(_y, _y + self.canvas.data["shipTypes"][self.currentDeploy]["size"]):
							self.canvas.itemconfig(self.canvas.data["playerBoard"][y][_x]["ref"], fill="#0000FF")		
							self.canvas.data["playerBoard"][y][_x]["presence"] = self.currentDeploy				
						self.canvas.data["shipTypes"][self.currentDeploy]["player"] +=1
						self.deploy_state()
			elif self.canvas.data["stage"] == "play":				
				if not "hit" in self.canvas.gettags(CURRENT) and "block" in self.canvas.gettags(CURRENT) and "ai" in self.canvas.gettags(CURRENT): 

					self.canvas.addtag_withtag("hit", CURRENT)
					self.redraw_board()
					self.canvas.data["play"] = False
					self.ai()
   #Funcion que maneja el click para el despliegue de barcos
	def on_click3(self, event=None):
		if self.canvas.data["play"]:
			if self.canvas.data["deployDir"] == "horizontal":
				self.canvas.data["deployDir"] = "vertical"
			else:
				self.canvas.data["deployDir"] = "horizontal"
			self.redraw_board()

			
	def on_release(self, event=None):
		pass
		
	def on_enter(self, event=None):
		#print("Test")
		if self.canvas.data["play"]:
			if self.canvas.data["stage"] == "deploy" and "block" in self.canvas.gettags(CURRENT) and "player" in self.canvas.gettags(CURRENT):
				self.currentId = self.canvas.find_withtag(CURRENT)[0]
				self.redraw_board()
			elif self.canvas.data["stage"] == "play" and "block" in self.canvas.gettags(CURRENT):
				self.currentId = self.canvas.find_withtag(CURRENT)[0]
				self.redraw_board()

	def get_deploy_list(self):
		deploy_list = {}
		if "block" in self.canvas.gettags(CURRENT):
			_y = int( self.canvas.gettags(CURRENT)[2] )
			_x = int( self.canvas.gettags(CURRENT)[3] )
			deploy_list["valid"] = True
			if self.canvas.data["deployDir"] == "horizontal":
				deploy_list[_y] = {}
				for x in range(_x, _x + self.canvas.data["shipTypes"][self.currentDeploy]["size"]):
					if x in self.canvas.data["playerBoard"][_y]:
						if self.canvas.data["playerBoard"][_y][x]["presence"] in self.canvas.data["shipTypes"]["typeList"]: 
							deploy_list[_y][x] = False
							deploy_list["valid"] = False
						else:
							deploy_list[_y][x] = True
					else:
						deploy_list["valid"] = False
						break
			else:
				for y in range(_y, _y + self.canvas.data["shipTypes"][self.currentDeploy]["size"]):		
					if y in self.canvas.data["playerBoard"]:
						deploy_list[y] = {}
						if self.canvas.data["playerBoard"][y][_x]["presence"] in self.canvas.data["shipTypes"]["typeList"]: 
							deploy_list[y][_x] = False
							deploy_list["valid"] = False
						else:
							deploy_list[y][_x] = True
					else:
						deploy_list["valid"] = False					
						break
		else:
			deploy_list["valid"] = False
		return deploy_list
		
	def redraw_board(self):
		if self.canvas.data["play"]:
			if self.canvas.data["stage"] == "deploy":
				deploy_list = self.get_deploy_list()
				for y in range(0,10):
					for x in range(0,10):
						
						if y in deploy_list and x in deploy_list[y] and deploy_list[y][x] == False:
							self.canvas.itemconfig(self.canvas.data["playerBoard"][y][x]["ref"], fill="#FF0000")		
						elif y in deploy_list and x in deploy_list[y] and deploy_list[y][x] == True:
							self.canvas.itemconfig(self.canvas.data["playerBoard"][y][x]["ref"], fill="#AAAAFF")				
						elif self.canvas.data["playerBoard"][y][x]["presence"] in self.canvas.data["shipTypes"]["typeList"]:
							self.canvas.itemconfig(self.canvas.data["playerBoard"][y][x]["ref"], fill="#0000FF")	
						else:
							self.canvas.itemconfig(self.canvas.data["playerBoard"][y][x]["ref"], fill=EMPTY_COLOR)
			elif self.canvas.data["stage"] == "play":
				for y in range(0,10):
					for x in range(0,10):
						if self.canvas.data["playerBoard"][y][x]["ref"] == self.currentId and self.canvas.data["playerBoard"][y][x]["presence"]:
							self.canvas.itemconfig(self.canvas.data["playerBoard"][y][x]["ref"], fill="#FF0000")	
						elif self.canvas.data["playerBoard"][y][x]["ref"] == self.currentId and not self.canvas.data["playerBoard"][y][x]["presence"]:
							self.canvas.itemconfig(self.canvas.data["playerBoard"][y][x]["ref"], fill="#CC0000")
							
						elif "hit" in self.canvas.gettags(self.canvas.data["playerBoard"][y][x]["ref"]) and self.canvas.data["playerBoard"][y][x]["presence"]:
							self.canvas.itemconfig(self.canvas.data["playerBoard"][y][x]["ref"], fill="#000000")
						elif "hit" in self.canvas.gettags(self.canvas.data["playerBoard"][y][x]["ref"]) and not self.canvas.data["playerBoard"][y][x]["presence"]:
							self.canvas.itemconfig(self.canvas.data["playerBoard"][y][x]["ref"], fill="#AAAAAA")
							
						elif self.canvas.data["playerBoard"][y][x]["presence"] in self.canvas.data["shipTypes"]["typeList"]:
							self.canvas.itemconfig(self.canvas.data["playerBoard"][y][x]["ref"], fill="#0000FF")	
						else:
							self.canvas.itemconfig(self.canvas.data["playerBoard"][y][x]["ref"], fill=EMPTY_COLOR)
							
						if self.canvas.data["aiBoard"][y][x]["ref"] == self.currentId:
							self.canvas.itemconfig(self.canvas.data["aiBoard"][y][x]["ref"], fill="#CC0000")
						elif "hit" in self.canvas.gettags(self.canvas.data["aiBoard"][y][x]["ref"]) and self.canvas.data["aiBoard"][y][x]["presence"]:
							self.canvas.itemconfig(self.canvas.data["aiBoard"][y][x]["ref"], fill="#000000")
						elif "hit" in self.canvas.gettags(self.canvas.data["aiBoard"][y][x]["ref"]) and not self.canvas.data["aiBoard"][y][x]["presence"]:
							self.canvas.itemconfig(self.canvas.data["aiBoard"][y][x]["ref"], fill="#AAAAAA")							
						else:
							self.canvas.itemconfig(self.canvas.data["aiBoard"][y][x]["ref"], fill=EMPTY_COLOR)
				
	def on_leave(self, event=None):
		if self.canvas.data["play"]:
			if self.canvas.data["stage"] == "deploy" and self.currentId:
				self.redraw_board()							
				self.currentId = None
	
	def __init__(self, root):
		self.root = root
		self.canvas = Canvas(root, width=850, height=350)

		self.canvas.pack()	
		self.button1 = Button(self.canvas, text = "New game", anchor = W, command = self.start)
		self.button1.place(x=720,y=25)
		self.button2 = Button(self.canvas, text = "Quit", anchor = W, command = self.quit)
		self.button2.place(x=790,y=25)		
	
		self.canvas.bind("<Button-1>", self.on_click1)
		self.canvas.bind("<Button-3>", self.on_click3)
		self.canvas.bind("<ButtonRelease-1>", self.on_release)
		self.canvas.data = { }
		self.canvas.data["play"] = None
		self.canvas.data["stage"] = None
		self.canvas.data["deployDir"] = "horizontal"
		
		self.canvas.data["playerBoard"] = {}
		self.canvas.data["aiBoard"] = {}
		self.canvas.data["aiHitList"] = []
		
		self.canvas.data["shipTypes"] = {}
		self.canvas.data["shipTypes"]["typeList"] = ["AircraftCarrier", "Battleship", "Cruiser", "Destroyer", "Frigate"]
		self.canvas.data["shipTypes"]["AircraftCarrier"] = {"size": 5, "count": 1, "player": 0, "ai": 0}
		self.canvas.data["shipTypes"]["Battleship"] = {"size": 4, "count": 2, "player": 0, "ai": 0}
		self.canvas.data["shipTypes"]["Cruiser"] = {"size": 3, "count": 3, "player": 0, "ai": 0}
		self.canvas.data["shipTypes"]["Destroyer"] = {"size": 2, "count": 4, "player": 0, "ai": 0}
		self.canvas.data["shipTypes"]["Frigate"] = {"size": 1, "count": 5, "player": 0, "ai": 0}
		
		self.currentId = None	
		
		for y in range(0,10):
			self.canvas.data["playerBoard"][y] = {}
			for x in range(0,10):
				self.canvas.data["playerBoard"][y][x] = {}
				self.canvas.data["playerBoard"][y][x]["ref"] = self.canvas.create_rectangle(30+x*30, 30+y*30, 30+30+ x*30, 30+30 +y*30, fill=EMPTY_COLOR, tags="block player {} {}".format(y,x))
				self.canvas.data["playerBoard"][y][x]["presence"] = None
				self.canvas.tag_bind(self.canvas.data["playerBoard"][y][x]["ref"], "<Enter>", self.on_enter)
				self.canvas.tag_bind(self.canvas.data["playerBoard"][y][x]["ref"], "<Leave>", self.on_leave)	
		
		for y in range(0,10):
			self.canvas.data["aiBoard"][y] = {}
			for x in range(0,10):
				self.canvas.data["aiBoard"][y][x] = {}
				self.canvas.data["aiBoard"][y][x]["ref"] = self.canvas.create_rectangle(20+x*30 + 350, 30+y*30, 20+30+ x*30 + 350, 30+30 +y*30, fill=EMPTY_COLOR, tags="block ai {} {}".format(y,x))
				self.canvas.data["aiBoard"][y][x]["presence"] = None
				self.canvas.data["aiHitList"].append( [y, x] )
				self.canvas.tag_bind(self.canvas.data["aiBoard"][y][x]["ref"], "<Enter>", self.on_enter)
				self.canvas.tag_bind(self.canvas.data["aiBoard"][y][x]["ref"], "<Leave>", self.on_leave)	

		self.text = self.canvas.create_text(740,10, text="Battleships", anchor='w')
		self.ai_deploy()
				
if __name__ == "__main__":
	root = Tk()
	root.title("Battleships Tk")
	root.resizable(0,0)
	game = game_controller(root)
	root.mainloop()

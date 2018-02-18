####################################
###  This is Toontown Journey's  ###
###    Development Launcher      ###
###   For  Testing  uses  only   ###
### Edited for Mr. T's Altis Mod ###
###      By. Christian M.        ###
####################################

#pos = (X, Y, Z)

from panda3d.core import *
loadPrcFileData("", "window-title Mr. Tankthrusts Toontown: Project Altis Modifications")
loadPrcFileData("", "win-size 1200 600")
loadPrcFileData("", "win-origin 200 200")
import direct.directbase.DirectStart
from direct.gui.DirectGui import *
import os
#import toontown.toonbase.ToontownStart
background=OnscreenImage(image = 'resources/phase_3/maps/background.jpg', pos = (0, 0, 0),parent=render2d)
background.setTransparency(TransparencyAttrib.MAlpha)

logo=OnscreenImage(image = 'resources/phase_3/maps/toontown-logo.png', pos = (0, 0, 0),parent=render2d)
logo.setTransparency(TransparencyAttrib.MAlpha)
logo.setScale(0.3)

buttonup=OnscreenImage(image = 'resources/launcher/Button_Up.png', pos = (0, 0, 0))
buttonup.setTransparency(TransparencyAttrib.MAlpha)
buttonup.setScale(0.0)

buttondown=OnscreenImage(image = 'resources/launcher/Button_Down.png', pos = (0, 0, 0))
buttondown.setTransparency(TransparencyAttrib.MAlpha)
buttondown.setScale(0.0)

with open('PPYTHON_PATH') as ppython:
	lines = [line.strip('[') for line in open ('PPYTHON_PATH')]
print lines
username = None
password = None
ip = None
#setup mythod to to ask for user input
def setUsername(textEntered):
    global username
    user__t.hide()
    user_b.hide()
    pass__t.show()
    pass_b.show()
    username = textEntered

def setPassword(textEntered):
    global password
    pass__t.hide()
    pass_b.hide()
    ip__t.show()
    ip_b.show()
    password = textEntered

def setIp(textEntered):
    global ip
    user__t.hide()
    user_b.hide()
    ip__t.hide()
    ip_b.hide()
    play_b.show()
    ip = textEntered

 
#Add the Username Area
user_b = DirectEntry(text = "" ,scale=.05,command=setUsername,\
pos = (-.35, 0, -.7 ), numLines = 1,width=15,obscured=0)
#Add the Password Area
pass_b = DirectEntry(text = "" ,scale=.05,command=setPassword,\
pos = (-.35, 0, -.7 ), numLines = 1,width=15,obscured=1)
#Add IP Address Area
ip_b = DirectEntry(text = "" ,scale=.05,command=setIp,\
pos = (-.35, 0, -.7 ), numLines = 1,width=15,obscured=0)

#Add Text to the button
#As well as position it.
user_t = TextNode('user')
user__t = aspect2d.attachNewNode(user_t)
user__t.setScale(0.07), user_t.setText("Username:")
user__t.setPos(-.73 , 0, -.7 ), user_t.setShadow(0.10, 0.10), user_t.setShadowColor(0, 0, 0, 1)

pass_t = TextNode('pass')
pass__t = aspect2d.attachNewNode(pass_t)
pass__t.setScale(0.07), pass_t.setText("Password:")
pass__t.setPos(-.73 , 0, -.697 ), pass_t.setShadow(0.10, 0.10), pass_t.setShadowColor(0, 0, 0, 1)
pass__t.hide()
pass_b.hide()

ip_t = TextNode('ip')
ip__t = aspect2d.attachNewNode(ip_t)
ip__t.setScale(0.07), ip_t.setText("ip:")
ip__t.setPos(-.45 , 0, -.695 ), ip_t.setShadow(0.10, 0.10), ip_t.setShadowColor(0, 0, 0, 1)
ip__t.hide()
ip_b.hide()

def launch():

    #Preparing for launching
	#Cheap way of killing the launcher XD
	os.environ['launcher'] = str(os.getpid())
	os.environ['islauncher'] = str("1")
	
	#Grabbing the play cookie(YUMMY COOKIE :D)
	#also takes the game server here too
	os.environ['TT_PLAYCOOKIE'] = str(username)
	os.environ['TT_PASSWORD'] = str(password)
	os.environ['TT_GAMESERVER'] = str(ip)
	
	pp = str("panda\python\ppython.exe")
	
	#and LAUNCH the game
	os.system(pp + ' -m toontown.toonbase.ClientStart')	

#setting up the play button
play_b = DirectButton(frameSize=None, image=(buttonup,buttondown,buttonup), relief=None,  
command=launch, pos = (0, 0, -.7 ), scale=0.27)
play_b.hide()


#start the GUI
base.run()

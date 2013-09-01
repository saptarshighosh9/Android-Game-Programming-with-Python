import pygame, sys
from pygame.locals import *

try:
   import android
except ImportError:
   android = None	
	


pygame.init()

if android:
   android.init()
   android.map_key(android.KEYCODE_BACK,pygame.K_ESCAPE)
else:
   print "error"
   
while True:	
	scr=0
	hit=200
	b=0
	l=0
	
	FPS = 10
	clock = pygame.time.Clock()
	size=(480,320)
	screen=pygame.display.set_mode(size)
	RED=(255,0,0)
	BLACK=(0,0,0)
	GREEN= (0,255,0)
	BLUE = (0,0,255)
	player_rect = pygame.Rect(300,20,64,64)
	player_rectt = pygame.Rect(300,230,64,64)
	im1=pygame.image.load("pp1.gif")
	im2=pygame.image.load("bn.jpg")
	im3=pygame.image.load("b1.jpg")
	st1=pygame.image.load("st1.png")
	stt=pygame.image.load("start.png")
	st1=pygame.image.load("st1.png")
	win=pygame.image.load("win.jpg")
	tu=pygame.image.load("tu.png")
	lose=pygame.image.load("lose.png")
	stt=pygame.image.load("start.png")
	up_rect = pygame.Rect(400 ,150,60,40)
	down_rect = pygame.Rect(300 ,230,40,40)
	left_rect = pygame.Rect(250 ,190,40,40)
	right_rect = pygame.Rect(350 ,190,40,40)
	startbox=pygame.Rect(380 ,260,80,80)
	i1=pygame.image.load("1.gif")
	i2=pygame.image.load("2.gif")
	i3=pygame.image.load("3.gif")
	i4=pygame.image.load("4.gif")
	i5=pygame.image.load("5.gif")
	i6=pygame.image.load("6.gif")
	fff=pygame.image.load("fff.png")
	h=pygame.image.load("h.png")
	m=pygame.image.load("m.png")
	
	p=pygame.image.load("nn.png")
	sco=pygame.image.load("score.png")
	tm=pygame.image.load("time.png")
	bc1=pygame.image.load("bcc1.png")
	bc2=pygame.image.load("bcc2.png")
	bc3=pygame.image.load("bcc3.png")
	pt=pygame.image.load("as.png")
	r=0
	x=0
	yy=0
	zz=0
	bl=[]
	for i in range(0,512,32):
	    g= pygame.Rect(i,298,32,32)
	    bl.append(g)
	       
	c=1
	d=1
	direction = "abc"
	label1=True
	label2=False
	label3=False
	label4=False
########################################################################

	while label1==True:
	     for event in pygame.event.get():
		 if event.type == pygame.QUIT:
		     pygame.quit()
		     sys.exit()
		 elif event.type == KEYDOWN:
		      if event.key == K_ESCAPE: 
			 pygame.quit()
			 sys.exit() 	
			 
		 
	     screen.blit(fff,[0,0])       
	     pygame.display.update() 
	     pygame.time.wait(10000)
	     label1=False
	     label2=True
	     break
	     clock.tick(FPS)
	     pygame.display.update() 
	#############################################################################
	while label2==True:
	     for event in pygame.event.get():
		 if event.type == pygame.QUIT:
		     pygame.quit()
		     sys.exit()
		 elif event.type == KEYDOWN:
		      if event.key == K_ESCAPE: 
			 pygame.quit()
			 sys.exit() 	
			 
		 
		 mouse_pos = pygame.mouse.get_pos()
		 if startbox.collidepoint(mouse_pos):
		    label2=False
		    label3=True        
	     screen.fill(BLACK)
	     screen.blit(st1,[0,0])
	     screen.blit(stt,[350,260])
	     clock.tick(FPS)
	     pygame.display.update()   	
	
	
	##############################################################################
	
	while label3==True:
	     for event in pygame.event.get():
		 if event.type == pygame.QUIT:
		     pygame.quit()
		     sys.exit()
		 elif event.type == KEYDOWN:
		      if event.key == K_ESCAPE: 
			 pygame.quit()
			 sys.exit()     
		 
		 
		 mouse_pos = pygame.mouse.get_pos()
		 if up_rect.collidepoint(mouse_pos) and direction== "abc":
		    direction = "up"
	 
		  
		 
			    
	     screen.fill(BLACK)    
	     
	     
	     
	     
	     if d== 1:
		screen.blit(bc1,[0,0])     
		d+=1
	     elif d==2:  
		screen.blit(bc3,[0,0])     
		d+=1
	     elif d==3:   
		screen.blit(bc2,[0,0])     
		d+=1
	     elif d==4:   
		screen.blit(bc1,[0,0])     
		d+=1   
	     elif d==5:   
		screen.blit(bc3,[0,0])     
		d+=1 
	     elif d==6:   
		screen.blit(bc2,[0,0])     
		d=1 
	     
	     if direction=="abc":
		if c== 1:    
		   screen.blit(i1,player_rectt)
		   c+=1
		elif c==2:  
		   
		   screen.blit(i2,player_rectt)
		   c+=1
		elif c==3:   
		     
		   screen.blit(i3,player_rectt)
		   c+=1
		elif c==4:   
		     
		  screen.blit(i4,player_rectt)
		  c+=1   
		elif c==5:        
		  screen.blit(i5,player_rectt)
		  c+=1 
		elif c==6:       
		  screen.blit(i6,player_rectt)
		  c=1    
	     else:     
		  screen.blit(i1,player_rect)    
		  
		  
		  
		  
	     if direction=="abc":
		    
		if b==300:   	
		   scr +=5
		if l==300:
		   hit -=5
	       
	    
	     pygame.draw.rect(screen,BLACK,up_rect)
	     screen.blit(p,up_rect)
	     if bl[0].right <=0:
		bl=bl[1:]
		bl.append(pygame.Rect(480,298,32,32))
	       
	     for g in bl:
		 screen.blit(im3,g)
		 g.left -=8
		 
		 
	   
	     if direction == "up":
		k=player_rect.centery 
		player_rect.centery -=10 
		if player_rect.centery < 100:
		   player_rect.centery=k 	
		   direction = "abc"
	         
	     
	     
	     b=20*x
	     l=10*yy
	     
	     
	     screen.blit(h,[b,265])
	    
	     screen.blit(m,[l,265])
	     
	     x +=3
	     yy+=5
	
	     if b>480:
		x=0
	     if l>480:
		yy=0
	     
	     if hit<0:
		label3=False
		label4=True  
		ooo=False
		
	     if scr <0:
		scr=0
	     if scr > 270:
		label3=False
		label4=True      
		ooo=True    
	     dd = pygame.Rect(50,10,scr,3)
	     pygame.draw.rect(screen,BLACK,dd)
	     ddd = pygame.Rect(50,20,hit,3)
	     pygame.draw.rect(screen,RED,ddd)
	     screen.blit(pt,[0,0])
	     
	     clock.tick(FPS)
	     pygame.display.update()        
	 
	 
	while label4==True:
	     for event in pygame.event.get():
		 if event.type == pygame.QUIT:
		     pygame.quit()
		     sys.exit()
		 elif event.type == KEYDOWN:
		      if event.key == K_ESCAPE: 
			 pygame.quit()
			 sys.exit() 	
			 
		 
		 mouse_pos = pygame.mouse.get_pos()
		 if startbox.collidepoint(mouse_pos):
		    label4=False
		    label1=True 
	     screen.fill(BLACK)
	     if ooo==True:
		screen.blit(win,[0,0])     
	     else:
		screen.blit(lose,[0,0])     
	     screen.blit(tu,[380,260])
	     clock.tick(FPS)
	     pygame.display.update() 

from random import* 
import random
import time
from time import ctime
from types import NoneType



######## The improved and Solved problem code: ########
import speech_recognition as sr
import pyttsx3
def speak(x):
    e=pyttsx3.init()
    e.say(x)
    e.runAndWait()

def listener():
	recognizer = sr.Recognizer()
	try:
		with sr.Microphone() as source:
			
			recognizer.adjust_for_ambient_noise(source)#(Problem Solved)
			voice= recognizer.listen(source)
			text= recognizer.recognize_google(voice)
			return text
	except:
		return "invalid"





# keys
aa=["what's up","how are you","how you dong","how r u","whats up" ,"hey whats up" ,"hey what's up"]
bb=["yes i am fine","fine","i am fine","good","well","better","okay"]
cc=["not well","ill", "not good","i am not fine","i am not good","not fine"]
dd=["thanks","thank you","thankyou"]

#
ee=["who are you", "who r u","who r you","who are u","what is your name","what is ur name"]
ff=["who is jarvis","who is JARVIS","who is J.A.R.V.I.S","what is jarvis","i don't know you","i don't know who is jarvis"]

#
gg=["What can you do", "what can you do","what can u do","What can u do","what is your capabilities","your capabilities"]
hh=["YES","YEAH","AFCOURSE","OFCOURSE","DEFINITELY","SURE","ABSOLUTELY"]
ii=["NO","NAY","NAH","NOPE"]

#
jj=["HEY JARVIS","OK JARVIS","HELLO JARVIS","HI JARVIS","WHATS UP JARVIS","WHAT'S UP JARVIS","HELLO"]
kk=["NO I AM FINE","NO","NO THANKS","NO I DONT NEED","NOT NEEDED","NOT REQUIRED"]
ll=["THANKYOU JARVIS","THANKS JARVIS","THANKS","THANK YOU JARVIS","THANKYOU","THANK YOU"]

#
mm=["YOU SUCK", "YOU ARE WORTHLESS","YOU ARE STUPID","YOU ARE A CRAP","YOU ARE NOT GOOD","GOOGLE ASSISTANT IS BETTER THAN YOU","ARE YOU STUPID","ARE YOU BRAINLESS","YOU ARE BAD","YOU ARE USELESS"]


#
nn=["WHAT TIME IS IT","COULD I KNOW THE TIME PLEASE","TIME","WHICH DAY IS TODAY","TODAY'S DATE","TODAYS DATE","WHAT TIME IS NOW","DAY","DATE"]


#
oo=["I AM BORED","BORED","BORED JARVIS","I AM BORED JARVIS","MAKE ME FEEL HAPPIER","MAKE ME HAPPY"]










def check(s):
		if  s in aa:
			time.sleep(0.5)
			print("I am fine sir, How are you")
			speak("I am fine sir, How are you")
			a=listener()
			if a in bb and a not in cc  :
				time.sleep(0.5)
				print("Happy to hear that ,")
				speak("Happy to hear that ")
			elif a in cc:
				time.sleep(0.9)
				print("I feel really sad that you are not feeling good")
				speak("I feel really sad that you are not feeling good")
				time.sleep(0.8)
			
				
				print("I wish ,you get well soon")
				speak("I wish ,you get well soon")
				b=listener()
				time.sleep(0.9)
				if b in dd:
					print("Mention not")
					speak("Mention not")
			elif a.lower()=="invalid":
				print("Sorry couldn't understand you ")
				speak("Sorry couldn't understand you ")
		elif s in ee:
			time.sleep(0.5)
			print("I am J.A.R.V.I.S , and what about you ? ")
			speak("I am jarvis , and what about you ? ")
			a=listener()
			if a.lower() in ff:
				time.sleep(0.4)
				print("I was a fictional A.I in IronMan's movie and was named J.A.R.V.I.S by Tony Stark")
				speak("I was a fictional AI in IronMan's movie and was named jarvis by Tony Stark")
				time.sleep(0.7)
				print("But currently I am being developed in reality by SAURAV")
				speak("But currently I am being developed in reality by SAURAV")
			else:
				if("I AM" in a.upper()):
					print("Nice to meet you", a[4:])
					speak("Nice to meet you {}".format(str(a[4:])))

				else:
					print("Nice to meet you",a)
					speak("Nice to meet you {}".format(a))

		elif s in ff:
			time.sleep(0.9)
			print("I was a fictional A.I in IronMan's movie and was named J.A.R.V.I.S by Tony Stark")
			speak("I was a fictional A.I in IronMan's movie and was named jarvis by Tony Stark")
		elif s in gg:
			time.sleep(0.6)
			print("I can talk with you")
			speak("I can talk with you")
			time.sleep(1)
			print("I can also set alarms for you and even timers")
			speak("I can also set alarms for you and even timers")
			time.sleep(0.8)
			print("you can also ask to calculate two no.s ,..like 'what is 3/8' or calculate 4*8 ")
			speak("you can also ask to calculate two numbers ,like what is 3 by 8 or calculate 4 into 8 ")
			time.sleep(0.9)
			print("wanna try?")
			speak("wanna try?")

			a=listener()
			if a.upper() in hh:
				time.sleep(0.5)
				print("alarm or timer or just say calculate 5+2")
				speak("alarm or timer or just say calculate 5+2")
				b=listener()
				if "TIMER" in b.upper():
					timer()
					
				elif "ALARM" in b.upper():
					alarm()
				elif "calculate" in b :
					print(calculator(b[9:]))
				elif "TALK" in b.upper():
					talk()
				
				else:
					time.sleep(0.8)
					print("I couldn't understand what you want")
					speak("I couldn't understand what you want")
			
			elif a.upper() in ii:
					time.sleep(0.8)
					print("Okay no problem, you can always do so  by saying set an alarm or timer")
					speak("Okay no problem, you can always do so  by saying set an alarm or timer")
					b=listener()
					if "TIMER" in b.upper():
						time.sleep(0.8)
						print("Here you go Sir")
						speak("Here you go Sir")
						time.sleep(0.7)
						timer()
					elif "ALARM" in b.upper():
						time.sleep(0.8)
						print("Here you are, sir")
						speak("Here you go Sir")
						time.sleep(0.7)
						alarm()
					elif "TALK" in b.upper():
						talk()
		elif s.upper() in jj:
					time.sleep(0.7)
					print("Hello sir, how may I help you")
					speak("Hello sir, how may I help you")
					a=listener()
					if a.upper() in kk:
						time.sleep(0.8)
						print("Okay no problem,  By the way I feel very happy to help ")
						speak("Okay no problem,  By the way I feel very happy to help ")
					elif  "TIMER" in a.upper():
						time.sleep(0.6)
						print("Here you go sir")
						speak("Here you go sir")
						time.sleep(0.9)
						timer()
					elif("ALARM" in a.upper()):
						time.sleep(0.6)
						print("Sure sir")
						speak("Sure sir")
						time.sleep(0.9)
						alarm()
					elif "TALK" in a.upper():
						time.sleep(0.4)
						print("I can talk but not for a long time since I am under development")
						speak("I can talk but not for a long time since I am under development")
						
						talk()
					elif "CALCULATE" in a.upper():
						print(calculator(a[9:]))
						speak(str(calculator(a[9:])))
					elif "WHAT IS " in a.upper() and a[-1]. isdigit():
						print(calculator(a[8:]))
						speak(str(calculator(a[8:])))
					elif "PLAY" in a.upper() or "BORED" in a.upper():
						time.sleep(0.5)
						print("Okay , here's a math quiz for you")
						speak("Okay , here's a math quiz for you")
						mathgame()
					
					else:
						time.sleep(0.7)
						print("You said something which I can't understand")
						speak("You said something which I can't understand")
		elif s.upper() in ll:
			time.sleep(0.5)
			print("You are welcome , sir")
			speak("You are welcome , sir")
			time.sleep(0.5)
			print("I feel very happy to be able to serve you")
			speak("I feel very happy to be able to serve you")
		elif s.upper() in mm:
			time.sleep(0.5)
			print("I felt really very sad about it...... but I am trying to improve")
			speak("I felt really very sad about it. but I am trying to improve")
		elif "CALCULATE" in s.upper():
			print(calculator(s[9:]))
		elif s[8:9].isdigit() and s[-1].isdigit():#checks for what is 4+5 type statements
			print(calculator(s[8:]))
		
		elif s.upper() in nn:
			time.sleep(0.3)
			print("Today is", ctime())
			speak("Today is {}".format(str(ctime())))
		
		elif "PLAY GAME" in s.upper() or "PLAY A GAME" in s.upper():
			mathgame()
		elif s.upper() in oo:
			time.sleep(0.5)
			print("would you like to play a game with me ?")
			a=input(".")
			if a.upper() in hh or "OK" in a.upper():
				mathgame()
			elif a.upper in ii or "NO" in a.upper():
				time.sleep(0.7)
				print("okay , whenever you want you can come back")
			else:
				time.sleep(0.4)
				print("I didn't understand what you said")
					 	
					 	
		elif "TALK" in s.upper():
				time.sleep(0.5)
				talk()
					 	
		elif "ALARM" in s.upper():
				alarm()
		elif "TIMER" in s.upper():
			 	timer()
					 	
					 		
					 	
					 	
					 
					 
			 
					 
					 			
		    
				
					 					 
					 					 
					 
						
					
					
				
			
			
			
			
		
				 
				 	
				 
				 	

				  

def timer():
	print("Timer :")
	speak("Say your timer value in seconds ")

	p=int(listener())
	if p=="invalid":
		speak("sorry couldn't get you ")
	print("timer :",p)
	k=0
	c=p
	
	while k<=p:
		k+=1
		
		
		time.sleep(1)
		print(c)
		
		c-=1
	print("Time completed", p," seconds")
	speak("Time completed {} seconds".format(p))
	

def alarm():
	print("hours : ")
	speak("hours  ")
	hu=listener()
	print(hu)
	print("minutes : ")
	speak("minutes  ")
	mu=listener()
	print(mu)
	print("seconds : ")
	speak("seconds  ")
	su=listener()
	print(su)
	while 1:
		if ctime()[11:13]==hu and ctime()[14:16]==mu and ctime()[17:19]==su:
			print("ALARM! !! .....",hu,":",mu,":",su)
			speak("alarm alarm , wake up , wake up , dude it's alraedy {},{}".format(hu,mu))
			break
		else:
			time.sleep(1)
			print(ctime()[17:19])
      
       
       



def calculator(a):	
	res=0
	c=0
	for j in a:
			if j=='*':
				res=float(a[0:c])
				res*=float(a[c+1:])
				return res
			elif j=='/':
				res=float(a[0:c])
				res/=float(a[c+1:])
				return res
			elif j=='+':
				res=float(a[0:c])
				res+=float(a[c+1:])
				return res
			elif j=='-':
				res=float(a[0:c])
				res-=float(a[c+1:])
				return res
			c+=1


def mathgame():
	time.sleep(0.5)
	print("This is a maths game")
	time.sleep(0.5)
	print("Do you want to know the instructions, if yes press yes else just press enter")
	x=input("?")
	if "YES" in x.upper():
		time.sleep(0.7)
		print("Instructions :")
		print("you have to do mathematical calculation with two no.s (÷ × + - )")
		print("you have to answer total of 5 questions")
		print("you will get one point for each correct")
		print("you will get exactly 7 seconds for each to answer :")
	time.sleep(0.7)
	print()
	print()
	print("Now press ENTER TO START")
	a=input()
	c=0
	z=1
	p=0
	t=int(ctime()[17:19])
	while(z<=5 ):
		n1=randint(1,20)
		n2=randint(1,20)
		d1=randrange(5,100,5)
		d2=randrange(5,100,5)
		k=randint(1,4)
		time.sleep(0.4)
		print("Question : ",z)
		z+=1
		time.sleep(0.4)
		if k==1:
			print("What is",d1,"÷",d2)
			r=d1/d2
		elif k==2:
			print("what is",n1,"×",n2)
			r=n1*n2
		elif k==3:
			print("what is",n1,"+",n2)
			r=n1+n2
		else:
			print("what is",n1,"-",n2)
			r=n1-n2

		start=time.time()
		b=float(input("."))
		
		elapsed=time.time()-start
		if(elapsed<=7 and b==r):
				print("correct")
				c+=1
		elif(b!=r):
				print("Wrong")
		elif(elapsed>=7):
				print("Time's up")
		
	if(c>3):
		time.sleep(0.8)
		print("YOU WON")
		print("you are good at numbers")
		time.sleep(0.7)
		print("With a score of",c)
	elif(c<3):
		time.sleep(0.7)
		print("You lose, you need to work at your numerical ability")
		time.sleep(0.7)
		print("Score",c)
	else:
		time.sleep(0.7)
		print("just passed", "score :",c)
		
		
		


		
			
		
		
def talk():
			print("okay sir , first let me introduce myself, I am J.A.R.V.I.S , an AI ")
			speak("okay sir , first let me introduce myself, I am JARVIS , an AI ")

			time.sleep(0.5)
			print("What about you ?")
			
			speak("What about you ?")
			a=listener()
			if("I AM" in a.upper()):
				print("Nice to meet you", a[4:])
				speak("Nice to meet you {}".format(a[4:]))
			else:
				print("Nice to meet you",a)
				speak("Nice to meet you {}".format(a))
			
			
			time.sleep(0.7)
			print("What's your age ?")
			speak("What's your age ?")
			b=listener()
			if "MY AGE IS" in b.upper():
				time.sleep(0.5)
				age=int(b[10:12])
				print("Okay so yo are",age,"Years old")
				speak("Okay so yo are {} Years old".format(age))
			elif "I AM" in b.upper():
				age=int(b[5:7])
				time.sleep(0.6)
				print("So you are",age,"years old")
				speak("So you are {} years old".format(age))
			else:
				time.sleep(0.5)
				age=int(b)
				print("Okay so yo are",age,"Years old")
				speak("Okay so yo are {} Years old".format(age))
				
			if (age<=18 and age>= 13):
					time.sleep(0.5)
					print("Then you must be busy in your studies everyday, aren't' you?")
					speak("Then you must be busy in your studies everyday, aren't' you?")
					c=listener()
					if "YES" in c.upper() or "YEAH" in c.upper():
						time.sleep(0.6)
						print("Yes It is very important , you know how these days competitions are increasing ")
						speak("Yes It is very important , you know how these days competitions are increasing ")

						time.sleep(0.8)
						print("Okay, I think I shouldn't waste your time more, so I should leave now")
						speak("Okay, I think I shouldn't waste your time more, so I should leave now")
						
					else:
						time.sleep(0.8)
						print("Seriously, at your age you must be studying")
						speak("Seriously, at your age you must be studying")
						time.sleep(0.6)
						print("So go now and don't waste your time here")
						speak("So go now and don't waste your time here")
			if(age<=50 and age>18):
						time.sleep(0.5)
						print("Are you working ?")
						speak("Are you working ?")
						d=listener()
						if "YES" in d.upper() or "YEAH" in d.upper():
							time.sleep(0.6)
							print("Do you do business or a job ?")
							speak("Do you do business or a job ?")
							e=listener()
							if "JOB" in e.upper():
								time.sleep(0.5)
								print("Oh Job! , Bosses are always ready to tease you isn't it ?")
								speak("Oh Job! , Bosses are always ready to tease you isn't it ?")
								f=listener()
								if "YES" in f.upper() or "YEAH" in f.upper():
									time.sleep(0.6)
									print("Yes this is true in more than 98% cases, haha")
									speak("Yes this is true in more than 98% cases, haha")
									
								else:
									time.sleep(0.6)
									print("Then you are really a lucky man")
									speak("Then you are really a lucky man")
									time.sleep(0.8)
									print("ok goodbye")
									speak("ok goodbye")
							elif "BUSINESS" in e.upper() or "BUSINESSMAN" in e.upper():
								time.sleep(0.6)
								print("Wow , that's really cool, you are your own boss")
								speak("Wow , that's really cool, you are your own boss")
						elif "NO" in d.upper():
							time.sleep(0.6)
							print("You are not working, then you must be in college")
							speak("You are not working, then you must be in college")
							time.sleep(0.6)
							print("Okay, goodbye as of now")
							speak("Okay, goodbye as of now")
				
					  				  				  				  				  				  				  				   
time.sleep(0.2)  
print("LOADING....")  
time.sleep(0.1)
 
print("Welcome to this AI")
speak("welcome to this AI")				  				  				  				  				  				  				  				  				  				  				  				  				  				  				  				  
while 1:
	try:
		s=listener()
		if "hey jarvis" in s.lower():
			speak("hi saurav , give me a moment      ")
		if(s)=="invalid":
			continue
		check(s)
	except:
		print("oops, some error occured !!")
		speak("oops, some error occured !")

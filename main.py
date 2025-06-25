import pygame, random, sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

# QuestionAnswer
# used for containing a question and its answers
# to get a list of answers, use shuffled_answers
# to check if its correct, use check_answer
# to get a question, use QuestionAnswer.question

class QuestionAnswer:
	def __init__(self, Question, CorrectAnswer, IncorrectAnswer1, IncorrectAnswer2, IncorrectAnswer3):
		self.question = Question
		self.correct_answer = CorrectAnswer
		self.incorrect_answer1 = IncorrectAnswer1
		self.incorrect_answer2 = IncorrectAnswer2
		self.incorrect_answer3 = IncorrectAnswer3
		self.array = [self.correct_answer, self.incorrect_answer1, self.incorrect_answer2, self.incorrect_answer3]
		random.shuffle(self.array)

	def shuffled_answers(self):
		random.shuffle(self.array)
		return ([self.question] + self.array + [self.correct_answer])

class Button():
	def __init__(self, x, y, x_size, y_size, size, text, color_text, color_bg):
		self.font = pygame.font.SysFont('Cambria.ttf', size)
		self.lines = text.split('\n')
		self.text_color = color_text
		self.bg_color = color_bg
		self.x = x
		self.y = y
		self.x_size = x_size
		self.y_size = y_size
		self.size = size
		self.clicked_last_frame = False
		self.bg_rect = pygame.Rect(self.x - self.x_size/2, self.y, self.x_size, self.y_size)

	def change_text(self, text):
		self.lines = text.split('\n')

	def draw(self):
		action = False
		i = 0
		pos = pygame.mouse.get_pos()

		if self.bg_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked_last_frame == False:
				self.clicked_last_frame = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked_last_frame = False

		pygame.draw.rect(screen, self.bg_color, self.bg_rect)

		for line in self.lines:
			self.text = self.font.render(line, False, self.text_color, self.bg_color)
			self.rect = self.text.get_rect()
			self.rect.midtop = (self.x, self.y+10+self.size*i*0.75)
			
			screen.blit(self.text, self.rect)
			i+=1
		
		return action

start_button = Button(640, 300, 300, 100, 110, 'Play', (255,255,255), (0,0,0))
exit_button =  Button(640, 500, 300, 100, 110, 'Quit', (255,255,255), (0,0,0))

question1 = QuestionAnswer('\nWhen was the internet\nfirst created?', '\n\n1960s', '\n\n1950s', '\n\n1970s', '\n\n1980s')
question2 = QuestionAnswer('\nWhat was the first internet\'s name?', '\n\nARPANET', '\n\nInter-Net', '\n\nProject INN', '\n\nUSANet')
question3 = QuestionAnswer('\nIn which country was the first internet created in?', '\n\nUSA', '\n\nUSSR', '\n\nWest Germany', '\n\nUK')
question4 = QuestionAnswer('\nWhat was the first computer virus punished by law?', '\n\nMorris Worm', '\n\nChristmas Tree EXEC', '\n\nBrain', '\n\nCreeper')
question5 = QuestionAnswer('\nHow much damage did it cause?', '\n\n98 million $', '\n\n51 million $', '\n\n213 million $', '\n\n465 million $')
question6 = QuestionAnswer('\nWhat is a computer worm?', '\nSoftware which replicates itself\nand spreads to other devices.', '\nSoftware which hides itself\nby replacing\napplication components.', '\nSoftware which corrupts data\non the disk.', '\nSoftware, which once launched,\ncannot be removed from\nthe computer.')
question7 = QuestionAnswer('\nWhat is WannaCry?', '\n\nRansomware', '\n\nThe first ever Trojan Horse', '\n\nA trojan horse (not the first one)', '\nA bug in Windows 7 which\nallowed Remote Code Execution\n to be done.')
question8 = QuestionAnswer('\nWhat is ransomware?', '\nSoftware which encrypts all files\n on a computer and\n\'takes ransom\' of them.', '\n\nWares which are to be ransomed.', '\nData stolen during a hack which\nthe user has to pay back for.', '\nA hacker group that created\nthe first ever virus\nwhich \'took ransom\'\n of people\'s computers.')
question9 = QuestionAnswer('','','','','')

question = 0

question_arr = [[0,0]]

option1_button = Button(320, 250, 600, 220, 50, '', (255,255,255), (200,30,10))
option2_button = Button(320, 480, 600, 220, 50, '', (255,255,255), (30,200,10))
option3_button = Button(960, 250, 600, 220, 50, '', (255,255,255), (50,10,240))
option4_button = Button(960, 480, 600, 220, 50, '', (255,255,255), (190,170,20))

points = 0

points_button  = Button(640,   0,   60, 40, 25, str(points) + '/' + str(question), (255,255,255), (0,0,0))

quiz_button    = Button(640,  40, 1240,200, 50, '', (255,255,255), (30,160,200))

points_endscreen_button = Button(640, 150, 225, 100, 110, str(points) + '/' + str(question), (255,255,255), (100,100,120))

your_final_score_button = Button(640, 50, 715, 100, 110, "Your final score is:", (255,255,255), (70,10,5))

play_again_button = Button(640, 350, 500, 100, 110, "Play Again?", (255,255,255), (0,0,0))

quit_endscreen_button = Button(640, 550, 200, 100, 110, "Quit", (255,255,255), (0,0,0))

section = "start"


while running:
	
	screen.fill('#F2E3CC')

	if(section == "start"):


		if start_button.draw():
			question_arr = [question1.shuffled_answers(),question2.shuffled_answers(),question3.shuffled_answers(),question4.shuffled_answers(),question5.shuffled_answers(),question6.shuffled_answers(),question7.shuffled_answers(),question8.shuffled_answers(),question1.shuffled_answers(),question1.shuffled_answers(),question1.shuffled_answers(),question1.shuffled_answers(),question1.shuffled_answers(),question1.shuffled_answers(),question1.shuffled_answers()]
			question = 0
			points = 0
			start_button_clicked = True
			section = "quiz"


		if exit_button.draw():
			running = False

	if(section == "quiz"):
		points_button.change_text(str(points) + '/' + str(question))

		quiz_button.change_text(question_arr[question][0])

		option1_button.change_text(question_arr[question][1])
		option2_button.change_text(question_arr[question][2])
		option3_button.change_text(question_arr[question][3])
		option4_button.change_text(question_arr[question][4])
		
		quiz_button.draw()
		points_button.draw()
		if(option1_button.draw() and start_button_clicked == False):
			if(question_arr[question][1] == question_arr[question][5]):
				points += 1
			question += 1

		if(option2_button.draw() and start_button_clicked == False):
			if(question_arr[question][2] == question_arr[question][5]):
				points += 1
			question += 1

		if(option3_button.draw() and start_button_clicked == False):
			if(question_arr[question][3] == question_arr[question][5]):
				points += 1
			question += 1

		if(option4_button.draw() and start_button_clicked == False):
			if(question_arr[question][4] == question_arr[question][5]):
				points += 1
			question += 1
		
		if(question == len(question_arr)):
			question = len(question_arr) 
			points_endscreen_button.change_text(str(points) + '/' + str(question))
			last_question_click = True
			section = "endscreen"

		start_button_clicked = False

	if(section == "endscreen"):
		points_endscreen_button.draw()
		your_final_score_button.draw()
		if(play_again_button.draw() and last_question_click == False):
			question = 0
			points = 0
			start_button_clicked = True
			section = "quiz"

		if(quit_endscreen_button.draw() and last_question_click == False):
			running = False

		last_question_click = False
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.update()

pygame.quit()

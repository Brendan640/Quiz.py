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

start_button = Button(640, 300, 100, 50, 50, 'start', (255,255,255), (0,0,0))
exit_button =  Button(640, 500, 100, 50, 50, 'exit', (255,255,255), (0,0,0))

question1 = QuestionAnswer('\nWhen was the internet\nfirst created?', '\n\n1960s', '\n\n1950s', '\n\n1970s', '\n\n1980s')

question = 0

question_arr = [question1.shuffled_answers()]

option1_button = Button(320, 250, 600, 220, 50, question_arr[question][1], (255,255,255), (200,30,10))
option2_button = Button(320, 480, 600, 220, 50, question_arr[question][2], (255,255,255), (30,200,10))
option3_button = Button(960, 250, 600, 220, 50, question_arr[question][3], (255,255,255), (50,10,240))
option4_button = Button(960, 480, 600, 220, 50, question_arr[question][4], (255,255,255), (190,170,20))

points = 0

points_button  = Button(640,   0,   50, 40, 25, str(points) + '/' + str(question), (255,255,255), (0,0,0))

quiz_button    = Button(640,  40, 1240,200, 50, question_arr[question][0], (255,255,255), (30,160,200))

section = "start"

while running:
	
	screen.fill('#F2E3CC')

	if(section == "start"):


		if start_button.draw():
			question = 0
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

		if(option1_button.draw()):
			if(question_arr[question][1] == question_arr[question][5]):
				print("Test 1")

		if(option2_button.draw()):
			if(question_arr[question][2] == question_arr[question][5]):
				print("Test 2")

		if(option3_button.draw()):
			if(question_arr[question][3] == question_arr[question][5]):
				print("Test 3")

		if(option4_button.draw()):
			if(question_arr[question][4] == question_arr[question][5]):
				print("Test 4")
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.update()

pygame.quit()

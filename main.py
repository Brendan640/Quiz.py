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
		self.incorrect_answer_1 = IncorrectAnswer1
		self.incorrect_answer_2 = IncorrectAnswer2
		self.incorrect_answer_3 = IncorrectAnswer3

	def shuffled_answers(self):
		return random.shuffle([self.correct_answer, self.incorrect_answer_1, self.incorrect_answer_2, self.incorrect_answer_3])

	def check_answer(self, answer):
		if(answer == self.correct_answer):
			return True
		else:
			return False

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
		self.clicked = False
		self.bg_rect = pygame.Rect(self.x - self.x_size/2, self.y, self.x_size, self.y_size)

	def draw(self):
		action = False
		i = 0
		pos = pygame.mouse.get_pos()

		pygame.draw.rect(screen, self.bg_color, self.bg_rect)

		if self.bg_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		for line in self.lines:
			self.text = self.font.render(line, False, self.text_color, self.bg_color)
			self.rect = self.text.get_rect()
			self.rect.midtop = (self.x, self.y+10+self.size*i*0.75)
			
			screen.blit(self.text, self.rect)
			i+=1
		
		return action

start_button = Button(640, 300, 100, 50, 50, 'start', (255,255,255), (0,0,0))
exit_button =  Button(640, 500, 100, 50, 50, 'exit', (255,255,255), (0,0,0))

while running:

	screen.fill('#F2E3CC')

	if start_button.draw():
		print('Start')


	if exit_button.draw():
		running = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.update()

pygame.quit()

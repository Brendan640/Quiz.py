import pygame, random, sys

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

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

class Button():
	def __init__(self, x, y, size, text, color_text, color_bg):
		self.font = pygame.font.Font('freesansbold.ttf', size)
		self.text = self.font.render(text, True, color_text, color_bg)
		self.rect = self.text.get_rect()
		self.rect.midtop = (x, y)
		self.clicked = False

	def draw(self):
		action = False

		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		screen.blit(self.text, self.rect)

		return action

start_button = Button(640, 300, 50, 'start', (255,255,255), (0,0,0))
exit_button = Button(640, 400, 50, 'exit', (255,255,255), (0,0,0))

running = True
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

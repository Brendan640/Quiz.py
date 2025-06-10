import pygame, random

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

while running:
	for event in pygame.event.get(): # get all events
		if event.type == pygame.QUIT: # stop running if event is quit
			running = False

	screen.fill("blue") # set bg to blue
	pygame.display.flip() # render

pygame.quit()

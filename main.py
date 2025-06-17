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

start_img = pygame.image.load('img/start_button.png').convert_alpha()
exit_img = pygame.image.load('img/quit_button.png').convert_alpha()



class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height* scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
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

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


start_button = Button(500, 200, start_img, 0.8)
exit_button = Button(500, 300, exit_img, 0.8)

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
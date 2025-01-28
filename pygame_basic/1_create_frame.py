import pygame

pygame.init() #초기화

screen_width = 480 # 화면 크기(가로)
screen_height = 640 # 화면 크기(세로)

screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임명

#이벤트 루프
running = True #게임이 진행중인가?
while running:
  for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
    if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
      running = False

pygame.quit() #pygame 종료
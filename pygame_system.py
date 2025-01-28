import pygame #pygame 모듈 임포트
import sys    #sys 모듈 임포트

WHITE = (255,255,255) # 색 정의: 하양
BLACK = (0,0,0)      # 색 정의: 검정

#메인 처리 수행 함수 정의
def main(): 
    pygame.init() #pygame 모듈 초기화
    pygame.display.set_caption("첫번째 Pygame") #윈도우에 표시할 타이틀 지정
    screen = pygame.display.set_mode((800,600)) #그릴 화면(screen) 초기화
    clock = pygame.time.Clock() #clock 오브젝트 초기화
    font = pygame.font.Font(None,80) #font 오브젝트 초기화
    tmr = 0
#무한 반복
    while True: 
        tmr = tmr + 1 #tmr 값 1 증가
        for event in pygame.event.get(): #pygame 이벤트 반복 처리
            if event.type == pygame.QUIT: #윈도우의 'X'버튼을 누른 경우
                pygame.quit() #pygame 모듈 초기화 해제
                sys.exit() #프로그램 종료

        txt = font.render(str(tmr),True,WHITE) #Surface에 문자열 표시
        screen.fill(BLACK) #지정한 색으로 스크린 전체 채움
        screen.blit(txt,[300,200]) #문자열 표시한 Surface를 스크린으로 전송
        pygame.display.update() #화면 업데이트
        clock.tick(10)

if __name__ == '__main__': #이 프로그램 직접 실행 시

    main() #main()함수 호출

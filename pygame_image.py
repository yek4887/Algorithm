import pygame  # pygame 모듈 임포트
import sys     # sys 모듈 임포트

def main():
    pygame.init()  # pygame 모듈 초기화
    pygame.display.set_caption("첫번째 Pygame: 이미지 표시")  # 윈도우 제목 지정
    screen = pygame.display.set_mode((640, 360))  # 그릴 화면(screen) 초기화
    clock = pygame.time.Clock()  # clock 오브젝트 초기화
    
    # 이미지 로드
    img_bg = pygame.image.load("pg_bg.png")
    img_chara = [
        pygame.image.load("pg_char0.png"),
        pygame.image.load("pg_char1.png"),
    ]
    
    tmr = 0

    while True:
        tmr += 1  # 타이머 1 증가
        for event in pygame.event.get():  # 이벤트 처리
            if event.type == pygame.QUIT:  # 윈도우 종료 이벤트 처리
                pygame.quit()
                sys.exit()  # 프로그램 종료
            
            if event.type == pygame.KEYDOWN:  # 키를 눌렀을 때 이벤트 처리
                if event.key == pygame.K_F1:  # F1키라면
                    screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN)  # 풀스크린 모드
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:  # F2나 ESC 키라면
                    screen = pygame.display.set_mode((640, 360))  # 일반 스크린 모드

        x = tmr % 160  # 배경이 왼쪽으로 움직이도록 x 값 계산
        
        # 배경을 화면에 반복적으로 그리기
        for i in range(5):
            screen.blit(img_bg, [i * 160 - x, 0])
        
        # 캐릭터 이미지 표시
        screen.blit(img_chara[tmr % 2], [224, 160])
        
        pygame.display.update()  # 화면 업데이트
        clock.tick(5)  # 초당 5번으로 속도 제한

if __name__ == '__main__':
    main()

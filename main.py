import pygame
import chess
import chess.engine
import asyncio


pygame.init()

DISPLAY_WIDTH, DISPLAY_HEIGHT = 800, 600
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

########################################classes here########################################





############################################################################################

BLACK = (0,0,0)
WHITE = (255,255,255)
CHARCOAL = (30,30,36)

RED = (200,0,0)
GREEN = (0,200,0)
YELLOW = (255,255,0)

BRIGHT_RED = (255,0,0)
BRIGHT_GREEN = (0,255,0)
LIGHT_YELLOW = (255,255,51)
NEON_YELLOW = (255,221,0)

AQUA = (0, 128, 128)
GRAY = (190, 190, 190)

MAIN_MENU, LEVEL1, PAUSE, SCOREBOARD = "main_menu","level1","pause","scoreboard"
current_state = MAIN_MENU

def text_objects(text,font,colour):
    return font.render(text,True,colour), font.render(text,True,colour).get_rect()

def draw_text(text,size,x,y,colour):
    font=pygame.font.SysFont("twcen",size)
    surf,rect=text_objects(text,font,colour)
    rect.center=(x,y)
    gameDisplay.blit(surf,rect)

def button(text,x,y,w,h,ic,ac,colour):
    mx,my=pygame.mouse.get_pos()
    hover = x<=mx<=x+w and y<=my<=y+h
    pygame.draw.rect(gameDisplay,ac if hover else ic,(x,y,w,h))
    font=pygame.font.SysFont("twcen",20)
    surf,rect=text_objects(text,font,colour)
    rect.center=(x+w/2,y+h/2)
    gameDisplay.blit(surf,rect)
    return hover

running=True

while running:
    clicked=False

    for event in pygame.event.get():
        if event.type==pygame.QUIT: running=False
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1: clicked=True

    if current_state==MAIN_MENU:

        ################################# main menu stuff here##################################################
        gameDisplay.fill(BLACK)
        draw_text("CHESS",50,DISPLAY_WIDTH/2,120,RED)
        if button("PLAY",340,250,120,50,RED,WHITE,BLACK) and clicked: current_state=LEVEL1
        if button("QUIT",340,350,120,50,RED,WHITE,BLACK) and clicked: running=False

    elif current_state==LEVEL1:

        ###################################gamew play here##########################################################
        gameDisplay.fill(BLACK)
        async def main() -> None:
            transport, engine = await chess.engine.popen_uci(r"C:\Users\sy252556\OneDrive - Xaverian College\David Law's files - TAHMASBI, Aidan\NEA Program\stockfish\stockfish-windows-x86-64-avx2.exe")

            board = chess.Board()
            while not board.is_game_over():
                result = await engine.play(board, chess.engine.Limit(time=0.1))
                board.push(result.move)

            await engine.quit()

        asyncio.run(main())
        if button("PAUSE",20,20,120,50,RED,WHITE,BLACK) and clicked: current_state=PAUSE
        if button("END",620,20,150,50,RED,WHITE,BLACK) and clicked: current_state=SCOREBOARD

    elif current_state==PAUSE:

        
        gameDisplay.fill(BLACK)
        draw_text("PAUSED",50,DISPLAY_WIDTH/2,120,RED)
        if button("RESUME",250,400,120,50,RED,WHITE,BLACK) and clicked: current_state=LEVEL1
        if button("MENU",430,400,120,50,RED,WHITE,BLACK) and clicked: current_state=MAIN_MENU

    elif current_state==SCOREBOARD:
        gameDisplay.fill(BLACK)
        if button("REPLAY",250,400,140,50,RED,WHITE,BLACK) and clicked: current_state=LEVEL1
        if button("MENU",430,400,120,50,RED,WHITE,BLACK) and clicked: current_state=MAIN_MENU

    pygame.display.update()
    clock.tick(60)

pygame.quit()
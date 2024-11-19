import asyncio    #これが必須の奴
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((320, 240))
clock = pygame.time.Clock()
# 日本語フォントの読み込み
font_path = "NotoSansJP-VariableFont_wght.ttf"  # フォントファイルのパス
font_size = 32
font = pygame.font.Font(font_path, font_size)
text = font.render('pygameブラウザ版', True, (0, 0, 255))

async def main():    #これが必須の奴
    x, y = 50, 50
    while True:
        screen.fill((0, 255, 0))
        screen.blit(text, (30, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
            if event.type == pygame.KEYDOWN:
                x += 5
            if event.type == pygame.MOUSEBUTTONDOWN:
                y += 5
        pygame.draw.rect(screen, ((255, 0, 0)), (x, y, 20, 20))
        pygame.display.update()
        clock.tick(30)
        await asyncio.sleep(0)    #これが必須の奴

asyncio.run(main())    #これが必須の奴

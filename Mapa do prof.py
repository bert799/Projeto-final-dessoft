# Estabelece a pasta que contem as figuras e sons.
import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
TITULO = 'Teste de nível'
WIDTH = 640
HEIGHT = 480
FPS = 60
TILE_IMG = 'tile_img'
BACKGROUND_IMG = 'background_img'

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define a velocidade do mundo, por camadas (temos 6 camadas)
world_speeds = [-1, -2, -3, -5, -7, -1]

TILE_SIZE = 32

EMPTY = -1
BLOCK1 = 'BLOCK1' # Top edge Right
BLOCK2 = 'BLOCK2' # Top block
BLOCK3 = 'BLOCK3' # Top edge left
BLOCK4 = 'BLOCK4' # interior top edge left
BLOCK5 = 'BLOCK5' # interior top midsection
BLOCK6 = 'BLOCK6' # Interior top edge right
PLATF1 = 'BLOCK7' # Plataform edge left
PLATF2 = 'BLOCK8' # Plataform midsection
PLATF3 = 'BLOCK9' # Plataform edge right
BLOCK10 = 'BLOCK10' # Ice block 1 
BLOCK11 = 'BLOCK11' # mid edge left
BLOCK12 = 'BLOCK12' # earth
BLOCK13 = 'BLOCK13' # mid edge right
BLOCK14 = 'BLOCK14' # interior verde
BLOCK15 = 'BLOCK15' # mid edge left
BLOCK16 = 'BLOCK16' # 
BLOCK17 = 'BLOCK17' # 
BLOCK18 = 'BLOCK18' # 
BLOCK19 = 'BLOCK19' # 
BLOCK20 = 'BLOCK20' # Ice block 2
BLOCK21 = 'BLOCK21' # 
BLOCK22 = 'BLOCK22' # 
BLOCK23 = 'BLOCK23' # 
BLOCK24 = 'BLOCK24' # 
BLOCK25 = 'BLOCK25' # 
BLOCK26 = 'BLOCK26' # 
BLOCK27 = 'BLOCK27' # 
BLOCK28 = 'BLOCK28' # 
BLOCK29 = 'BLOCK29' # 
BLOCK30 = 'BLOCK30' # Ice Block 3
BLOCK31 = 'BLOCK31' # 
BLOCK32 = 'BLOCK32' # 
BLOCK33 = 'BLOCK33' # 
BLOCK34 = 'BLOCK34' # 
BLOCK35 = 'BLOCK35' # 
BLOCK36 = 'BLOCK36' # 
BLOCK37 = 'BLOCK37' # 
BLOCK38 = 'BLOCK38' # 
BLOCK39 = 'BLOCK39' # 
BLOCK40 = 'BLOCK40' # Ice Block 4
BLOCK41 = 'BLOCK41' #
BLOCK42 = 'BLOCK42' # 
BLOCK43 = 'BLOCK43' #
BLOCK44 = 'BLOCK44' # 
BLOCK45 = 'BLOCK45' #
BLOCK46 = 'BLOCK46' # 
BLOCK47 = 'BLOCK47' #
BLOCK48 = 'BLOCK48' # 
BLOCK49 = 'BLOCK49' #
BLOCK50 = 'BLOCK50' # Ice Block 5
BLOCK51 = 'BLOCK51' # 
BLOCK52 = 'BLOCK52' # 
BLOCK53 = 'BLOCK53' # 
BLOCK54 = 'BLOCK54' # 
BLOCK55 = 'BLOCK55' # 
BLOCK56 = 'BLOCK56' # 
BLOCK57 = 'BLOCK57' # 
BLOCK58 = 'BLOCK58' # 
BLOCK59 = 'BLOCK59' # 
BLOCK60 = 'BLOCK60' # 


TILE_MAP = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, BLOCK1, BLOCK2, BLOCK3, BLOCK4, BLOCK5, BLOCK6, PLATF1, PLATF2, PLATF3, BLOCK10, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, BLOCK11, BLOCK12, BLOCK13, BLOCK14, BLOCK15, BLOCK16, BLOCK17, BLOCK18, BLOCK19, BLOCK20, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, BLOCK21, BLOCK22, BLOCK23, BLOCK24, BLOCK25, BLOCK26, BLOCK27, BLOCK28, BLOCK29, BLOCK30, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, BLOCK31, BLOCK32, BLOCK33, BLOCK34, BLOCK35, BLOCK36, BLOCK37, BLOCK38, BLOCK39, BLOCK40, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, BLOCK41, BLOCK42, BLOCK43, BLOCK44, BLOCK45, BLOCK46, BLOCK47, BLOCK48, BLOCK49, BLOCK50, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, BLOCK51, BLOCK52, BLOCK53, BLOCK54, BLOCK55, BLOCK56, BLOCK57, BLOCK58, BLOCK59, BLOCK60, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
]

MAP2 = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK1, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK3, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK11, BLOCK12, BLOCK12, BLOCK12, BLOCK12, BLOCK12, BLOCK13, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK11, BLOCK4, BLOCK22, BLOCK22, BLOCK22, BLOCK22, BLOCK23, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK11, BLOCK14, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, PLATF1, PLATF2, PLATF3, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK11, BLOCK14, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK11, BLOCK24, BLOCK25, BLOCK25, BLOCK25, BLOCK25, BLOCK25, BLOCK3, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK11, BLOCK12, BLOCK12, BLOCK12, BLOCK12, BLOCK12, BLOCK12, BLOCK13, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK21, BLOCK22, BLOCK22, BLOCK22, BLOCK22, BLOCK22, BLOCK22, BLOCK23, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
]

MAP3 = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, BLOCK31, BLOCK31, BLOCK31, PLATF2, PLATF2, BLOCK31, BLOCK31, BLOCK31, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, PLATF2, PLATF2, PLATF2, PLATF2, PLATF2, PLATF2, PLATF2, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, PLATF2, PLATF2, PLATF2, PLATF2, PLATF2, PLATF2, PLATF2, PLATF2, EMPTY, EMPTY, EMPTY],
    [BLOCK31, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK31, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK31],
    [EMPTY, EMPTY, BLOCK31, EMPTY, BLOCK31, BLOCK31, BLOCK31, BLOCK31, EMPTY, BLOCK31, BLOCK31, BLOCK31],
    [BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31],
    [BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31, BLOCK31],
]

# Tile set
class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, row, column):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))

        # Define a imagem do tile.
        self.image = tile_img
        self.image.set_colorkey(BLACK)
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row

# Separa uma tile sheet nos blocos e já os nomeia.
def load_tilesheet(tilesheet, rows, columns):
    tile_width = tilesheet.get_width() // columns
    tile_height = tilesheet.get_height() // rows
    sheet_size = tilesheet.get_width() * tilesheet.get_height()

    # adiciona em um dicionario
    tiles = {}
    i = 1 
    for row in range(rows):
        for column in range(columns):
            x = column * tile_width
            y = row * tile_height
            dest_rect = pygame.Rect(x, y, tile_width, tile_height)
            image = pygame.Surface((tile_width, tile_height))
            image.blit(tilesheet, (0, 0), dest_rect)
            tile_name = 'BLOCK{0}'.format(i)
            tiles[tile_name] = image 
            i += 1
    print(sheet_size)
    return tiles

def load_assets(img_dir):
    assets = {}
    tile_sheet  = pygame.image.load(path.join(img_dir, 'Tileset.png')).convert()
    tile_dict =  load_tilesheet(tile_sheet, 6, 10)
    for block, image in tile_dict.items():
        assets[block] = image
    assets[BACKGROUND_IMG] = []
    for i in range(1, 6):
        background = pygame.image.load(path.join(img_dir, 'background-{0}.png'.format(i))).convert_alpha()
        # Redimensiona o fundo
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        assets[BACKGROUND_IMG].append(background)
    return assets

def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Carrega o fundo do jogo
    backgrounds = assets[BACKGROUND_IMG]
    background_rects = []
    for background in backgrounds:
        background_rects.append(background.get_rect())

    all_sprites = pygame.sprite.Group()
    blocks = pygame.sprite.Group()

    # Cria tiles de acordo com o mapa
    for row in range(len(MAP3)):
        for column in range(len(MAP3[row])):
            tile_type = MAP3[row][column]
            if tile_type != EMPTY:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                blocks.add(tile)
    print(MAP3[0])
    PLAYING = 0
    DONE = 1

    state = PLAYING
    while state != DONE:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE

        # Atualiza a posição de cada camada do fundo e desenha
        for i in range(len(backgrounds)):
            world_speed = world_speeds[i]
            background = backgrounds[i]
            background_rect = background_rects[i]

            # Atualiza a posição da imagem de fundo.
            background_rect.x += world_speed
            # Se o fundo saiu da janela, faz ele voltar para dentro.
            if background_rect.right < 0:
                background_rect.x += background_rect.width
            # Desenha o fundo e uma cópia para a direita.
            # Assumimos que a imagem selecionada ocupa pelo menos o tamanho da janela.
            # Além disso, ela deve ser cíclica, ou seja, o lado esquerdo deve ser continuação do direito.
            screen.blit(background, background_rect)
            # Desenhamos a imagem novamente, mas deslocada da largura da imagem em x.
            background_rect2 = background_rect.copy()
            background_rect2.x += background_rect2.width
            screen.blit(background, background_rect2)

        all_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


# Inicialização do Pygame.
pygame.init()


# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption(TITULO)

# Imprime instruções
print('*' * len(TITULO))
print(TITULO.upper())
print('*' * len(TITULO))
print('Esse exemplo não é interativo.')

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
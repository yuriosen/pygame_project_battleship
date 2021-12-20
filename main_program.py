import pygame


SPACE_PRESS_COUNT = 0


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        colors = [pygame.Color(0, 0, 0), pygame.Color(0, 255, 0)]
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (x * self.cell_size + self.left,
                                  y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)
                pygame.draw.rect(screen, colors[self.board[y][x]], (x * self.cell_size + self.left + 1,
                                                                    y * self.cell_size + self.top + 1,
                                                                    self.cell_size - 2, self.cell_size - 2))

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y
        return None

    def on_click(self, cell_coords):
        self.board[cell_coords[1]][cell_coords[0]] = 1 - self.board[cell_coords[1]][cell_coords[0]]

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


def draw(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Морской бой", True, (0, 255, 255))
    # нужно будет написать здесь правила игры (думаю, это можно из ТЗ скопировать)
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 10 - text.get_height() // 10
    screen.blit(text, (text_x, text_y))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Касаева Яна; Цыганова Виктория")
    draw(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) and SPACE_PRESS_COUNT == 0:
                SPACE_PRESS_COUNT += 1
                screen.fill('black')
                board1 = Board(10, 10)
                board1.set_view(45, 85, 35)
                board1.render(screen)
                board2 = Board(10, 10)
                board2.set_view(440, 85, 35)
                board2.render(screen)
                # по краям расположить буквы и цифры; наверху - player1, player2
        pygame.display.flip()
    pygame.quit()


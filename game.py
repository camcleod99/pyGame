import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy


class Game:

    def __init__(self):
        self.act_player = None
        self.sys_running = True
        self.vid_size = (800, 800)
        self.sys_color_white = (255, 255, 255)
        self.sys_clock_rate = 120
        self.sys_window = pygame.display.set_mode(self.vid_size)
        self.sys_clock = pygame.time.Clock()
        self.tro_enemies = []
        self.var_level = 1
        self.var_reset = False

        ast_background = pygame.image.load('assets/background.png')
        self.vid_scale = (self.vid_size[0] / ast_background.get_width(), self.vid_size[1] / ast_background.get_height())

        self.obj_background = GameObject(0, 0, self.vid_size[0], self.vid_size[1], 'assets/background.png', None)
        self.obj_treasure = GameObject(382, 114, 14, 12, 'assets/treasure.png', self.vid_scale)
        self.init_actors()

    def init_actors(self):
        self.act_player = Player(375, 700, 12, 16, 'assets/player.png', self.vid_scale, 5, 0, 'x')
        self.tro_enemies = [
            Enemy(100, 500, 16, 12, 'assets/enemy.png', self.vid_scale, 5, 1, 'y', 1),
            Enemy(700, 350, 16, 12, 'assets/enemy.png', self.vid_scale, 5, 2, 'y', 3),
            Enemy(100, 200, 16, 12, 'assets/enemy.png', self.vid_scale, 5, 3, 'y', 5),
        ]

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.sys_running = False
            elif event.type == pygame.KEYDOWN:
                self.act_player.setDirection(event.key)
            elif event.type == pygame.KEYUP:
                self.act_player.resetDirection()

    def control_logic(self):
        self.act_player.move(self.vid_size[0])
        for act_enemy in self.tro_enemies:
            if act_enemy.level <= self.var_level:
                act_enemy.move(self.vid_size[0])

    def draw_objects(self):
        # Static Objects
        self.sys_window.fill(self.sys_color_white)
        self.sys_window.blit(self.obj_background.image, (self.obj_background.x, self.obj_background.y))
        self.sys_window.blit(self.obj_treasure.image, (self.obj_treasure.x, self.obj_treasure.y))
        # Moving Objects
        self.sys_window.blit(self.act_player.image, (self.act_player.x, self.act_player.y))
        for act_enemy in self.tro_enemies:
            if act_enemy.level <= self.var_level:
                self.sys_window.blit(act_enemy.image, (act_enemy.x, act_enemy.y))
        pygame.display.update()

    @staticmethod
    def detect_collision(object_a, object_b):
        if object_a.y > (object_b.y + object_b.height):
            return False
        elif (object_a.y + object_a.height) < object_b.y:
            return False
        if object_a.x > (object_b.x + object_b.width):
            return False
        elif (object_a.x + object_a.width) < object_b.x:
            return False
        return True

    def check_collision(self):
        for act_enemy in self.tro_enemies:
            if (act_enemy.level <= self.var_level) and self.detect_collision(self.act_player, act_enemy):
                self.var_level = 1
                self.var_reset = True
                return
        if self.detect_collision(self.act_player, self.obj_treasure):
            self.var_level += 1
            self.var_reset = True
        return

    def reset_board(self):
        if not self.var_reset:
            return
        else:
            self.init_actors()
            return

    def run_game_loop(self):
        while self.sys_running:
            self.handle_events()
            self.control_logic()
            self.draw_objects()
            self.check_collision()
            self.reset_board()
            self.var_reset = False
            self.sys_clock.tick(self.sys_clock_rate)

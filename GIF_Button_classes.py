import pygame


# Definition of our first class!!
class Button:
    """To create a button."""

    def __init__(self, the_image, pos, text_input, font, base_color, hovering_color):
        """Initializes the parameters of the button (image, position, text, font, color and color when the mouse is
        matching the position)."""

        super().__init__()

        # The image for the background of the button:
        self.image = the_image

        # The coordinates of the button:
        self.x_pos = pos[0]
        self.y_pos = pos[1]

        # Determine the font which will be used for the text:
        self.font = font

        # Determine the natural color of the text
        self.base_color = base_color
        # Determine the modified color of the text when the coordinates of the mouse will match the coordinates
        # of the button:
        self.hovering_color = hovering_color

        # Text to insert in the button:
        self.text_input = text_input
        # Apply the color to the text:
        self.text = self.font.render(self.text_input, True, self.base_color)

        # If we don't want to insert an image in the button (only clickable text):
        if self.image is None:
            self.image = self.text

        # Create the rectangle around the image with four parameters : the coordinates x and y, the width and the
        # height.
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def check_for_input(self, position):
        """Returns True if the user clicked on the rectangle covering the surface of the button.
        In brief, allows two make the connection between the button and the linked menu."""

        # The function is called once the 'click' of the user has already been detected.
        # If the coordinates of the 'click' are in the surface covered by the button, it sends the user to the game,
        # the game mode menu, or closes the library and the game.
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    def change_button_color(self, position):
        """Changes the color of the text if the mouse is over the button."""

        # Either the coordinates of the button's rectangle match the position of the mouse.
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        # Either it doesn't and the color of the text remains the same.
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def update(self, surface):
        """Updates the displayed button."""
        # If an image is provided :
        if self.image is not None:
            surface.blit(self.image, self.rect)
        # Update the text
        surface.blit(self.text, self.text_rect)


# Flower class
class Flower(pygame.sprite.Sprite):
    """To animate the flower."""

    def __init__(self, pos_x, pos_y):
        """Initialize the array with the flower's sprites."""

        super().__init__()

        self.sprites_flower = []

        # Define the size of the sprites (in pixels)
        gif_size = (80, 80)

        # Import and resize sprites
        sprite_flower_0 = pygame.image.load("PNJ/flower/PNJ_flower1/sprite_flower0.png").convert_alpha()
        sprite_flower_0 = pygame.transform.scale(sprite_flower_0, gif_size)

        sprite_flower_1 = pygame.image.load("PNJ/flower/PNJ_flower1/sprite_flower1.png").convert_alpha()
        sprite_flower_1 = pygame.transform.scale(sprite_flower_1, gif_size)

        # Put the sprites in the sprites array
        self.sprites_flower.append(sprite_flower_0)
        self.sprites_flower.append(sprite_flower_1)

        # The first image to display corresponds to the image at index 0.
        # Then the index will be increased by one until reaching the maximum index.
        self.actual_sprite = 0
        self.image = self.sprites_flower[self.actual_sprite]

        # Creating a rectangle around the image in order to place it wherever we want
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        # We go to the next image in the array (we use a value inferior to 0 to slow down the animation because of the
        # int casting will round it to the next integer)
        self.actual_sprite += speed

        # the indexes of the array are limited, there will be an error if it goes past the maximum index
        if self.actual_sprite >= len(self.sprites_flower):
            self.actual_sprite = 0

        # We also need to update the image to be displayed
        self.image = self.sprites_flower[int(self.actual_sprite)]


# Zombie class
class Zombie(pygame.sprite.Sprite):
    """To animate the bee."""
    def __init__(self, pos_x, pos_y):

        super().__init__()

        self.sprites_zombie = []

        # Define the size of the sprites (in pixels)
        gif_size = (60, 60)

        # Import and resize images
        sprite_zombie_0 = pygame.image.load("PNJ/zombie/zombie_hand/sprite_zombie0.png").convert_alpha()
        sprite_zombie_0 = pygame.transform.scale(sprite_zombie_0, gif_size)

        sprite_zombie_1 = pygame.image.load("PNJ/zombie/zombie_hand/sprite_zombie1.png").convert_alpha()
        sprite_zombie_1 = pygame.transform.scale(sprite_zombie_1, gif_size)

        sprite_zombie_2 = pygame.image.load("PNJ/zombie/zombie_hand/sprite_zombie2.png").convert_alpha()
        sprite_zombie_2 = pygame.transform.scale(sprite_zombie_2, gif_size)

        sprite_zombie_3 = pygame.image.load("PNJ/zombie/zombie_hand/sprite_zombie3.png").convert_alpha()
        sprite_zombie_3 = pygame.transform.scale(sprite_zombie_3, gif_size)

        # Put the sprites in the sprites array
        self.sprites_zombie.append(sprite_zombie_0)
        self.sprites_zombie.append(sprite_zombie_1)
        self.sprites_zombie.append(sprite_zombie_2)
        self.sprites_zombie.append(sprite_zombie_3)

        # The first image to display corresponds to the image at index 0.
        # Then the index will be increased by one until reaching the maximum index.
        self.actual_sprite = 0
        self.image = self.sprites_zombie[self.actual_sprite]

        # Creating a rectangle around the image in order to place it wherever we want
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        # We go to the next image in the array (we use a value inferior to 0 to slow down the animation because of the
        # int casting will round it to the next integer)
        self.actual_sprite += speed

        # the indexes of the array are limited, there will be an error if it goes past the maximum index
        if self.actual_sprite >= len(self.sprites_zombie):
            self.actual_sprite = 0

        # We also need to update the image to be displayed
        self.image = self.sprites_zombie[int(self.actual_sprite)]


# Spider class
class Spider(pygame.sprite.Sprite):
    """To animate the bee."""
    def __init__(self, pos_x, pos_y):

        super().__init__()

        self.sprites_spider = []

        # Define the size of the sprites (in pixels)
        gif_size = (60, 60)

        # Import and resize images
        sprite_spider_00 = pygame.image.load("PNJ/spider/spider/sprite_spider00.png").convert_alpha()
        sprite_spider_00 = pygame.transform.scale(sprite_spider_00, gif_size)

        sprite_spider_01 = pygame.image.load("PNJ/spider/spider/sprite_spider01.png").convert_alpha()
        sprite_spider_01 = pygame.transform.scale(sprite_spider_01, gif_size)

        sprite_spider_02 = pygame.image.load("PNJ/spider/spider/sprite_spider02.png").convert_alpha()
        sprite_spider_02 = pygame.transform.scale(sprite_spider_02, gif_size)

        sprite_spider_03 = pygame.image.load("PNJ/spider/spider/sprite_spider03.png").convert_alpha()
        sprite_spider_03 = pygame.transform.scale(sprite_spider_03, gif_size)

        sprite_spider_04 = pygame.image.load("PNJ/spider/spider/sprite_spider04.png").convert_alpha()
        sprite_spider_04 = pygame.transform.scale(sprite_spider_04, gif_size)

        sprite_spider_05 = pygame.image.load("PNJ/spider/spider/sprite_spider05.png").convert_alpha()
        sprite_spider_05 = pygame.transform.scale(sprite_spider_05, gif_size)

        sprite_spider_06 = pygame.image.load("PNJ/spider/spider/sprite_spider06.png").convert_alpha()
        sprite_spider_06 = pygame.transform.scale(sprite_spider_06, gif_size)

        sprite_spider_07 = pygame.image.load("PNJ/spider/spider/sprite_spider07.png").convert_alpha()
        sprite_spider_07 = pygame.transform.scale(sprite_spider_07, gif_size)

        sprite_spider_08 = pygame.image.load("PNJ/spider/spider/sprite_spider08.png").convert_alpha()
        sprite_spider_08 = pygame.transform.scale(sprite_spider_08, gif_size)

        sprite_spider_09 = pygame.image.load("PNJ/spider/spider/sprite_spider09.png").convert_alpha()
        sprite_spider_09 = pygame.transform.scale(sprite_spider_09, gif_size)

        sprite_spider_10 = pygame.image.load("PNJ/spider/spider/sprite_spider10.png").convert_alpha()
        sprite_spider_10 = pygame.transform.scale(sprite_spider_10, gif_size)

        sprite_spider_11 = pygame.image.load("PNJ/spider/spider/sprite_spider11.png").convert_alpha()
        sprite_spider_11 = pygame.transform.scale(sprite_spider_11, gif_size)

        sprite_spider_12 = pygame.image.load("PNJ/spider/spider/sprite_spider12.png").convert_alpha()
        sprite_spider_12 = pygame.transform.scale(sprite_spider_12, gif_size)

        # Put the sprites in the sprites array
        self.sprites_spider.append(sprite_spider_00)
        self.sprites_spider.append(sprite_spider_01)
        self.sprites_spider.append(sprite_spider_02)
        self.sprites_spider.append(sprite_spider_03)
        self.sprites_spider.append(sprite_spider_04)
        self.sprites_spider.append(sprite_spider_05)
        self.sprites_spider.append(sprite_spider_06)
        self.sprites_spider.append(sprite_spider_07)
        self.sprites_spider.append(sprite_spider_08)
        self.sprites_spider.append(sprite_spider_09)
        self.sprites_spider.append(sprite_spider_10)
        self.sprites_spider.append(sprite_spider_11)
        self.sprites_spider.append(sprite_spider_12)

        # The first image to display corresponds to the image at index 0.
        # Then the index will be increased by one until reaching the maximum index.
        self.actual_sprite = 0
        self.image = self.sprites_spider[self.actual_sprite]

        # Creating a rectangle around the image in order to place it wherever we want
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        # We go to the next image in the array (we use a value inferior to 0 to slow down the animation because of the
        # int casting will round it to the next integer)
        self.actual_sprite += speed

        # the indexes of the array are limited, there will be an error if it goes past the maximum index
        if self.actual_sprite >= len(self.sprites_spider):
            self.actual_sprite = 0

        # We also need to update the image to be displayed
        self.image = self.sprites_spider[int(self.actual_sprite)]


# Bee class
class Bee(pygame.sprite.Sprite):
    """To animate the bee."""
    def __init__(self, pos_x, pos_y):

        super().__init__()

        self.sprites_bee = []

        # Define the size of the sprites (in pixels)
        gif_size = (160, 160)

        # Import and resize images
        sprite_bee_0 = pygame.image.load("PNJ/bee/beep beep the bee/sprite_bee0.png").convert_alpha()
        sprite_bee_0 = pygame.transform.scale(sprite_bee_0, gif_size)

        sprite_bee_1 = pygame.image.load("PNJ/bee/beep beep the bee/sprite_bee1.png").convert_alpha()
        sprite_bee_1 = pygame.transform.scale(sprite_bee_1, gif_size)

        sprite_bee_2 = pygame.image.load("PNJ/bee/beep beep the bee/sprite_bee2.png").convert_alpha()
        sprite_bee_2 = pygame.transform.scale(sprite_bee_2, gif_size)

        sprite_bee_3 = pygame.image.load("PNJ/bee/beep beep the bee/sprite_bee3.png").convert_alpha()
        sprite_bee_3 = pygame.transform.scale(sprite_bee_3, gif_size)

        # Put the sprites in the sprites array
        self.sprites_bee.append(sprite_bee_0)
        self.sprites_bee.append(sprite_bee_1)
        self.sprites_bee.append(sprite_bee_2)
        self.sprites_bee.append(sprite_bee_3)

        # The first image to display corresponds to the image at index 0.
        # Then the index will be increased by one until reaching the maximum index.
        self.actual_sprite = 0
        self.image = self.sprites_bee[self.actual_sprite]

        # Creating a rectangle around the image in order to place it wherever we want
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        # We go to the next image in the array (we use a value inferior to 0 to slow down the animation because of the
        # int casting will round it to the next integer)
        self.actual_sprite += speed

        # the indexes of the array are limited, there will be an error if it goes past the maximum index
        if self.actual_sprite >= len(self.sprites_bee):
            self.actual_sprite = 0

        # We also need to update the image to be displayed
        self.image = self.sprites_bee[int(self.actual_sprite)]

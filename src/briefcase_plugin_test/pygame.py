from briefcase.bootstraps import PygameGuiBootstrap


class PygameAutomationBootstrap(PygameGuiBootstrap):
    def app_source(self):
        return """\
import importlib.metadata
import os
import sys

import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)


def main():
    app_module = sys.modules["__main__"].__package__
    metadata = importlib.metadata.metadata(app_module)

    os.environ["SDL_VIDEO_X11_WMCLASS"] = metadata["Formal-Name"]

    pygame.init()
    pygame.display.set_caption(metadata["Formal-Name"])
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.time.set_timer(pygame.QUIT, 2000)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(">>> successfully started...exiting <<<")
                print(">>>>>>>>>> EXIT 0 <<<<<<<<<<")
                running = False
                break

        screen.fill(WHITE)
        pygame.display.flip()

    pygame.quit()
"""

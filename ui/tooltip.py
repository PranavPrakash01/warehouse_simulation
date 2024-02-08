# ui/tooltip.py

import pygame

def draw_tooltip(screen, components, cell_size, start_x, start_y):
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for component in components:
        # Determine the component_rect based on the existence of 'cells' attribute
        if hasattr(component, 'cells'):
            component_rects = [pygame.Rect(start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size) for row, col in component.cells]
        else:
            component_rect = pygame.Rect(start_x + component.column * cell_size, start_y + component.row * cell_size, cell_size, cell_size)
            component_rects = [component_rect]

        # Check collision for each component_rect
        for component_rect in component_rects:
            if component_rect.collidepoint(mouse_x, mouse_y):
                tooltip_text = pygame.font.Font(None, 24).render(component.get_name(), True, (255, 255, 255))
                tooltip_rect = tooltip_text.get_rect(center=(mouse_x, mouse_y - 20))
                pygame.draw.rect(screen, (50, 50, 50), tooltip_rect)  # Tooltip background
                screen.blit(tooltip_text, tooltip_rect)

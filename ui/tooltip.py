# ui/tooltip.py

import pygame
from components.storage_area import StorageArea
pygame.init()
font = pygame.font.Font(None, 24)

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
                tooltip_text = get_tooltip_text(component)
                if isinstance(component, StorageArea):
                    tooltip_rect = tooltip_text.get_rect(center=(mouse_x, mouse_y - 40))
                else:
                    tooltip_rect = tooltip_text.get_rect(center=(mouse_x, mouse_y - 20))
                pygame.draw.rect(screen, (50, 50, 50), tooltip_rect)  # Tooltip background
                screen.blit(tooltip_text, tooltip_rect)

def get_tooltip_text(component):
    name_text = component.get_name()

    if isinstance(component, StorageArea):
        storage_area_info = f"{name_text}   Item Location: {component.item_location}   Max Capacity: {component.max_capacity}   Current Items: {len(component.storage_list)}"

        # Split the storage_area_info into lines
        lines = storage_area_info.split("   ")
        
        # Render each line separately
        rendered_lines = [font.render(line, True, (255, 255, 255)) for line in lines]

        # Calculate total height for rendering
        total_height = sum([line.get_height() for line in rendered_lines])

        # Create a surface for the tooltip text
        tooltip_text = pygame.Surface((max(line.get_width() for line in rendered_lines), total_height), pygame.SRCALPHA)

        # Blit each line onto the tooltip surface
        y_offset = 0
        for line in rendered_lines:
            tooltip_text.blit(line, (0, y_offset))
            y_offset += line.get_height()

    else:
        tooltip_text = font.render(name_text, True, (255, 255, 255))

    return tooltip_text



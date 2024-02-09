# event_log.py
import pygame

class EventLog:
    def __init__(self):
        self.log_entries = []
        self.all_logs = []
        self.max_entries = 6  # Maximum number of entries to display in the event_log_box
        self.log_font = pygame.font.Font("assets/RobotoMono-Light.ttf", 10)

    def add_entry(self, entry):
        self.log_entries.insert(0, entry)
        self.all_logs.append(entry)   # Insert new entry at the beginning
        if len(self.log_entries) > self.max_entries:
            self.log_entries.pop()  # Remove the last entry if exceeding the maximum
        if len(self.all_logs) > 100:
            self.log_entries.pop(0)

    def get_entries(self):
        return self.log_entries
    
    def draw_event_log(self, screen, event_log_box):
        max_entries = min(len(self.log_entries), self.max_entries)  # Determine the maximum entries to display
        for i in range(max_entries):
            log_entry = self.log_entries[i]
            text_surface = self.log_font.render(log_entry, True, (255, 255, 255))  # Enable anti-aliasing
            text_rect = text_surface.get_rect(topleft=(event_log_box.left + 10, event_log_box.top + 5 + i * 10 + i * 2))
            screen.blit(text_surface, text_rect)



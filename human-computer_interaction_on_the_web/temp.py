import pygame
consecutive_thumbs_up_count=0
consecutive_thumbs_down_count=0

match consecutive_thumbs_up_count:
pygame.mixer.Sound(r"feedbacksounds\start_1.mp3")
    case 1: pygame.mixer.Sound(r"feedbacksounds\start_2.mp3")
    case 2: pygame.mixer.Sound(r"feedbacksounds\start_3.mp3")
    case 3: pygame.mixer.Sound(r"feedbacksounds\start_4.mp3")
    case 4: pygame.mixer.Sound(r"feedbacksounds\start_5.mp3")
    case _: pygame.mixer.Sound(r"feedbacksounds\start_6.mp3")
        

match consecutive_thumbs_down_count:
    case 0: pygame.mixer.Sound(r"feedbacksounds\start_6.mp3")
    case 1: pygame.mixer.Sound(r"feedbacksounds\start_5.mp3")
    case 2: pygame.mixer.Sound(r"feedbacksounds\start_4.mp3")
    case 3: pygame.mixer.Sound(r"feedbacksounds\start_3.mp3")
    case 4: pygame.mixer.Sound(r"feedbacksounds\start_2.mp3")
    case _: pygame.mixer.Sound(r"feedbacksounds\start_1.mp3")
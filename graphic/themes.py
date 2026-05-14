COLOR_THEMES = {
    "Classic Monochrome": {
        "bg":      (0,   0,   0),
        "cell":    (200, 200, 200),
        "entry":   (180,   0, 180),
        "exit":    (200,   0,   0),
        "blocked": (80,   80,  80),
        "path":    (255, 220,   0),
    },

    "Deep Ocean": {
        "bg":      (10,  10,  30),
        "cell":    (60,  80, 160),
        "entry":   (0,  200, 255),
        "exit":    (255,  60,  60),
        "blocked": (30,  30,  60),
        "path":    (0,  255, 160),
    },

    "Retro Terminal": {
        "bg":      (0,   0,   0),
        "cell":    (0,  160,   0),
        "entry":   (0,  255, 100),
        "exit":    (255,  50,  50),
        "blocked": (0,   50,   0),
        "path":    (255, 255,   0),
    },

    "Ancient Desert": {
        "bg":      (20,  12,   5),
        "cell":    (200, 170, 120),
        "entry":   (120, 200,  80),
        "exit":    (200,  60,  40),
        "blocked": (70,  55,  35),
        "path":    (255, 200,  80),
    },

    "Frozen Aurora": {
        "bg":      (5,   15,  25),
        "cell":    (180, 220, 255),
        "entry":   (0,  255, 200),
        "exit":    (255, 100, 120),
        "blocked": (40,  70, 100),
        "path":    (255, 255, 150),
    },

    "Volcanic Ash": {
        "bg":      (18,  18,  18),
        "cell":    (120, 120, 120),
        "entry":   (255, 140,   0),
        "exit":    (255,  40,  40),
        "blocked": (50,   50,  50),
        "path":    (255, 220, 120),
    },

    "Cyberpunk Neon": {
        "bg":      (8,    0,  20),
        "cell":    (255,   0, 200),
        "entry":   (0,   255, 255),
        "exit":    (255,  80, 120),
        "blocked": (40,   10,  60),
        "path":    (255, 255,   0),
    },

    "Forest Night": {
        "bg":      (10,  25,  10),
        "cell":    (80, 140,  80),
        "entry":   (120, 255, 120),
        "exit":    (255,  90,  90),
        "blocked": (30,  60,  30),
        "path":    (255, 240, 120),
    },

    "Royal Purple": {
        "bg":      (25,  10,  40),
        "cell":    (180, 140, 255),
        "entry":   (255, 120, 255),
        "exit":    (255,  80, 120),
        "blocked": (60,  30,  80),
        "path":    (255, 220, 120),
    },

    "Sunset Horizon": {
        "bg":      (30,  10,   5),
        "cell":    (255, 140, 100),
        "entry":   (255, 220, 120),
        "exit":    (255,  80,  80),
        "blocked": (90,  40,  20),
        "path":    (255, 255, 180),
    },
}

RESET = "\033[0m"

THEME_NAMES = list(COLOR_THEMES.keys())

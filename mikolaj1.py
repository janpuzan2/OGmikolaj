import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle, Circle, Polygon
import numpy as np

# Ustawienie tytułu aplikacji Streamlit
st.title("🎅 Mikołaj z Prezentami (Streamlit & Matplotlib)")

# --- INTERFEJS UŻYTKOWNIKA (Streamlit Widgets) ---

# Używamy st.color_picker, aby użytkownik mógł wybrać kolor skóry
# Domyślny kolor to ROSY_SKIN z poprzedniej wersji.
DEFAULT_SKIN_COLOR = '#FFDBAC'
selected_skin_color = st.sidebar.color_picker('Wybierz kolor skóry Mikołaja:', DEFAULT_SKIN_COLOR)

# Definicja funkcji rysującej Mikołaja (przyjmuje argument koloru skóry)
def draw_santa(skin_color):
    # Konfiguracja płótna Matplotlib
    fig, ax = plt.subplots(figsize=(7, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(-2, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    # Kolory
    WARM_RED = '#E53935'    
    WARM_WHITE = '#F5F5F5'  
    # ROSY_SKIN jest teraz pobierany z argumentu 'skin_color'
    LIGHT_ROSE = '#FFCDD2'  # Utrzymujemy ten sam dla nosa, chyba że zechcesz go też zmienić
    GREEN = '#4CAF50'      
    GOLD = '#FFD700'       
    CREAM_WHITE = '#FFFDE7' 

    # 1. Tło
    ax.set_facecolor(CREAM_WHITE)

    # --- POSTAĆ MIKOŁAJA ---

    # GŁOWA I BRODA
    beard_center = (5, 6.5)
    beard_radius_x = 3.2
    beard_radius_y = 3.0
    head_beard = Ellipse(beard_center, width=beard_radius_x * 2, height=beard_radius_y * 2,
                         color=WARM_WHITE, ec='grey', lw=0.5, zorder=1)
    ax.add_artist(head_beard)

    # TWARZ UŻYWA WYBRANEGO KOLORU
    face_center = (5, 7.2)
    face_radius = 1.2
    face = Circle(face_center, face_radius, color=skin_color, ec='grey', lw=0.5, zorder=2) # TUTAJ ZMIANA
    ax.add_artist(face)

    # Kapelusz (bez zmian)
    hat_y_base = 7.4
    hat_points = [(3.4, hat_y_base), (6.6, hat_y_base), (5, 9.5)]
    ax.add_patch(Polygon(hat_points, closed=True, color=WARM_RED, zorder=3))
    ax.bar(x=5, height=0.4, width=3.5, bottom=7.2, color=WARM_WHITE, align='center', zorder=4, edgecolor='grey', linewidth=0.5)
    pompon = Circle((7.0, 8.5), 0.5, color=WARM_WHITE, ec='grey', lw=0.5, zorder=5)
    ax.add_artist(pompon)

    # Detale Twarzy
    nose = Circle((5, 6.8), 0.4, color=LIGHT_ROSE, ec='grey', lw=0.5, zorder=6)
    ax.add_artist(nose)
    ax.plot(4.3, 7.5, 'ko', markersize=4, zorder=6)
    ax.plot(5.7, 7.5, 'ko', markersize=4, zorder=6)
    mustache = Ellipse((5, 6.2), width=2.5, height=0.8, angle=0, color=WARM_WHITE, ec='grey', lw=0.5, zorder=6)
    ax.add_artist(mustache)
    ax.plot([4.6, 5.4], [6.0, 6.0], color='black', linewidth=1.5, zorder=6)
    ax.add_artist(Ellipse((4.3, 6.1), width=0.8, height=0.3, angle=15, color=WARM_WHITE, ec='grey', lw=0.5, zorder=6))
    ax.add_artist(Ellipse((5.7, 6.1), width=0.8, height=0.3, angle=-15, color=WARM_WHITE, ec='grey', lw=0.5, zorder=6))

    # TUŁÓW I PŁASZCZ (bez zmian)
    body_center = (5, 3.5)
    body_width = 5.0
    body_height = 4.0
    body = Ellipse(body_center, width=body_width, height=body_height, angle=0,
                   color=WARM_RED, ec='black', lw=1.5, zorder=0)
    ax.add_artist(body)

    fur_strip = Rectangle((4.5, 1.5), width=1.0, height=4.0, color=WARM_WHITE, zorder=1)
    ax.add_patch(fur_strip)

    belt = Rectangle((2.5, 3.0), width=5.0, height=0.5, color='black', zorder=2)
    ax.add_patch(belt)

    buckle = Rectangle((4.6, 3.0), width=0.8, height=0.5, color=GOLD, zorder=3)
    ax.add_patch(buckle)

    # KOŃCZYNY (bez zmian)
    arm_width = 1.0
    arm_height = 2.0
    ax.add_patch(Rectangle((2.5, 4.0), arm_width, arm_height, color=WARM_RED, zorder=0, angle=10))
    ax.add_patch(Rectangle((6.5, 4.0), arm_width, arm_height, color=WARM_RED, zorder=0, angle=-10))

    glove_radius = 0.5
    ax.add_artist(Circle((2.5, 4.5), glove_radius, color=WARM_WHITE, ec='black', lw=1, zorder=4))
    ax.add_artist(Circle((7.5, 4.5), glove_radius, color=WARM_WHITE, ec='black', lw=1, zorder=4))

    leg_width = 1.5
    leg_height = 2.0
    ax.add_patch(Rectangle((3.0, -0.5), leg_width, leg_height, color=WARM_RED, zorder=0))
    ax.add_patch(Rectangle((5.5, -0.5), leg_width, leg_height, color=WARM_RED, zorder=0))

    shoe_width = 2.0
    shoe_height = 0.5
    ax.add_patch(Rectangle((2.8, -1.0), shoe_width, shoe_height, color='black', zorder=1))
    ax.add_patch(Rectangle((5.2, -1.0), shoe_width, shoe_height, color='black', zorder=1))

    # --- DODANE PREZENTY (bez zmian) ---

    def draw_present(ax, x_base, y_base, width, height, color, ribbon_color, z):
        ax.add_patch(Rectangle((x_base, y_base), width, height, color=color, ec='black', lw=1, zorder=z))
        ax.add_patch(Rectangle((x_base + width/2 - 0.1, y_base), 0.2, height, color=ribbon_color, zorder=z + 1))
        ax.add_patch(Rectangle((x_base, y_base + height/2 - 0.1), width, 0.2, color=ribbon_color, zorder=z + 1))

    draw_present(ax, 0.5, -1.0, 1.8, 1.8, WARM_RED, GOLD, 1)
    draw_present(ax, 1.8, -0.7, 1.0, 1.0, GREEN, WARM_WHITE, 1)
    draw_present(ax, 7.5, -0.9, 1.5, 1.3, WARM_RED, WARM_WHITE, 1)
    draw_present(ax, 6.5, -0.8, 0.8, 0.8, GREEN, GOLD, 1)

    ax.set_title("Mikołaj z Prezentami (Matplotlib)", fontsize=16)

    return fig

# Wyświetlenie figury w Streamlit, przekazując wybrany kolor skóry
st.pyplot(draw_santa(selected_skin_color))

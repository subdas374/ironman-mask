import turtle

# Setup the window screen
screen = turtle.Screen()
screen.title("JARVIS - Iron Man Armor Interface")
screen.setup(width=600, height=650)
screen.bgcolor("#1A1A1A")  # Dark Charcoal

# Create the artist turtle
t = turtle.Turtle()
t.speed(3)  # Moderate speed so you can watch it draw
t.pensize(2)

def draw_polygon(points, fill_color, border_color):
    """Helper function to move turtle and draw a filled polygon."""
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.color(border_color, fill_color)
    t.begin_fill()
    for point in points[1:]:
        t.goto(point)
    t.goto(points[0])  # Close path
    t.end_fill()

# ==========================================
# 1. DRAW OUTER RED HELMET
# ==========================================
# Coordinate points mapping out the head shell
outer_helmet = [
    (-100, 200), (100, 200),   # Top head
    (150, 100),  (150, -50),   # Right ears/cheeks
    (80, -170),  (-80, -170),  # Jawline / Chin
    (-150, -50), (-150, 100)   # Left cheeks/ears
]
draw_polygon(outer_helmet, fill_color="#B71C1C", border_color="#7F0000")

# ==========================================
# 2. DRAW GOLD FACEPLATE
# ==========================================
# Coordinate points mapping out the golden face mask
face_plate = [
    (-70, 140),  (70, 140),    # Forehead
    (110, 70),   (110, -30),   # Right inner cheek
    (70, -110),  (50, -140),   # Right jaw
    (-50, -140), (-70, -110),  # Left jaw
    (-110, -30), (-110, 70)    # Left inner cheek
]
draw_polygon(face_plate, fill_color="#FFC107", border_color="#D32F2F")

# ==========================================
# 3. DRAW GLOWING ARC-REACTOR EYES
# ==========================================
# Left Eye
left_eye = [(-70, 50), (-20, 50), (-25, 35), (-70, 35)]
draw_polygon(left_eye, fill_color="#00E5FF", border_color="#FFFFFF")

# Right Eye
right_eye = [(20, 50), (70, 50), (70, 35), (25, 35)]
draw_polygon(right_eye, fill_color="#00E5FF", border_color="#FFFFFF")

# ==========================================
# 4. DETAIL ACCENTS (Mouth Line)
# ==========================================
t.penup()
t.goto(-40, -80)
t.pendown()
t.color("#333333")
t.pensize(4)
t.goto(40, -80)  # Main mouth slit

# Hide the turtle arrow when finished
t.hideturtle()

# Keep the window open until you click it
screen.exitonclick()

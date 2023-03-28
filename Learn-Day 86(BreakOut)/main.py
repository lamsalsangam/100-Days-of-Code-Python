from tkinter import *
import random

# set up the window
window = Tk()
window.title("Breakout")
window.resizable(False, False)

# set up the canvas
canvas_width = 500
canvas_height = 500
canvas = Canvas(window, width=canvas_width, height=canvas_height, bg='black')
canvas.pack()

# set up the paddle
paddle_width = 100
paddle_height = 10
paddle_start_x = canvas_width // 2 - paddle_width // 2
paddle_start_y = canvas_height - 50
paddle = canvas.create_rectangle(paddle_start_x, paddle_start_y,
                                  paddle_start_x + paddle_width, paddle_start_y + paddle_height,
                                  fill='white')

# set up the ball
ball_radius = 10
ball_start_x = canvas_width // 2
ball_start_y = paddle_start_y - ball_radius
ball = canvas.create_oval(ball_start_x - ball_radius, ball_start_y - ball_radius,
                           ball_start_x + ball_radius, ball_start_y + ball_radius,
                           fill='white')
ball_speed = 5
ball_dx = ball_speed
ball_dy = -ball_speed

# set up the bricks
brick_rows = 6
brick_cols = 10
brick_width = canvas_width // brick_cols
brick_height = 20
brick_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        color = brick_colors[row]
        brick = canvas.create_rectangle(col * brick_width, row * brick_height + 50,
                                         (col + 1) * brick_width, (row + 1) * brick_height + 50,
                                         fill=color)
        bricks.append(brick)

# move the ball
def move_ball():
    global ball_dx, ball_dy
    x1, y1, x2, y2 = canvas.coords(ball)
    if x1 <= 0 or x2 >= canvas_width:
        ball_dx = -ball_dx
    if y1 <= 0:
        ball_dy = -ball_dy
    if y2 >= paddle_start_y and x1 <= paddle_start_x + paddle_width and x2 >= paddle_start_x:
        ball_dy = -ball_speed
        ball_dx = random.uniform(-1, 1) * ball_speed
    if y2 >= canvas_height:
        canvas.create_text(canvas_width // 2, canvas_height // 2,
                            text="Game Over", fill='white', font=('Arial', 30))
        return
    overlapping_bricks = canvas.find_overlapping(x1, y1, x2, y2)
    for brick in overlapping_bricks:
        if brick in bricks:
            canvas.itemconfigure(brick, fill="black")
            ball_dy = -ball_dy
            bricks.remove(brick)
            break
    canvas.move(ball, ball_dx, ball_dy)
    window.after(20, move_ball)


# move the paddle
def move_paddle(event):
    global paddle_start_x
    if event.keysym == 'Left' and paddle_start_x >= 0:
        paddle_start_x -= 10
        canvas.move(paddle, -10, 0)
    if event.keysym == 'Right' and paddle_start_x + paddle_width <= canvas_width:
        paddle_start_x += 10
        canvas.move(paddle, 10, 0)

canvas.bind_all('<Left>', move_paddle)
canvas.bind_all('<Right>', move_paddle)

# start the game
move_ball()
window.mainloop()

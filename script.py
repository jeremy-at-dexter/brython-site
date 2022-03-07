print("Whats up")

from browser import document
import turtle

turtle.set_defaults(
    turtle_canvas_wrapper = document['turtle-div']
)

tim = turtle.Turtle()

tim.forward(100)

turtle.done()

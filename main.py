def on_button_pressed_a():
    basic.show_leds("""
        . . # . .
                . # . # .
                # # # # #
                # . . . #
                # . . . #
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_number(randint(1, 9))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    basic.show_leds("""
        # # # . .
                # . . # .
                # # # . .
                # . . # .
                # # # . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

MyAge = 27
basic.show_number(MyAge)
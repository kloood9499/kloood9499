input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . # . .
        . # . # .
        # # # # #
        # . . . #
        # . . . #
        `)
})
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(randint(1, 9))
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        # # # . .
        # . . # .
        # # # . .
        # . . # .
        # # # . .
        `)
})
let MyAge = 27
basic.showNumber(MyAge)

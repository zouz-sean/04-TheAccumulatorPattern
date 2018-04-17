"""
This module lets you practice one form of the ACCUMULATOR pattern,
namely, the "IN GRAPHICS" form which features:
  -- DRAWING OBJECTS via ACCUMULATING positions and/or sizes,
     as in:   x = x + pixels

Additionally, it emphasizes that you must
  ** DO A CONCRETE EXAMPLE BY HAND **
before you can implement a solution to the problem in Python.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Zhengxiao Zou.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


# ----------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# ----------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    test_draw_parallel_lines()
    test_draw_lines()


def test_draw_parallel_lines():
    """ Tests the   draw_parallel_lines  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_parallel_lines  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # TWO tests on ONE window.
    # ------------------------------------------------------------------
    title = 'Tests 1 and 2 of DRAW_PARALLEL_LINES:'
    title = title + '  4 long lines, 7 short lines'
    window1 = rg.RoseWindow(600, 350, title)

    # Test 1:
    left_most_point = rg.Point(400, 50)
    draw_parallel_lines(7, left_most_point, 100, window1)

    # Test 2:
    left_most_point = rg.Point(50, 200)
    draw_parallel_lines(4, left_most_point, 300, window1)
    window1.close_on_mouse_click()

    # ------------------------------------------------------------------
    # A third test on ANOTHER window.
    # ------------------------------------------------------------------
    title = 'Test 3 of DRAW_PARALLEL_LINES:  12 very long lines!'
    window2 = rg.RoseWindow(500, 400, title)

    # Test 3:
    left_most_point = rg.Point(20, 20)
    draw_parallel_lines(12, left_most_point, 470, window2)

    window2.close_on_mouse_click()


def draw_parallel_lines(n, point, length, window):
    """
    What comes in: The four arguments are:
      -- A positive integer n.
      -- An rg.Point.
      -- A positive integer length.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_parallel_lines.pdf   in this project for pictures
        that may help you better understand the following specification:
      Draws  n  rg.Lines parallel to each other,
      all on the given rg.RoseWindow, such that:
        -- The first rg.Line has its left-most end at the given rg.Point.
        -- Each rg.Line is a horizontal line
             (i.e., parallel to the x-axis).
        -- Each rg.Line has the given length.
        -- Each rg.Line is 30 pixels below the previous rg.Line.
      Must  ** render **     but   ** NOT close **   the window.
    Type hints:
      :type n: int
      :type point: rg.Point
      :type length: int
      :type window: rg.RoseWindow
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       endpoints for each line,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------
    x = point.x
    y = point.y

    for _ in range(n):
        point = rg.Point(x, y)
        start = rg.Point(point.x, point.y)
        end = rg.Point(point.x + length, point.y)
        line = rg.Line(start, end)


        line.attach_to(window)

        y = y + 30

    window.render()




def test_draw_lines():
    """ Tests the   draw_lines  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_lines  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 & 2 of DRAW_LINES:  4 lines, 12 lines!'
    window1 = rg.RoseWindow(350, 400, title)

    draw_lines(4, rg.Point(20, 120), window1)
    draw_lines(12, rg.Point(150, 230), window1)
    window1.close_on_mouse_click()

    # A third test on ANOTHER window.
    window2 = rg.RoseWindow(350, 300, 'Test 3 of DRAW_LINES:  7 lines!')
    draw_lines(7, rg.Point(50, 120), window2)
    window2.close_on_mouse_click()


def draw_lines(n, point, window):
    """
    What comes in: The three arguments are:
      -- A integer n that is at least 2.
      -- An rg.Point.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_lines.pdf   in this project for pictures that
        may help you better understand the following specification:
      Draws  n  rg.Lines on the given rg.RoseWindow, such that:
        -- The leftmost point of each of the rg.Lines
             is the given rg.Point.
     -- For the rightmost point of each of the lines:
         -- Its x-coordinate is (pX + 100),
              where pX is the x-coordinate of the given rg.Point.
         -- The y-coordinates of the lines vary evenly
              from  (pY - 100)  to  (pY + 100),
              where pY is the y-coordinate of the given rg.Point.
      Must  ** render **     but   ** NOT close **   the window.
    Type hints:
      :type n: int
      :type point: rg.Point
      :type window: rg.RoseWindow
    """
    # ------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       endpoints for each line,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------
    x = point.x
    y = point.y

    for _ in range(n):
        point = rg.Point(x, y)
        start = rg.Point(point.x, point.y)

    for k in range(1, n + 1):
        point.y = y - 100 + (200 * (k - 1) / (n - 1))
        end = rg.Point(point.x + 100, point.y)


        line = rg.Line(start, end)

        line.attach_to(window)

    window.render()





# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
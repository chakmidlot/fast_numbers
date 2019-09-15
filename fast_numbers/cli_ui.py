from contextlib import contextmanager
import curses


class CliUi:

    def __init__(self):
        self.stdscr = None

    @contextmanager
    def init(self):
        try:
            self.stdscr = curses.initscr()
            curses.noecho()
            curses.cbreak()
            self.stdscr.keypad(1)
            curses.curs_set(0)

            yield

        finally:
            self.stdscr.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin()

    def draw_status(self, score, level, lives, best_score):
        line_text = f"Score: {score:<5} Level: {level:<2} " \
                    f"Lives: {self.lives(lives)}   Best score: {best_score:<5}"
        self.stdscr.addstr(0, 0, line_text)
        self.stdscr.move(2, 0)
        self.stdscr.refresh()

    def read_number(self, length):
        curses.curs_set(1)
        curses.flushinp()

        self.show_hint("REPEAT THE NUMBER")
        self.stdscr.addstr(2, 0, "_" * length)
        self.stdscr.move(2, 0)

        position = 0
        number = ''
        while True:
            self.stdscr.move(2, position)
            self.stdscr.refresh()
            x = self.stdscr.getkey()
            if x.isdigit():
                number += x
                self.stdscr.addch(x)
                position += 1
            elif x == 'KEY_BACKSPACE' and number:
                number = number[:-1]
                position -= 1
                self.stdscr.addch(2, position, '_')
            elif x == '\n':
                self.stdscr.addstr(2, 0, ' ' * 20)
                curses.curs_set(0)
                return number

    def lives(self, lives):
        return '♥ ' * lives + '♡ ' * (5 - lives)

    def show_number(self, number):
        self.show_hint("")
        self.stdscr.addstr(1, 0, str(number) + " " * 20)
        self.stdscr.move(2, 0)
        self.stdscr.refresh()

    def hide_number(self):
        self.stdscr.addstr(1, 0, " " * 10)
        self.stdscr.refresh()

    def game_over(self, initial, typed):
        self.stdscr.addstr(1, 0, "GAME OVER      SHOWED: {}".format(initial))
        self.stdscr.addstr(2, 0, "                TYPED: {}".format(typed))

    def wrong_answer(self, initial, typed):
        self.stdscr.addstr(1, 0, "WRONG          SHOWED: {}".format(initial))
        self.stdscr.addstr(2, 0, "                TYPED: {}".format(typed))

    def wait_user_next(self):
        self.show_hint("PRESS ENTER")
        self.stdscr.move(2, 0)
        curses.curs_set(1)
        while self.stdscr.getkey() != '\n':
            pass
        curses.curs_set(0)
        self.stdscr.addstr(1, 0, " " * 30)
        self.stdscr.addstr(2, 0, " " * 30)

    def show_hint(self, text):
        self.stdscr.addstr(4, 0, "{} {}".format(text, " " * 30))

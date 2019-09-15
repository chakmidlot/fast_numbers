import random
import time

from fast_numbers.cli_ui import CliUi
from fast_numbers.settings import LEVELS


class FastNumbers:

    def __init__(self, ui):
        self.ui = ui

        self.active = False

        self.score = 0
        self.level = 0
        self.lives = 0
        self.best_score = 0

        self._rnd = random.Random()

    def run(self):
        try:
            with self.ui.init():
                self.play_loop()
        except KeyboardInterrupt:
            pass

    def play_loop(self):
        while True:
            self.ui.draw_status(self.score, self.level, self.lives, self.best_score)

            if self.active:
                self.guess_next()
            else:
                self.wait_start()
                self.reset()

    def guess_next(self):
        number = self.get_random_number()
        answer = self.show_and_ask(number)

        if str(number) == answer:
            self.correct()
        else:
            self.wrong(number, answer)

    def wait_start(self):
        self.ui.wait_user_next()

    def show_and_ask(self, number):
        self.ui.show_number(number)
        time.sleep(LEVELS[self.level].delay)
        self.ui.hide_number()
        return self.ui.read_number(len(str(number)))

    def wrong(self, initial, typed):
        if self.lives == 0:
            self.ui.game_over(initial, typed)
            self.reset()
        else:
            self.lives -= 1
            self.ui.draw_status(self.score, self.level, self.lives, self.best_score)
            self.ui.wrong_answer(initial, typed)

        self.wait_start()

    def correct(self):
        self.score += 1
        self.best_score = max(self.score, self.best_score)
        level_number = self.score // 5
        if level_number >= len(LEVELS):
            level_number = len(LEVELS) - 1
        self.level = level_number

    def get_random_number(self):
        l = LEVELS[self.level].length
        b = 10 ** l
        a = b // 10
        return self._rnd.randint(a, b)

    def reset(self):
        self.active = True

        self.score = 0
        self.level = 0
        self.lives = 5
        self.best_score = 0


def main():
    ui = CliUi()
    game = FastNumbers(ui)
    game.run()


if __name__ == '__main__':
    main()

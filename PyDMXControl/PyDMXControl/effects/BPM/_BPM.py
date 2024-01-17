from ..defaults import Effect
import time


class BPM(Effect):
    def __init__(self, *args, **kwargs):
        self._bpm = 128
        self._bpm_period = int(60 * 1000 / self._bpm)
        self._state = True
        self.last_tick = 0
        self.off_counter = 0

        super().__init__(*args, **kwargs)
        self.__start = None

    def callback(self):
        if self.__start is None:
            self.__start = self.fixture.controller.ticker.millis_now()
            # self.last_tick = self.fixture.controller.ticker.millis_now()

        now = self.fixture.controller.ticker.millis_now()
        if now - self.last_tick > self._bpm_period:
            if self.off_counter == 0:
                self.fixture.set_channel("dimmer", 255)
            else:
                self.fixture.set_channel("dimmer", 0)
            self.off_counter = (self.off_counter + 1) % 2
            self.last_tick = now

    def start(self):
        self.__start = None
        super().start()

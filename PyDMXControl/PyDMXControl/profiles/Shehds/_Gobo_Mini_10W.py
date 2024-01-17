from warnings import warn

from ..defaults import Fixture


class Gobo_Mini_11Ch(Fixture):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._register_channel("pan")
        self._register_channel("pan_fine")
        self._register_channel("y_axis")
        self._register_channel("y_axis_fine")
        self._register_channel("axis")
        self._register_channel("dimmer")
        self._register_channel("strobe")
        self._register_channel("red")
        self._register_channel_aliases("red", "r")
        self._register_channel("green")
        self._register_channel_aliases("green", "g")
        self._register_channel("blue")
        self._register_channel_aliases("blue", "b")
        self._register_channel("white")
        self._register_channel_aliases("white", "w")


class Gobo_Mini_13Ch(Fixture):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._register_channel("x_axis")
        self._register_channel("x_axis_fine")
        self._register_channel("y_axis")
        self._register_channel("y_axis_fine")
        self._register_channel("axis")
        self._register_channel("dimmer")
        self._register_channel("strobe")
        self._register_channel("red")
        self._register_channel_aliases("red", "r")
        self._register_channel("green")
        self._register_channel_aliases("green", "g")
        self._register_channel("blue")
        self._register_channel_aliases("blue", "b")
        self._register_channel("white")
        self._register_channel_aliases("white", "w")
        # 0-249 auto run mode
        # 250 - 255 sound mode
        self._register_channel("auto_run_mode")
        self._register_channel("rest")

from PyDMXControl.PyDMXControl.controllers import OpenDMXController

# from PyDMXControl.PyDMXControl.profiles.Shehds import Shehds_Gobo_Mini_11Ch

from PyDMXControl.PyDMXControl.profiles.Shehds import Shehds_Gobo_Mini_13Ch

# from PyDMXControl.PyDMXControl.effects.Intensity import Dim
from PyDMXControl.PyDMXControl.effects.BPM import BPM
from PyDMXControl.PyDMXControl.effects.Color import Chase

dmx = OpenDMXController(ticker_interval_millis=1 / 30 * 1000.0)

fixture = dmx.add_fixture(Shehds_Gobo_Mini_13Ch, name="gobo_1")
fixture.dim(255, 0)
fixture.color([255, 0, 0])

# fixture.dim(255, 5000, channel="pan")
# fixture.add_effect(Chase, colors=[[255, 0, 0], [0, 0, 255]], speed=100)
dim_effect = BPM(fixture, 0)
# dim_effect.start()

chase = Chase(fixture, 1000, colors=[[255, 0, 0], [0, 0, 255]])


def pan_value():
    print(fixture.get_channel_value("pan"))


dmx.web_control(
    callbacks={
        "start_bpm": dim_effect.start,
        "stop_bpm": dim_effect.stop,
        "start_chase": chase.start,
        "stop_chase": chase.stop,
        "pan": pan_value,
    }
)

dmx.debug_control()

dmx.sleep_till_enter()

dmx.close()

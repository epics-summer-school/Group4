from ophyd import EpicsSignal, EpicsSignalRO
import time
from ophyd.pv_positioner import PVPositionerComparator, PVPositionerDone

from ophyd import Device, Component
from ophyd.status import Status
import numpy as np

class StepperMotorPositioner(Device):


    setpoint = Component(EpicsSignal, 'Mtr')
    readback = Component(EpicsSignal, 'Mtr', kind='hinted')


    def set(self,position):
        speed_rate = 500

        self.setpoint.set(position)
        stat = Status(settle_time=10) #np.abs(position)/speed_rate)

        stat.set_finished()
        return stat

# z_stage = StepperMotorPositioner(SMprefix, name='StepperMotor')
# z_stage.wait_for_connection()
# stat = z_stage.set(-1000)
# stat.wait()
# print("go to lunch")
# from bluesky import RunEngine


# RE=RunEngine()

# from bluesky.plans import scan
# from bluesky.plan_stubs import mov

# RE(mov(z_stage,-2000))

# from ophyd.sim import det

# RE(scan([det],z_stage,-1000,-1200,10))

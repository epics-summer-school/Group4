# Workarounds/patches
from ophyd.signal import EpicsSignalBase
EpicsSignalBase.set_defaults(connection_timeout= 5, timeout=200)

from ophyd import EpicsMotor

# standard magics
from bluesky.magics import BlueskyMagics
get_ipython().register_magics(BlueskyMagics)

# simulated devices
from ophyd.sim import det1, det2, det3, det4, motor1, motor2, motor, noisy_det   # two simulated detectors
from beamlinetools.devices.StepperMotor import StepperMotorPositioner
from beamlinetools.devices.Group4GaussMeter import GaussMeter
from beamlinetools.devices.PowerSupply1 import PowerSupply1

SMprefix='Gr4:Ax1_'
Prefix='Group4:'
MyGauss='GssMtr1:'
MyPwr='PwrSup1:'


myPwrSup=PowerSupply1(Prefix+MyPwr,name='myPwrSup')
#myPwrSup.read()

MyGaussMeter = GaussMeter(Prefix+MyGauss, name='MyGaussMeter')
#MyGaussMeter.read()



z_stage = StepperMotorPositioner(SMprefix, name='z_stage')
#z_stage.wait_for_connection()
#stat = z_stage.set(-1000)
#stat.wait()
#print("stat")




from bluesky.plans import scan
from bluesky.plan_stubs import mov
#load_user_script("myPlan.py")


# RE(mov(z_stage, -2000))
#rom ophyd.sim import det 
#from user_scripts import myPlan
#RE(scan([det],z_stage,500,-4800,10))

# RE(scan([MyGaussMeter],z_stage,-4800,500,10))

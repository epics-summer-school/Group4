# start of automatically prepended lines
from beamlinetools.BEAMLINE_CONFIG import *
# end of automatically prepended lines
import numpy as np

#from beamlinetools.devices.StepperMotor import StepperMotorPositioner
#from beamlinetools.devices.Group4GaussMeter import GaussMeter
#from beamlinetools.devices.PowerSupply1 import PowerSupply1


def sweep_Current(Current):
    "Multiple scans: one per exposure time setting."
    myPwrSup.EnableCurr.set(1)
    for i in Current:
        yield from mv(myPwrSup.I_set, i)
        yield from scan([MyGaussMeter], z_stage, 0, -5300, 20)
    myPwrSup.I_set.set(0)
    myPwrSup.EnableCurr.set(0)

#SMprefix='Gr4:Ax1_'
#Prefix='Group4:'
#MyGauss='GssMtr1:'
#MyPwr='PwrSup1:'

#myPwrSup=PowerSupply1(Prefix+MyPwr,name='myPwrSup')
#MyGaussMeter = GaussMeter(Prefix+MyGauss, name='MyGaussMeter')
#z_stage = StepperMotorPositioner(SMprefix, name='z_stage')


if myPwrSup.connected==1 and MyGaussMeter.connected==1 and z_stage.connected==1:
	CurrentScan=np.arange(1,2.5,0.5)
	print('Everything is fine')
else:
	print(f'Nothing is working: Power={myPwrSup.connected}, Gauss={MyGaussMeter.connected}, Motor={z_stage.connected}')
#RE(sweep_Current(CurrentScan))

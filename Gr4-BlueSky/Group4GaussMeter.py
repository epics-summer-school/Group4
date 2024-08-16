from ophyd import Device, Component, EpicsSignal, EpicsSignalRO

# Gauss Meter
# Prefix='Group4:'
# MyGauss='GssMtr1:'

class GaussMeter(Device):
    Bx = Component(EpicsSignalRO, 'MagX:get')
    By = Component(EpicsSignalRO, 'MagY:get')
    Bz = Component(EpicsSignalRO, 'MagZ:get')
    Btot = Component(EpicsSignalRO, 'MagSum:get', kind='hinted')

# and connect to multiple instances
# of that device.
# MyGaussMeter = GaussMeter(Prefix+MyGauss, name='GaussMeter')

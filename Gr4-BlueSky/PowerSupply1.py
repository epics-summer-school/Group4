from ophyd import Device, Component, EpicsSignal, EpicsSignalRO

# Gauss Meter
# Prefix='Group4:'
# MyGauss='PwrSup1:'

class PowerSupply1(Device):
    I = Component(EpicsSignalRO, 'Curr:get')
    V = Component(EpicsSignalRO, 'Volt:get')
    Ramp_rate = Component(EpicsSignalRO, 'Ramp:get')
    EnableCurr= Component(EpicsSignal, 'Enable')
    I_set= Component(EpicsSignal, 'Curr:set')
    Ramp_rate_set = Component(EpicsSignal, 'Ramp:set')
    

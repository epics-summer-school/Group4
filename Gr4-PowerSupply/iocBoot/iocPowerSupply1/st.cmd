#!../../bin/linux-x86_64/PowerSupply1

#- You may have to change PowerSupply1 to something else
#- everywhere it appears in this file

#< envPaths

## Register all support components
dbLoadDatabase "../../dbd/PowerSupply1.dbd"
PowerSupply1_registerRecordDeviceDriver(pdbbase) 
drvAsynIPPortConfigure("DEV1", "192.168.1.71:10001")
## Load record instances
dbLoadRecords("../../db/PowerSupply1.db","user=Group4:PwrSup1, PORT=DEV1")
epicsEnvSet("STREAM_PROTOCOL_PATH", "../../db")

iocInit()

## Start any sequence programs
#seq sncPowerSupply1,"user=Group4:PwrSup1"

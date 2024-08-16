#!../../bin/linux-x86_64/ioc_gauss

#- You may have to change ioc_gauss to something else
#- everywhere it appears in this file

#< envPaths

## Register all support components
dbLoadDatabase "../../dbd/ioc_gauss.dbd"
ioc_gauss_registerRecordDeviceDriver(pdbbase) 
drvAsynIPPortConfigure("IP1","192.168.1.75:7777")
## Load record instances
dbLoadRecords("../../db/gauss.db","user=Group4")
epicsEnvSet("STREAM_PROTOCOL_PATH","../../db/")

iocInit()

## Start any sequence programs
#seq sncioc_gauss,"user=epics"

TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = PowerSupply1
# PowerSupply1.dbd will be created and installed
DBD += PowerSupply1.dbd

# PowerSupply1.dbd will be made up from these files:
PowerSupply1_DBD += base.dbd

PowerSupply1_DBD += stream-base.dbd
PowerSupply1_DBD += asyn.dbd
PowerSupply1_DBD += drvAsynIPPort.dbd
# Include dbd files from all support applications:
#PowerSupply1_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#PowerSupply1_LIBS += xxx
PowerSupply1_LIBS += stream
PowerSupply1_LIBS += asyn
# PowerSupply1_registerRecordDeviceDriver.cpp derives from PowerSupply1.dbd
PowerSupply1_SRCS += PowerSupply1_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
PowerSupply1_SRCS_DEFAULT += PowerSupply1Main.cpp
PowerSupply1_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#PowerSupply1_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
PowerSupply1_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE


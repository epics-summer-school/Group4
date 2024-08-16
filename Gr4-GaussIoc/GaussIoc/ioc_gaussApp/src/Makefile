TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = ioc_gauss
# ioc_gauss.dbd will be created and installed
DBD += ioc_gauss.dbd

# ioc_gauss.dbd will be made up from these files:
ioc_gauss_DBD += base.dbd
ioc_gauss_DBD += stream-base.dbd
ioc_gauss_DBD += asyn.dbd
ioc_gauss_DBD += drvAsynIPPort.dbd
# Include dbd files from all support applications:
#ioc_gauss_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#ioc_gauss_LIBS += xxx
ioc_gauss_LIBS += stream
ioc_gauss_LIBS += asyn
# ioc_gauss_registerRecordDeviceDriver.cpp derives from ioc_gauss.dbd
ioc_gauss_SRCS += ioc_gauss_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
ioc_gauss_SRCS_DEFAULT += ioc_gaussMain.cpp
ioc_gauss_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#ioc_gauss_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
ioc_gauss_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE


TOP=../..

ifdef EPICS_HOST_ARCH

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# Create and install (or just install)
# databases, templates, substitutions like this
DB += digitelMpc.template
DB += digitelMpcIonp.template
DB += digitelMpcIonpSps.template
DB += digitelMpcTsp.template
DB += digitelMpcIonpGroup.template
DB += digitelMpcTspGroup.template
DB += dummyIonp.template

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE


else

include $(TOP)/config/CONFIG_APP
include $(TOP)/config/RULES_ARCHS

endif

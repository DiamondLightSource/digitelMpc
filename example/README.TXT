digitelMpc example - Pete Owens 11-10-2003
    Example to illustrate use of the digitelMpc application 

Hardware setup:
VME 64x Crate:
Slot 1: IOC - PPC 604
Slot 7: Hytec 8002 IP Carrier card -
    Slot B: Hytec 8515 Octal serial module -
        Port 4: /ty/71/4 - connected to Varian Dual ion pump controller
            Ion Pump 1: TS-VA-IONP-01
            Ion Pump 2: TS-VA-IONP-02
            TSP:        TS-VA-TSP-01
This directory contains following files:
    st.cmd                 - VxWorks startup script to initialise an IOC
    digitelMpc.sub         - substitution files to instantiate the records
    digitelMpc-launch.edl  - EDM pannel to launch panels for the conected pumps 
    startgui               - script to start off the user interface







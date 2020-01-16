/***************************************************************************************************/
/* Object name   : model.cpp                                                                       */
/* Purpose          : Determine the MPC model                               					   */
/*                                                                                                 */
/* Version details: V1.0.0 - Ian Gillingham - 13.11.19                                             */
/*                                                                                                 */
/* History            : V1.0.0 First release                                                       */
/*                                                                                                 */
/*                                                                                                 */
/***************************************************************************************************/


#include <ctype.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <subRecord.h>
#include <recSup.h>
#include <math.h>

#include <shareLib.h>
#include <devSup.h>

#include <dbDefs.h>
#include <registryFunction.h>
#include <epicsExport.h>
#include <epicsExit.h>
#include <epicsThread.h>
#include <iocsh.h>
#include <aSubRecord.h>

#define NUMINP 1
#define SEVR_INVALID 3

// Mappings of Model strings and enumerations
#define MPC2 0
#define MPCE 1
#define MPCQ 2
#define MPC2_STR "MPC DD"
#define MPCE_STR "MPCe"
#define MPCQ_STR "MPCq"

typedef int bool;
#define TRUE  1
#define FALSE 0

static int iDebug = 0;

void modelDebug(int debug)
	{
	iDebug = debug;
	}

/*******************************************************************************
* modelInit
* Initialisation function - Does nothing
*/
long modelInit (aSubRecord *psub)
    {
    return 0;
    }

long modelCalc(aSubRecord *p_gSub)
	{
	long lRet = 0;

	/* Hookup the inputs and outputs */
	char *inmodel = (char *)p_gSub->a;

	short *pdModel = (short *)p_gSub->vala;

    bool foundMPC2 = (strstr(inmodel, MPC2_STR) != NULL);
    bool foundMPCe = (strstr(inmodel, MPCE_STR) != NULL);
    bool foundMPCq = (strstr(inmodel, MPCQ_STR) != NULL);

	if ( iDebug > 0 )
		{
		// printf("modelCalc processed\n");
		}

    if (foundMPC2)
        {
        pdModel[0] = MPC2;
        }
    else if (foundMPCe)
        {
        pdModel[0] = MPCE;
        }
    else if (foundMPCq)
        {
        pdModel[0] = MPCQ;
        }

    if (iDebug != 0)
        {
        printf("MPC model: %s  enumerated: %d\n", inmodel, pdModel[0]);
        }

	return(lRet);
	} /* model */

// ---------------------------

epicsRegisterFunction(modelInit);
epicsRegisterFunction(modelCalc);

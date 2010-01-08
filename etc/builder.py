from iocbuilder import AutoSubstitution, Substitution, SetSimulation, ModuleBase
from iocbuilder.modules.streamDevice import AutoProtocol
from iocbuilder.arginfo import *

class digitelMpc(AutoSubstitution):
    # Make sure unit is a 2 digit int
    def __init__(self, **args):
        if "unit" in args:
            args["unit"] = "%02d" % int(args["unit"])
        self.__super.__init__(**args)
        
    # Substitution attributes
    TemplateFile = 'digitelMpc.template'
    
    # AutoProtocol attributes
    ProtocolFiles = ['digitelMpc.proto']

# Simulation has a different db
class digitelMpc_sim(Substitution):
    TemplateFile = 'simulation_digitelMpc.template'        
SetSimulation(digitelMpc, digitelMpc_sim)

class digitelMpcPump(ModuleBase):
    pass
        
class digitelMpcTsp(AutoSubstitution, digitelMpcPump):
    TemplateFile = 'digitelMpcTsp.template'

class _digitelMpcIonpTemplate(AutoSubstitution):
    TemplateFile = 'digitelMpcIonp.template'    

class digitelMpcIonp(_digitelMpcIonpTemplate, digitelMpcPump):
    __doc__ = _digitelMpcIonpTemplate.__doc__
    # Just pass the arguments straight through
    def __init__(self, MPC, **args):
        args['port'] = MPC.args['port']
        args['unit'] = MPC.args['unit']
        self.__super.__init__(**args)

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        MPC    = Ident ('digitelMPC object', digitelMpc)) + \
        _digitelMpcIonpTemplate.ArgInfo.filtered(without = ['port', 'unit'])

# Simulation has a different db
class digitelMpcIonp_sim(digitelMpcIonp):
    TemplateFile = 'simulation_digitelMpcIonp.template'
SetSimulation(digitelMpcIonp, digitelMpcIonp_sim)
            
class digitelMpcIonpGroup(AutoSubstitution):
    TemplateFile = 'digitelMpcIonpGroup.template'

class digitelMpcTspGroup(AutoSubstitution):
    TemplateFile = 'digitelMpcTspGroup.template'

class dummyIonp(AutoSubstitution):
    TemplateFile = 'dummyIonp.template'

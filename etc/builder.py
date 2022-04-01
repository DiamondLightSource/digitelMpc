from iocbuilder import AutoSubstitution, Substitution, SetSimulation, ModuleBase, Device
from iocbuilder.modules.streamDevice import AutoProtocol
from iocbuilder.arginfo import *
from iocbuilder.modules.calc import Calc
from iocbuilder.modules.asyn import AsynIP

class digitelMpcPump(ModuleBase):
    pass

class _digitelMpcTemplate(AutoSubstitution ):
    TemplateFile = 'digitelMpc.template'

class digitelMpc(digitelMpcPump, AutoProtocol):
    # Make sure unit is a 2 digit int

    Dependencies = (Calc, )
    ProtocolFiles = ['digitelMpc.proto']

    def __init__(self,name,device,port, unit = "01", proto = "digitelMpc.proto"):
        self.__super.__init__()
        self.name = name
        self.device = device
        self.port = port
        self.unit = unit
        self.proto = proto
        _digitelMpcTemplate(device=self.device,port=self.port,unit=self.unit,proto=self.proto)

    ArgInfo = makeArgInfo(__init__,
        name = Simple("Gui tag",str),
        device = Simple("Device name",str),
        port = Ident("Asyn port",AsynIP),
        unit = Choice("Unit number for multi drop serial",["%02d" % unit for unit in range(1,33)]),
        proto = Choice("Protocol file to use", ["digitelMpc.proto","digitelMpcq.proto"]),
    )
    
   

class digitelMpcTsp(AutoSubstitution, digitelMpcPump):
    TemplateFile = 'digitelMpcTsp.template'

class digitelMpcqTsp(AutoSubstitution, digitelMpcPump):
    TemplateFile = 'digitelMpcqTsp.template'
   
class _digitelMpcIonpTemplate(AutoSubstitution):
    TemplateFile = 'digitelMpcIonp.template'

class digitelMpcIonp(_digitelMpcIonpTemplate, digitelMpcPump):
    __doc__ = _digitelMpcIonpTemplate.__doc__
    # Just pass the arguments straight through
    def __init__(self, MPC, **args):
        args['port'] = MPC.port
        args['unit'] = MPC.unit
        self.__super.__init__(**args)

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        MPC    = Ident ('digitelMPC object', digitelMpc),
        proto = Choice("Protocol file to use", ["digitelMpc.proto","digitelMpcq.proto"])) + \
        _digitelMpcIonpTemplate.ArgInfo.filtered(without = ['port', 'unit','proto'])

class digitelMpcIonpGroup(AutoSubstitution):
    TemplateFile = 'digitelMpcIonpGroup.template'

class digitelMpcTspGroup(AutoSubstitution):
    TemplateFile = 'digitelMpcTspGroup.template'

class dummyIonp(AutoSubstitution):
    TemplateFile = 'dummyIonp.template'

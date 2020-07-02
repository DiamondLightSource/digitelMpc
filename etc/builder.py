from iocbuilder import AutoSubstitution, Substitution, SetSimulation, ModuleBase
from iocbuilder.modules.streamDevice import AutoProtocol
from iocbuilder.arginfo import *
from iocbuilder.modules.calc import Calc
from iocbuilder.modules.asyn import AsynIP

class digitelMpcPump(ModuleBase):
    pass

class _digitelMpcTemplate(AutoSubstitution,AutoProtocol ):
    TemplateFile = 'digitelMpc.template'

class digitelMpc(_digitelMpcTemplate,digitelMpcPump):
    # Make sure unit is a 2 digit int
    def __init__(self,unit = "01", proto = "digitelMpc.proto",**args):
        self.__super.__init__(**args)
    # Dependencies
    Dependencies = (Calc, )


    # AutoProtocol attributes
    ProtocolFiles = ['digitelMpc.proto']

    ArgInfo = makeArgInfo(__init__,
        port = Ident("Asyn port",AsynIP),
        unit = Choice("Unit number for multi drop serial",["%02d" % unit for unit in range(1,33)]),
        proto = Choice("Protocol file to use", ["digitelMpc.proto","digitelMpcq.proto"])) + \
        _digitelMpcTemplate.ArgInfo.filtered(without = ['a', 'c'])
    
   

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
        args['port'] = MPC.args['port']
        args['unit'] = MPC.args['unit']
        self.__super.__init__(**args)

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        MPC    = Ident ('digitelMPC object', digitelMpc)) + \
        _digitelMpcIonpTemplate.ArgInfo.filtered(without = ['port', 'unit'])

class digitelMpcIonpGroup(AutoSubstitution):
    TemplateFile = 'digitelMpcIonpGroup.template'

class digitelMpcTspGroup(AutoSubstitution):
    TemplateFile = 'digitelMpcTspGroup.template'

class dummyIonp(AutoSubstitution):
    TemplateFile = 'dummyIonp.template'

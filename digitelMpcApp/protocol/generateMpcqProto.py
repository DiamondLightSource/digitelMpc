import os
from collections import OrderedDict
from subprocess import Popen, PIPE

def readProtocol(protocolFile):

    inputFile = open(protocolFile,"r")
    functions = OrderedDict()
    parameters = list()
    function = ""
    inFunction = False
    openParenthesesCount = 0
    closeParenthesesCount = 0

    for line in inputFile:
        if(line[0][0] != '#' and line[0][0] != '\n'):
            if(inFunction == False and '{' not in line):
                parameters.append(line)
            if('{' in line and inFunction == False):
                inFunction = True
                openParenthesesCount += line.count('{')
                closeParenthesesCount += line.count('}')
                function+=line

            elif(inFunction):
                openParenthesesCount += line.count('{')
                closeParenthesesCount += line.count('}')
                function+=line
                    
            if(openParenthesesCount == closeParenthesesCount and inFunction == True):
                inFunction = False
                openParenthesesCount = 0
                closeParenthesesCount = 0
                methodName = function.split()[0]
                functions[methodName]=function[len(methodName):]
                function = ""

    return functions,parameters
                

baseFunctions,baseParam = readProtocol("digitelMpc.proto")

# Find file  with the string "Override" in them
overrideFiles = Popen("ls | grep '.override'",shell=True,stdout=PIPE).stdout.read().decode().split('\n')[:-1]

for overrideFile in overrideFiles:
    # Read in Override file
    overrideFunctions,parameters = readProtocol(overrideFile)
    # Replace functions in baseFunctions if they appear in the override file
    for overrideFunction in overrideFunctions:
        if(overrideFunction in baseFunctions):
            baseFunctions[overrideFunction]=overrideFunctions[overrideFunction]
    
    # Create protocol file
    outputFileName = overrideFile.replace('.override','.proto')
    outputProto = open(outputFileName,'w')

    for parameter in baseParam:
        outputProto.write(parameter)
    for function in baseFunctions:
        outputProto.write(function + baseFunctions[function])
        outputProto.write('\n')
    outputProto.close()
    os.system('mv %s ../../data'%outputFileName)

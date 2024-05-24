#!env python

# This script generates the digitelMpcq.proto (MPCq) file by taking all functions from digitelMpc.proto (MPCe) as a base function set.
# It then reads the digitelMpcq.override file and replaces any functions from digitelMpc.proto with the version found in digitelMpcq.override.
# In addition it also adds any functions that are found in digitelMpcq.override that are not found in digitelMpc.proto.
# The purpose of this script is to avoid duplicating many of the common functions found in both controller types

# Definitions:
#   parameter   -   streamDevice parameter, eg replytimeout = 1000
#   function    -   streamDevice function.

import os
from collections import OrderedDict
from subprocess import PIPE, Popen


def readProtocol(protocolFile):
    inputFile = open(protocolFile, "r")
    functions = OrderedDict()
    parameters = list()
    function = ""
    inFunction = False
    openParenthesesCount = 0
    closeParenthesesCount = 0

    for line in inputFile:
        if line[0][0] != "#" and line[0][0] != "\n":
            if inFunction == False and "{" not in line:
                parameters.append(line)
            if "{" in line and inFunction == False:
                inFunction = True
                openParenthesesCount += line.count("{")
                closeParenthesesCount += line.count("}")
                function += line

            elif inFunction:
                openParenthesesCount += line.count("{")
                closeParenthesesCount += line.count("}")
                function += line

            if openParenthesesCount == closeParenthesesCount and inFunction == True:
                inFunction = False
                openParenthesesCount = 0
                closeParenthesesCount = 0
                methodName = function.split()[0]
                functions[methodName] = function[len(methodName) :]
                function = ""

    return functions, parameters


# Read in the digitelMpc.proto file. This will be the basis for the digitelMpcq.proto file.
baseFunctions, baseParam = readProtocol("digitelMpc.proto")

# Find file  with the string "override" in them
overrideFiles = (
    Popen("ls | grep '.override'", shell=True, stdout=PIPE)
    .stdout.read()
    .decode()
    .split("\n")[:-1]
)

for overrideFile in overrideFiles:
    # Read in Override file
    overrideFunctions, parameters = readProtocol(overrideFile)
    # Replace functions in baseFunctions if they appear in the override file
    for overrideFunction in overrideFunctions:
        if overrideFunction in baseFunctions:
            baseFunctions[overrideFunction] = overrideFunctions[overrideFunction]

    # Create protocol file
    outputFileName = overrideFile.replace(".override", ".proto")
    outputProto = open(outputFileName, "w")

    outputProto.write(f"# File was generated from {__file__}, do not modify \n")

    for parameter in baseParam:
        outputProto.write(parameter)
    for function in baseFunctions:
        outputProto.write(function + baseFunctions[function])
        outputProto.write("\n")
    for overrideFunction in overrideFunctions:
        if overrideFunction not in baseFunctions:
            outputProto.write(overrideFunction + overrideFunctions[overrideFunction])
            outputProto.write("\n")

    outputProto.close()
    os.system("mv %s ../../data" % outputFileName)

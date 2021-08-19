# Gives a list of input pins, output pins and parameters for given design

def verilogFileParser (verilogFile):
    import re

    moduleRegex = re.compile(r'(module )(.*)( (#)?\()')

    portRegex = re.compile(r'''(
    ((in|out)put)       #port declaration
    (\s)+
    (\w{3,4})*               #wire/reg
    (\s)*
    (\[[A-Z-]*(\d)* : [A-Z-]*(\d)*])?  #if vector
    (\s)*
    (\w+)               #name
    (,|;)?             #seperator
    )''', re.VERBOSE)
    
    #CHANGE: think about what to do for declarations like input clk, reset..

    parameterRegex = re.compile(r'''(
    (parameter)         #declaration
    (\s)+
    [A-Z_0-9]+               #name
    (\s)*
    =    
    (\s)*               
    ([A-Za-z0-9']+)               #value
    (,|\;)+               #end  
    )''', re.VERBOSE)

    #access Verilog file
    fileObject = open(verilogFile)
    text = fileObject.read()

    #Find Module name
    mo = moduleRegex.search(text)
    moduleName = mo.group(2)
    
    #open a file to write to
    fileName = 'LOG{name}.txt'.format(name = moduleName)
    writeFileObject = open(fileName, 'w')
    writeFileObject.write("The design is of a:\n\t%s\n" %moduleName)
    
    #ports
    po = portRegex.findall(text)
    ports = []
    for i in po:
        ports.append(i[0])
        inputs = []
        outputs = []
    for i in ports:
        name = str(i)
        if name[0:5] == 'input':
            inputs.append(name)
        else:
            outputs.append(i)
    writeFileObject.write("List of input ports:\n\t%s\n" %inputs)
    writeFileObject.write("List of output ports:\n\t%s\n" %outputs)

    #CHANGE: format the ports how they are saved using groups

    #parameters
    lo = parameterRegex.findall(text)
    parameters = []
    for i in lo:
        parameters.append(i[0])
    writeFileObject.write("List of parameters:\n\t%s" %parameters)     



import sys

if len(sys.argv) > 2:
    print("Invalid number of arguements")
    sys.exit()

else:
    text = sys.argv[1]
    verilogFileParser(text)
    



                       

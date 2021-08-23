# Gives a list of input pins, output pins and parameters for given design

def verilogFileParser (verilogFile):
    import re

    moduleRegex = re.compile(r'(module )(.*)((\s)+(#)?\()')

    portRegex = re.compile(r'''(
    ((in|out)put)       #port declaration
    (\s)+
    (reg|wire|logic|bit)?               #wire/reg
    (\s)*
    (\[[A-Z-_0-9\s]*:[A-Z-_0-9\s]*\])?  #if vector
    (\s)*
    (\w+)                 #name
    (,|;|\))?             #seperator
    )''', re.VERBOSE)

    parameterRegex = re.compile(r'''(
    (parameter)         #declaration
    (\s)+
    ([A-Z_0-9]+)               #name
    (\s)*
    (=)    
    (\s)*               
    ([A-Za-z0-9']+)               #value
    (,|;|\))+               #end  
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
        item = [i[1], i[4], i[6], i[8]]
        for x in item :
            if '' in item :
                item.remove('')
        item = " ".join(item)
        ports.append(item)
        inputs = []
        outputs = []
    for name in ports:
        
        if name[0:5] == 'input':
            inputs.append(name[6:])
        else:
            outputs.append(name[7:])
    writeFileObject.write("List of input ports:\n\t%s\n" %inputs)
    writeFileObject.write("List of output ports:\n\t%s\n" %outputs)

    
    #parameters
    lo = parameterRegex.findall(text)
    parameters = []
    for i in lo:
        item = [i[3], i[5], i[7]]
        if '' in item : item.remove('')
        item = " ".join(item)
        parameters.append(item)
    writeFileObject.write("List of parameters:\n\t%s" %parameters)     

    print("Results can be viewed from %s" %fileName)
    


import sys

if len(sys.argv) > 2:
    print("Invalid number of arguements")
    sys.exit()

else:
    text = sys.argv[1]
    verilogFileParser(text)
    



                       

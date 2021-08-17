# Gives a list of input pins, output pins and parameters for given design

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
(,|;)?
                #seperator
)''', re.VERBOSE)

#think about what to do for declarations like input clk, reset..

parameterRegex = re.compile(r'''(
(parameter)         #declaration
(\s)+
[A-Z]+               #name
(\s)*
=    
(\s)*               
(\w+)               #value
(,|\;)+               #end  
)''', re.VERBOSE)

#parameters with vector spec

#access verilog file
fileObject = open(r'MUX.v')
text = fileObject.read()

#Find Module name
mo = moduleRegex.search(text)
moduleName = mo.group(2)
print("The design is of a:\n\t%s\n" %moduleName)

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
print("List of input ports:\n\t%s\n" %inputs)
print("List of output ports:\n\t%s\n" %outputs)

#format the ports how they are saved using groups

#parameters
lo = parameterRegex.findall(text)
parameters = []
for i in lo:
    parameters.append(i[0])
print("List of parameters:\n\t%s" %parameters)     


#write to a new file


                       

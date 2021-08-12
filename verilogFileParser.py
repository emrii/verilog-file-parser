# Gives a list of input pins, output pins and parameters for given design

import re

portRegex = re.compile(r'''(
((in|out)put)       #port declaration
(\s)+
(\w{3,4})               #wire/reg
(\s)+
([A-Z-]+(\d)+ : (\d)+])?  #if vector
(\s)?
(\w+)               #name
(,)?                #seperator
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
(,|;)               #end  
)''', re.VERBOSE)


text = '''
module MUX (in, sel, out);

   parameter LEN = 8;
   parameter LINES = 3; //2**3 = 8

   input wire  [LEN-1:0] in;
   output wire 		out;

   input wire [LINES-1:0] sel;

   assign out = in[sel];
'''


mo = portRegex.findall(text)
print(mo)
lo = parameterRegex.findall(text)
print(lo)



                       

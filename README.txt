Access Verilog design files, parse through it to identify the input output ports and the paarmeters being used in the module.

1. Takes Verilog File to be parsed as a command line arguement
2. Generates a list of Module name, Ports and Parameters of the design
3. Writes the results to a text file named LOG<ModuleName>.txt

FUTURE IMPROVEMENTS
 Currently it is assumed that prevalent verilog coding style is used in the file

 Aim is to make it possible to derive the same results when following style of declaration is used in RTL code:
     	   input x, y, z;

## Common tools:
* objdump - linux CLI disassembler
* gdb - linux CLI debugger
* binwalk - examines binary images for embedded files
* IDA Pro - commerical disassembler and decompile (expensive, but demo versions free). 
* Ghida - new open-source tool created by the NSA

```
$ strings <filename>
$ file < filename>
```

determine the type of executable
* ELF - 'Executable and Linux Format': LInux program
* PE - portable executable: Windows program
* AIF - 'ARM Image format': Embedded systems

Reverse Engineering - Entry Level Challenges
* Run the program to see what it does!
* 'Fuzz' the program to see if you can make it fail un-gracefully

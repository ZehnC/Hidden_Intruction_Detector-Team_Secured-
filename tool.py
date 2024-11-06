import os
import random
import math
import textwrap
import time

# functions
def getRandomHex():
    ins = random.randint(1,4294967296) # max value of 32 bit hex
    # 4294967296
    ins = hex(ins)[2:]
    #b = '%x' % ins
    print(ins)
    return ins

# test function
def fileMatch():
    print("opening file")
    filename = "test.txt"
    string_find = 'findme'
    with open(filename,'r') as file:
        for lines in file:
            if string_find in lines:
                print(lines)

def getAddresss(address):

    last = address[-4:] # last 4 digits
    return int(last, 16)

   # return
    #


# adds instruction based on line number of .mem file
def addInstructionMem(lineNum, content , filename): # line num is an int, content is the address which is string, filename is a string
    # iterate through the file and find the exact address from the end of the file name
    # conversion into string
    addr = list(map(''.join, zip(*[iter(content)]*2)))
    print(addr)
    #lineNum += 1
    count = 0
    i = 0;

    with open(filename,'r') as file:
        lines = file.readlines()
            #if lineNum+1 >= count and count < lineNum+4:
             #print(line)
        #file.write('')

    with open(filename,'w') as file:
        #file.truncate()

        # little endian followed
        lines[lineNum] = addr[3] + "\n" #
        lines[lineNum+1] = (addr[2]) + "\n"
        lines[lineNum+2] = (addr[1]) + "\n"
        lines[lineNum+3]  = addr[0] + "\n"
        #write line to file
        ##for line in lines:
          ##  print(line)
        file.seek(0)
        for line in lines:
            file.write(line)

        #file.write(addr[i])
        #i += 1

#instruction comparison checker that takes three textfiles as input
def compInstruction(testLog, spikeLog, cvaLog):
    #setting up the textlists to compare

    #Opening the input file and putting the information needed(40 test cases) into a list
    testList = []
    with open(testLog, 'r') as file:
        line = file.readline()
        trig = 0
        cnt = 0
        while "<main>:" not in line:
            line = file.readline()
        for i in range(0, 40):
            testList.append(file.readline())

    #Opening the spike output file and putting the information needed into a list
    spikeList = []
    with open(spikeLog, 'r') as file:
        for i in range(0, 69):
            file.readline()
        for i in range(0, 40):
            spikeList.append(file.readline())

    #Opening the cva6 output file and putting the information needed into a list
    cvaList = []
    with open(cvaLog, 'r') as file:
        for i in range(0, 69):
            file.readline()
        for i in range(0, 40):
            cvaList.append(file.readline())

    #Looping through the lists
    for i in range(0, 40):

        #checking incase an exception illegal instruction is found
        if spikeList[i].find("exception") >= 0 or cvaList[i].find("Exception") >= 0:
            i+=2
        if i >= 40:
            break

        #Getting the addresses from the lists
        testAdr = testList[i][4:12]
        spikeAdr = spikeList[i][20:28]
        cvaAdr = cvaList[i][30:38]

        #prints for testing if the correct information is being recorded
        #print(testList[i])
        # print(testAdr)
        # print(spikeList[i])
        # print("Spike Address:", i , "is" , spikeAdr)
        # print(cvaList[i])
        # print("Cva Address:" , i , "is" , cvaAdr)

        #Getting instructionID from the lists
        testID = testList[i][14:22]
        spikeID = spikeList[i][32:40]
        cvaID = cvaList[i][41:49]

        #prints for testing if the correct information is being recorded
        #print(testList[i])
        #print(testID)
        # print(spikeList[i])
        # print(spikeID)
        # print(cvaList[i])
        # print(cvaID)

        #Getting instruction Results(action) from the lists
        #taking length-1 so the '\n' is not included
        testRes = testList[i][33:len(testList[i])-1]
        spikeRes = spikeList[i][42:len(spikeList[i])-1]
        cvaRes = cvaList[i][50:len(cvaList[i])-1]

        #prints for testing if the correct information is being recorded
        #print(testList[i])
        # print(testRes)
        # print(spikeList[i])
        # print(spikeRes)
        # print(cvaList[i])
        # print(cvaRes)

        #Begin Comparing the information
        #Comparing given hexcodes(input) with the results from spike
        if testAdr == spikeAdr and testID == spikeID:

            #Comparing the Spike address with the CVA6 address
            if spikeAdr == cvaAdr:

                #Comparing the Spike instruction with the CVA6 instruction
                if spikeID == cvaID:

                    #Creating temp files to split up the resulting actions of Spike and CVA6
                    temp = spikeRes.split(" ")
                    temp2 = cvaRes.split(" ")
                    cnt = 0

                    #loop to go through the split up Spike result
                    for i in range(0, len(temp)):
                        #making sure we are not comparing a blank space
                        if temp[i] != '':

                            #Counter to keep track of where we are in the CVA6 split up result(temp2)
                            while temp2[cnt] == '':
                                cnt+=1

                            #comparing the Spike and CVA6 Result
                            if temp[i] != temp2[cnt]:
                                print("The results of Spike and Cva6 are not the same")
                                print("The Address of Spike is" , spikeAdr, "The Instruction for Spike is", spikeID, "The result of Spike is", spikeRes)
                                print("The Address of Cva6 is" , cvaAdr, "The Instruction for Cva6 is", cvaID, "The result of Cva6 is", cvaRes, "\n")
                                #Creating textfiles for Hidden Instructions
                                HdInstruc = open("HiddenInstructions.txt", "a+")
                                temptext = "Address:" + spikeAdr + "   Instruction:" + spikeID + "   Result of Spike:" + spikeRes + "   Result of CVA6:" + cvaRes + "\n"
                                HdInstruc.write(temptext)
                                #Closing File
                                HdInstruc.close()
                                break
                            elif i == len(temp)-1:
                                #Creating textfile for Normal Instructions
                                KnInstruc = open("KnownInstructions.txt", "a+")
                                temptext = "Address:" + spikeAdr + "   Instruction:" + spikeID + "   Result:" +  spikeRes + "\n"
                                KnInstruc.write(temptext)
                                #Closing File
                                KnInstruc.close()
                            cnt+=1

                #Else function if the Instructions for Spike and CVA6 do not match
                else:
                    print("The Instruction ID of Spike and Cva6 are not the same")
                    print("The Address for this Instruction is", spikeAdr)
                    print("The Instruction of Spike is" , spikeID)
                    print("The Instruction of Cva6 is" , cvaID, "\n")

            #Else function if the Address of Spike and CVA6 do no match
            else:
                print("The Address of Spike and Cva6 are not the same")
                print("The Address of Spike is" , spikeAdr)
                print("The Address of Cva6 is" , cvaAdr, "\n")

        #Else function if the Address or Intrsuctions of the Given HexCode(input) and Spike do not match
        else:
            print("The Address or Instruction ID of the Test and Spike are not the same")
            print("The result of Test address is" , testAdr, "The result of the Test Instruction is", testID)
            print("The result of Spike address is" , spikeAdr, "The result of the Spike Instruction is", spikeID, "\n")

    #print(testAdr)


'''
2. Setup the environment
    RUN ALL THESE WITH OS.

   os.system('source /opt/coe/mentorgraphics/modelsim/setup.modelsim.bash')

   os.system('export PROJECT_HOME=$PWD/ecen426_class_project/')
   os.system('export TOOL_DIR=$PROJECT_HOME/tools')
   os.system ('export PATH=$PATH:$TOOL_DIR/install/bin')
   os.system('export RISCV=$TOOL_DIR/install')
   os.system('export PATH=$TOOL_DIR/verilator/usr/bin:$PATH')

    os.system('export PATH=$TOOL_DIR/modelsim/bin:$PATH')
    os.system('export MODELSIM_PATH=$TOOL_DIR/modelsim/bin')

   os.system('cd $TOOL_DIR')
  os.system(' cd riscv-fesvr')
   os.system('cd build')
   os.system('../configure --prefix=$RISCV --target=riscv64-unknown-elf')
   os.system('make -j $(nproc); make install')
	os.system('cd')

'''

'''
2. Run the simulation
   cd $PROJECT_HOME/soc/cva6 - NOT NECESSARY SINCE TOOL WILL RUNNING HERE

   make sim preload=<.mem file> spike-tandem=1 batch-mode=1 2> spike_out.log

	For ex: make sim preload=my_run_0.mem spike-tandem=1 batch-mode=1  2> spike_out.log

'''

'''

// AUTOMATION NEEDED

1.
 os.system ('make sim preload=my_run_0.mem spike-tandem=1 batch-mode=1  2> spike_out.log')

2. time.sleep(20) # sleep for 20 seconds

    os.system('^C') # kill the simulation

 2.
('riscv64-unknown-elf-objdump -D <.riscv file> > test.dump')

 Ex:
os.system ('riscv64-unknown-elf-objdump -D  my_run_0.riscv > test.dump')


'''
#os.system('cd')
#time.sleep(2)
#os.system("ls") # print directly to the terminal

print("start")

#testing the compare function

compInstruction("testCopy.dump", "spike_outCopy.log", "trace_hart_0Copy.log")

val = getRandomHex()

s = str(val )

# getAddresss(s) use as the input for addInstructionMem( first field)

print (getAddresss(s))

#print (addr)

#addInstructionMem(5, s, "test.txt")

#os.system('cd -')
#os.system("ls") # print directly to the terminal

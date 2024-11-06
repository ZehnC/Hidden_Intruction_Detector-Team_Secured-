import os
import random
import math
import textwrap
import time

from subprocess import call
import threading

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
    #addr = list(map(''.join, zip(*[iter(content)]*2)))
    addr = []
    addr.append(content[0:2])
    addr.append(content[2:4])
    addr.append(content[4:6])
    addr.append(content[6:])

   
    print(addr)
    #lineNum += 1
    count = 0
    i = 0;

    with open(filename,'r') as file:
        lines = file.readlines()
            #if lineNum+1 >= count and count < lineNum+4:
             #print(line)
        #file.write('')
        if len(lines) == 0:
            print("empty file")
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

        #Getting the addresses from the lists
        testAdr = testList[i][4:12]
        spikeAdr = spikeList[i][20:28]
        cvaAdr = cvaList[i][30:38]

        #prints for testing if the correct information is being recorded
        print(testList[i])
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
        print(testID)
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
        print(testList[i])
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
                                break
                            cnt+=1

                #Else function if the Instructions for Spike and CVA6 do not match
                else:
                    print("The Instruction ID of Spike and Cva6 are not the same")
                    print("The Address for this Instruction is", spikeAdr)
                    print("The Instruction of Spike is" , spikeID)
                    print("The Instruction of Cva6 is" , cvaID, "\n")
                    exit() # leave the program

            #Else function if the Address of Spike and CVA6 do no match
            else:
                print("The Address of Spike and Cva6 are not the same")
                print("The Address of Spike is" , spikeAdr)
                print("The Address of Cva6 is" , cvaAdr, "\n")

        #Else function if the Address or Intrsuctions of the Given HexCode(input) and Spike do not match
        '''
        else:
            print("The Address or Instruction ID of the Test and Spike are not the same")
            print("The result of Test address is" , testAdr, "The result of the Test Instruction is", testID)
            print("The result of Spike address is" , spikeAdr, "The result of the Spike Instruction is", spikeID, "\n")
        '''
    #print(testAdr)



def wait_timeout(proc, seconds):
    start = time.time()
    end = start + seconds
    interval = min(seconds / 1000.0, .25)

    while True:
        result = proc.poll()
        if result is not None:
            return result
        if time.time() >= end:
            raise RuntimeError("Process timed out")
        time.sleep(interval)



print("start")

#testing the compare function

#compInstruction("testCopy.dump", "spike_outCopy.log", "trace_hart_0Copy.log")

#vals = []

start = '8000258c'
dummy = int(start, 16)
s = hex(dummy)
print ('s:' , s)

for i in range(0, 39):
    ins = (getRandomHex())
    st = str(s)  
    lineNum = getAddresss(st)
    print(str(st))
    print('lineNum on .mem',lineNum)
    addInstructionMem(lineNum, str(ins), 'my_run_0.mem')
    #time.sleep(2)
    print ('line: ', str(lineNum), 'instruction: ', ins)
    #basehexin = int(s, 16)
    #echexin = int(4, 16)
    d = int(s, 16)
    d += 4
    s = hex(d)
    
    #s += 4
    #vals.append(compInstruction(testList[i], spikeList[i], cvaList[i]))

#val = getRandomHex()


# getAddresss(s) use as the input for addInstructionMem( first field)


# starting for address 

#print (addr)


#p = subprocess.run("exec " + " make sim preload=my_run_0.mem spike-tandem=1 batch-mode=1  2> spike_out.log", stdout=subprocess.PIPE, shell=True)
#time.wait(p.stdout.read)

#print(os.getcwd())


#os.system('. ./scr.sh')

#p = subprocess.run("./scr.sh"  ,stdout=subprocess.PIPE, shell=True)


#rc = call("./scr.sh", shell = True)




#

print('graceful exit')

#make_process = subprocess.Popen("", stdout=subprocess.PIPE)
#, shell=True)
#e = threading.Event()
#t = threading.Thread(target=os.system('make sim preload=my_run_0.mem spike-tandem=1 batch-mode=1  2> spike_out.log'))
#t.start()

# Team_Secured_Hidden_Instructure_Project

Created in Ubuntu 20.0.1 Linux in enviroment by using python 3.9

Functionality:

    run . ./auto.sh 
    in home directory and this will work
    . used to execute commands on the actual terminal NOT A CHILD subprocess

    auto.sh executes both the prereqs and then 
    an infinite loop of instruction generation,
    modelsim simulation, and instruction checker
    


Tasks:

    1. Run command line prompts from python script
    2. Generate a 32 bit random integer and convert into hex : DONE
    3. 
        find the values of the instruction in the dump file where we have 
        open spots for the production  [0x80002590   ,0x80002628] - 40 random instructions to deal with

        USE THIS ADDRESS SPACE

    3a. find the place in the file of my_run_0 obj and modify the values RPE -> DONE

    using little endian -> have this function 
    4. compare the dump file with cv6 log file 
    
    SPIKE LOG is garbage rn - run again

    5. now compare the cv6 log file with the spike log file

    if cv6  runs it but not in spike log - then we have a problem and need to report to user
    

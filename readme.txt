Steps 


#Do these steps one time on tamu servers (dont switch or close terminals during the entire process)

1. ssh into the tamu servers (ssh -Y <tamu username>@olympus.ece.tamu.edu)

2. Go to a location in the terminal where you want to install the setup

3. Create the folders

   mkdir ecen426_class_project
   cd ecen426_class_project
   export PROJECT_HOME=$PWD
   mkdir tools soc

4. Install the gcc tool
   cd $PROJECT_HOME/tools
   export TOOL_DIR=$PWD 
   ls // i should see install.zip
   unzip install.zip
   ls // install
   ls install // bin include ...
   // copy the compiled files from your TA rahul
   // u will have to do this over a zoom call
	   export PATH=$PATH:$TOOL_DIR/install/bin
	export RISCV=$TOOL_DIR/install

5. Install the setup for baremetal compilation
   cd $PROJECT_HOME/soc
   git clone https://github.com/riscv/riscv-tests
   cd riscv-tests
   git submodule update --init --recursive
   cd benchmarks
   make all

6. Install another tool needed to simulate the cv6 SoC
   cd $TOOL_DIR
   git clone https://github.com/riscv/riscv-fesvr.git
   cd riscv-fesvr
   mkdir build ; cd build
   ../configure --prefix=$RISCV --target=riscv64-unknown-elf
   make -j $(nproc); make install


// skip
7. Install the modelsim simulation tool
      

	source /opt/coe/mentorgraphics/modelsim/setup.modelsim.bash

	
  
	
  
  
  
8. Setup the SoC
   cd $PROJECT_HOME/soc
   git clone --branch v4.2.0  https://github.com/openhwgroup/cva6.git  
   cd cva6
   git submodule update --init --recursive
   
	
	
	// DRAG & DROP in the location outlined below from drive link 
   
	cva6/tb/ariane_tb.sv
	cva6/tb/ariane_testharness.sv
	cva6/tb/common/spike.sv
	cva6/tb/dpi/spike.cc

   
   
   make build-spike
   make clean
   
   // NECESSARY - PLEASE DO THIS
   
   Open the Makefile and insert "-I/opt/coe/mentorgraphics/modelsim/modeltech/include \" at line 98
	
	/////////////////////////////////////
   
   make build preload=~/ spike-tandem=1 batch-mode=1
 	   make build preload=~/ spike-tandem=1 batch-mode=1



#Do these steps everytime you open a new terminal after the initial installation

# my location
/home/ugrads/p/pmish1/ecen426_class_project/


1. Go to the location in the terminal where you did the installation
    (if you run the 'ls' command you should see the folder 'ecen426_class_project')



2. Setup the environment
   source /opt/coe/mentorgraphics/modelsim/setup.modelsim.bash
	
   
   
   export PROJECT_HOME=$PWD/ecen426_class_project/
   export TOOL_DIR=$PROJECT_HOME/tools
   export PATH=$PATH:$TOOL_DIR/install/bin 
   export RISCV=$TOOL_DIR/install
   export PATH=$TOOL_DIR/verilator/usr/bin:$PATH
	


	
#Simulation steps

1. If you opened a new terminal setup the environment with the above steps. 

2. Run the simulation
   cd $PROJECT_HOME/soc/cva6
   
   make sim preload=<.mem file> spike-tandem=1 batch-mode=1 2> spike_out.log

	For ex: make sim preload=my_run_0.mem spike-tandem=1 batch-mode=1  2> spike_out.log
   
   
// Useful for later, (tool production)

// AUTOMATION NEEDED

1.
 make sim preload=my_run_0.mem spike-tandem=1 batch-mode=1  2> spike_out.log
 
 2.
 riscv64-unknown-elf-objdump -D <.riscv file> > test.dump
 
 Ex:
	riscv64-unknown-elf-objdump -D  my_run_0.riscv > test.dump 
 
  make sim preload=my_run_0.mem spike-tandem=1 batch-mode=1  2> spike_out.log  
 
 


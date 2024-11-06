import os
import random
import math
import textwrap
import time


os.system('source /opt/coe/mentorgraphics/modelsim/setup.modelsim.bash')

os.system('export PROJECT_HOME=$PWD/ecen426_class_project/')
os.system('export TOOL_DIR=$PROJECT_HOME/tools')
os.system ('export PATH=$PATH:$TOOL_DIR/install/bin')
os.system('export RISCV=$TOOL_DIR/install')
os.system('export PATH=$TOOL_DIR/verilator/usr/bin:$PATH')

os.system('export PATH=$TOOL_DIR/modelsim/bin:$PATH')
os.system('export MODELSIM_PATH=$TOOL_DIR/modelsim/bin')

os.system('cd $TOOL_DIR')
os.system('cd riscv-fesvr')
os.system('cd build')
os.system('../configure --prefix=$RISCV --target=riscv64-unknown-elf')
os.system('make -j $(nproc); make install')
os.system('cd')
os.system('cd $PROJECT_HOME/soc/cva6') 
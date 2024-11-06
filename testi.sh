#echo ${PROJECT_HOME}
source /opt/coe/mentorgraphics/modelsim/setup.modelsim.bash
export PROJECT_HOME=$PWD/ecen426_class_project/
export TOOL_DIR=$PROJECT_HOME/tools
export PATH=$PATH:$TOOL_DIR/install/bin 
export RISCV=$TOOL_DIR/install
export PATH=$TOOL_DIR/verilator/usr/bin:$PATH
cd $TOOL_DIR
cd riscv-fesvr
cd build
../configure --prefix=$RISCV --target=riscv64-unknown-elf
make -j $(nproc); make install
cd
cd $PROJECT_HOME/soc/cva6
ls
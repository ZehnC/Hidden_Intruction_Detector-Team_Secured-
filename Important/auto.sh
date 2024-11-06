#echo ${PROJECT_HOME}
while true
do
  #clear
  python3 changer.py # make changes to the .mem file
#  timeout 40s make sim preload=my_run_0.mem spike-tandem=1 batch-mode=1  2> spike_out.log
  sleep 3 # fix model sim bug
  python3 tester.py
  sleep 1
  #sleep 1
done

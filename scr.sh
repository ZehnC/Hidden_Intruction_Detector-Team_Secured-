while true
do
  #clear
  python3 changer.py # c
   # sleep 4
  timeout 40s make sim preload=my_run_0.mem spike-tandem=1 batch-mode=1  2> spike_out.log  
  sleep 3
  python3 tester.py
  #sleep 1
done
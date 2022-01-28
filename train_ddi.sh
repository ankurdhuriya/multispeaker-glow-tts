config=$1
modeldir=$2

init=1 # 1, start from scratch - 0, start from last checkpoint

if [[ $init -eq 1 ]]
then
  python ./init.py -c $config -m $modeldir -l $logdir
fi
python ./train.py -c $config -m $modeldir -l $logdir

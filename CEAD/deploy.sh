#/usr/bin/env bash
# __author__ = "liyc"
# __copyright__ = "Copyright 2020"
# __email__ = "liyichen2015@gmail.com"

env_tar=$1
env_name=$2


# check if conda exists.
which "conda" > /dev/null 2>&1
if [ ! $? -eq 0 ]
then
    echo conda is not exist, please install.
    exit
fi


# get conda path
CONDA_PATH=$(dirname $(dirname `which conda`))
echo Current conda path:$CONDA_PATH

pip list | grep conda-pack > /dev/null 2>&1
if [ ! $? -eq 0 ]
then
    echo conda pack is not exist, plase use pip to install.
    exit
fi


# start install the conda env.
echo strat install the conda env...
mkdir $env_name
tar -xzvf $env_tar -C $env_name > /dev/null 2>&1;
mv ./$env_name $CONDA_PATH/envs


# >>> conda init >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$(CONDA_REPORT_ERRORS=false $CONDA_PATH'/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f $CONDA_PATH"/etc/profile.d/conda.sh" ]; then
        . $CONDA_PATH"/etc/profile.d/conda.sh"
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH=$CONDA_PATH"/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda init <<<

conda activate $env_name
conda-unpack

echo Completed! Please use conda activate $env_name to use the conda env!


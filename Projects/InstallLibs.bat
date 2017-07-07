REM Run this file on PowerShell and so on as an administrator.

REM Install libraries with Anaconda.
conda create -n tensorflow python=3.5

REM After this activation, running this batch file fails.
call activate tensorflow

REM Some errors occurred, but it seems to work on GPU.
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-1.2.0-cp35-cp35m-win_amd64.whl

REM install OpenCV 3 on Python 3
REM refer to: http://qiita.com/Merdane/items/655130dfd176d8ee272e

REM if already added, it fails.
call conda config --add channels conda-forge

conda install opencv



cd darkflow
python setup.py build_ext --inplace

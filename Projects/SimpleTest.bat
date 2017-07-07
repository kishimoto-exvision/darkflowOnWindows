REM Before test, download "yolo.weights" from https://pjreddie.com/media/files/yolo.weights and copy it to "darkflow/bin/".
REM And do not forget calling "python setup.py build_ext --inplace" in the darkflow directory.

cd darkflow
python ../SimpleTest.py

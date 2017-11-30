if [ $# != 1 ]; then
    echo "./run_test.sh (fast|normal|slow)"
    exit
fi

MODE=$1
echo "Running in $MODE mode"
if [ ! -d "$MODE-sa-nn" ]; then
    mkdir $MODE-sa-nn
fi

python saDriver.py TSP_Files-1/tsp_example_1.txt $MODE > ./$MODE-sa-nn/e1.log &
python saDriver.py TSP_Files-1/tsp_example_2.txt $MODE > ./$MODE-sa-nn/e2.log &
python saDriver.py TSP_Files-1/tsp_example_3.txt $MODE > ./$MODE-sa-nn/e3.log &

python saDriver.py tsp_test_cases/test-input-1.txt $MODE > ./$MODE-sa-nn/1.log &
python saDriver.py tsp_test_cases/test-input-2.txt $MODE > ./$MODE-sa-nn/2.log &
python saDriver.py tsp_test_cases/test-input-3.txt $MODE > ./$MODE-sa-nn/3.log &
python saDriver.py tsp_test_cases/test-input-4.txt $MODE > ./$MODE-sa-nn/4.log &
python saDriver.py tsp_test_cases/test-input-5.txt $MODE > ./$MODE-sa-nn/5.log &
python saDriver.py tsp_test_cases/test-input-6.txt $MODE > ./$MODE-sa-nn/6.log &
python saDriver.py tsp_test_cases/test-input-7.txt $MODE > ./$MODE-sa-nn/7.log &

python generate_transpose.py < test.txt
rm -Rf ./models
MODEL_DIR=models 
python3 -m sockeye.train --source transpose.train.source \
                       --target transpose.train.target \
                       --encoder rnn \
                       --decoder rnn \					 
                       --validation-source transpose.dev.source \
                       --validation-target transpose.dev.target \
                       --output MODEL_DIR \
		       --decode-and-evaluate 500 
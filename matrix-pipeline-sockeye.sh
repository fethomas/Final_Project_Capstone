python3 generate_transpose.py
rm -Rf ./models
#Train
MODEL_DIR=models
python3 -m sockeye.train --source transpose.train.source \
                       --target transpose.train.target \
                       --encoder cnn \
                       --decoder cnn \
					   --rnn-cell-type lstm \
					   --max-num-epochs 300 \
                       --validation-source transpose.dev.source \
                       --validation-target transpose.dev.target \
                       --output $MODEL_DIR \
		       --decode-and-evaluate 500 
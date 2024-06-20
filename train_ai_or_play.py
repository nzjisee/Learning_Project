from q_learning import train, play, GameAI
import datetime
import argparse
import time

parser = argparse.ArgumentParser(description="Flappy Bird")
parser.add_argument("--train", action=argparse.BooleanOptionalAction, default=False,
	help='Enable or disable the training process, use --no-train to disable it')
args = parser.parse_args()

# 参数设置
alpha     = 0.5
gamma     = 0.98
epsilon   = 0
iteration = 50000
if args.train:
	now_time = datetime.datetime.now().strftime('%m%d_%H%M%S')
	# 存储Q-Function
	path = 'q_test.pkl'
	start_time = time.time()
	best_ai, best_iteration = train(iteration, alpha, gamma, epsilon)
	interval = int(time.time() - start_time)  # Get elapsed time in seconds
	minute = interval // 60
	second = interval % 60
	print("Training time:", f"{minute} min and {second} sec")
	# ai.save_q(path)
	best_ai.save_q(path)
	print(f"The best model was achieved at iteration {best_iteration}")
else:
	ai = GameAI()
	path = 'q_best.pkl'
	ai.load_q(path)
	play(ai)
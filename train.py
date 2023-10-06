from game import *
import random

class QLearningAgent:
    def __init__(self, alpha, epsilon, discount_factor):
        self.Q = {}
        self.alpha = alpha
        self.epsilon = epsilon
        self.discount_factor = discount_factor

    def get_Q_value(self, state, action):
        if (state, action) not in self.Q:
            self.Q[(state, action)] = 0.0
        return self.Q[(state, action)]

    def choose_action(self, state, available_moves):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(available_moves)
        else:
            Q_values = [self.get_Q_value(state, action) for action in available_moves]
            max_Q = max(Q_values)
            if Q_values.count(max_Q) > 1:
                best_moves = [i for i in range(len(available_moves)) if Q_values[i] == max_Q]
                i = random.choice(best_moves)
            else:
                i = Q_values.index(max_Q)
            return available_moves[i]

    def update_Q_value(self, state, action, reward, next_state):
        next_Q_values = [self.get_Q_value(next_state, next_action) for next_action in TicTacToe(next_state).available_moves()]
        max_next_Q = max(next_Q_values) if next_Q_values else 0.0
        self.Q[(state, action)] += self.alpha * (reward + self.discount_factor * max_next_Q - self.Q[(state, action)])

def train(num_episodes, alpha, epsilon, discount_factor):
    agent = QLearningAgent(alpha, epsilon, discount_factor)
    for i in range(num_episodes):
        state = TicTacToe().board
        while not TicTacToe(state).game_over():
            available_moves = TicTacToe(state).available_moves()
            action = agent.choose_action(state, available_moves)
            next_state, reward = TicTacToe(state).make_move(action)
            agent.update_Q_value(state, action, reward, next_state)
            state = next_state
    return agent

def test(agent, num_games):
    num_wins = 0
    for i in range(num_games):
        state = TicTacToe().board
        while not TicTacToe(state).game_over():
            if TicTacToe(state).player == 1:
                action = agent.choose_action(state, TicTacToe(state).available_moves())
            else:
                action = random.choice(TicTacToe(state).available_moves())
            state, reward = TicTacToe(state).make_move(action)
        if reward == 1:
            num_wins += 1
    return num_wins / num_games * 100

# Train the Q-learning agent
agent = train(num_episodes=100000, alpha=0.5, epsilon=0.1, discount_factor=1.0)

# Test the Q-learning agent
win_percentage = test(agent, num_games=1000)
print("Win percentage: {:.2f}%".format(win_percentage))
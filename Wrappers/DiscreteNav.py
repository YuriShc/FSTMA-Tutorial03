from pettingzoo.mpe import simple_v2
from gym import spaces
def make_env():
class DiscreteNav(simple_v2.raw_env):
    def __init__(self, pos_limit, pos_bins, vel_limit, vel_bins):
        super().__init__()
        self.pos_limit = pos_limit
        self.pos_bins = pos_bins
        self.vel_limit = vel_limit
        self.vel_bins = vel_bins
        self.pos_bin_size = 2 * pos_limit / pos_bins
        self.vel_bin_size = 2 * vel_limit / vel_bins

        def get_pos_idx(pos):
            if pos < - pos_limit:
                return -float('inf')
            elif pos > pos_limit:
                return float('inf')
            return (pos + pos_limit) // pos_bins

        def get_vel_idx(vel):
            if vel < - vel_limit:
                return -float('inf')
            elif vel > vel_limit:
                return float('inf')
            return (vel + vel_limit) // vel_bins

        def transform_state(state):
            self.state.agent.p_vel


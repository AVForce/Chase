import torch
SHOULD_USE_CUDA = 'cuda' if torch.cuda.is_available() else 'cpu'

# Global params
PORT = 2000  # Port on which the server is running
SCENARIO = [1, 3, 4, 5]  # List of scenarios on which the model is trained
REWARD_NUMBER = 4
SLEEP_BETWEEN_ACTIONS = 0.2  # How many sec sleep between consecutive actions? E.g: 0.2 gives 5 actions per 1 sec
# Without sleeping there are a lot of actions and those actions do not have enough time to influence the world.
LOAD_MODEL = ''  # The name of the model which you want to load in .pth format
# If you do not want to load anything keep it empty
ACTION_TYPE = 'discrete'  # 'discrete' or 'continuous'
CAMERA_TYPE = 'rgb'  # 'rgb' or 'semantic'
GAMMA = 0.9  # Discount factor
LR = 1e-4  # Learning rate
USE_ENTROPY = True  # Use entropy regularization?
SERV_RESX = 384  # Server's X resolution
SERV_RESY = 288  # Server's Y resolution
FPS = 15  # Pygame's fps. Carla server's fps seems to do not affect anything
SHOW_CAM = False  # Vehicle's camera preview
SERV_RESX = 640  # Server X resolution
SERV_RESY = 480  # Server Y resolution

TB_DESCRIPTION = f'Chase_r{REWARD_NUMBER}_sc{SCENARIO}'  # Tensorboard

""" 
Scenario parameter: {1,2,3,4,5}
1) Straight short lane
2) Straight long lane
3) Turn left
4) Slow turn left
5) Turn right

The whole list of scenarios can be specified with switch_scenario parameter indicating that
after switch_scenario episodes there will be next scenario from the list
"""

ACTIONS = ['forward', 'forward_left', 'forward_right', 'brake', 'brake_left', 'brake_right']

CARLA_PATH = r'<paste/your/path>'
CARLA_EGG_PATH = r'<paste/your/path>'

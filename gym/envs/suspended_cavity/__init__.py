from gym.envs.registration import registry, register, make, spec

# Algorithmic
# ----------------------------------------

register(
    id='FabryPerot-v1',
    entry_point       = 'gym.envs.suspended_cavity.fpcavity:FPcavEnv',
    max_episode_steps = 200,
    reward_threshold  = 25.0,
)

register(
    id='simplePendulum-v1',
    entry_point='gym.envs.suspended_cavity.fpcavity:PendulumEnv',
    max_episode_steps=200,
)

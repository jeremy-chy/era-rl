# from .sokoban import SokobanEnv,SokobanEnvConfig
# from .frozenlake import FrozenLakeEnvConfig
from .alfred.alfred_env_config_for_vagen import AlfredEnvConfig
from .ebman.ebman_env_config_for_vagen import EBManEnvConfig
# from .navigation import NavigationEnv, NavigationEnvConfig, NavigationServiceConfig, NavigationService
# from .svg import SVGEnv, SvgEnvConfig, SVGService, SVGServiceConfig
# from .primitive_skill import PrimitiveSkillEnv, PrimitiveSkillEnvConfig, PrimitiveSkillService, PrimitiveSkillServiceConfig
# from .alfworld import ALFWorldEnv, ALFWorldEnvConfig, ALFWorldService, ALFWorldServiceConfig
REGISTERED_ENV = {
    # "sokoban": {
    #     "env_cls": SokobanEnv,
    #     "config_cls": SokobanEnvConfig,
    # },
    # "frozenlake": {
    #     # "env_cls": FrozenLakeEnv,
    #     "config_cls": FrozenLakeEnvConfig,
    #     # "service_cls": FrozenLakeService
    # },
    "alfred": {
        # "env_cls": None,
        "config_cls": AlfredEnvConfig,
        # "service_cls": None
    },
    "ebman": {
        "config_cls": EBManEnvConfig,
    },
}
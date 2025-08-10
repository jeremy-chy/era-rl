from vagen.env.base.base_env_config import BaseEnvConfig
import random

class AlfredEnvConfig(BaseEnvConfig):
    def __init__(self, image_mode, image_interval):
        self.image_mode = image_mode
        self.image_interval = image_interval
    
    def config_id(self) -> str:
        return f"{self.image_mode}_{self.image_interval}"
    def get(self, key, default=None):
        return None
    def generate_seeds(self, env_size, train_size):
        import numpy as np
        
        # train_seeds = (list(range(0, 50)) + list(range(300, 350)) + list(range(400, 450))) * 100
        # train_seeds = train_seeds[:15000]

        block = list(range(0, 50)) + list(range(300, 350)) + list(range(400, 450))
        train_seeds = []
        for _ in range(100):
            group = block.copy()
            random.shuffle(group)
            train_seeds.extend(group)

        print("Generated train seeds:", train_seeds[:10], "...")  # Print first 10 seeds for verification

        # train_seeds = list(range(500, 550)) * 100
        
        # test_ranges = [(100,150), (200,250), (500,550)]
        # test_candidates = []
        # for start, end in test_ranges:
        #     test_candidates.extend(list(range(start, end)))
        # test_seeds = np.random.choice(test_candidates, size=env_size-train_size, replace=True).tolist()

        # test_seeds = list(range(0, 50)) + list(range(300, 350)) + list(range(400, 450)) + list(range(100, 150)) + list(range(200, 250))
        # test_seeds = list(range(100, 150)) + list(range(200, 250)) + [0]*2
        # test_seeds = list(range(500,550))
        test_seeds = list(range(100, 150)) + list(range(200, 250))
        # test_seeds = list(range(200, 250)) + list(range(100, 150)) + [0]*2
        
        return train_seeds + test_seeds
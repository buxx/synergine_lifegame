from synergine.core.Core import Core
from synergine_lifegame.PrintTerminal import PrintTerminal
from synergine_lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from synergine_lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from synergine_lifegame.synergy.collection.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration
from synergine_xyz.Context import Context as XyzContext
from synergine_xyz.display.PygameDisplay import PygameDisplay
from synergine_lifegame.PlotTerminal import PlotTerminal
from synergine_lifegame.display.pygame_visualisation import visualisation as pygame_visualisation

config = {
    'app': {
        'name': 'LifeGame simulation',
        'classes': {
            'Context': XyzContext
        }
    },
    'engine': {
        'fpsmax': 5,
    },
    'simulations': [LifeGameSimulation([LifeGameCollection(LifeGameCollectionConfiguration())])],
    'connections': [PrintTerminal, PygameDisplay, PlotTerminal],
    'terminal': {
        'pygame': {
            'visualisation': pygame_visualisation,
            'window_size': (700, 500),
            'display': {
                'grid': {
                    'size': 20
                }
            }
        },
    }
}

if __name__ == '__main__':
    # Run simulation
    Core.start_core(config)
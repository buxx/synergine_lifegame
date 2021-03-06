from synergine_xyz.display.object.TextTraceVisualisation import TextTraceVisualisation
from synergine_lifegame.synergy.object.Cell import Cell


def is_old_cell(cell, context):
    if cell.is_alive():
      if cell.get_is_alive_since() < 1:
          return TextTraceVisualisation('o')
      elif cell.get_is_alive_since() == 1:
          return TextTraceVisualisation('O')
      else:
          return TextTraceVisualisation('0')
    else:
        return TextTraceVisualisation(' ')

visualisation = {
    'window': {},
    'objects': {
        #SynergyObject: {
        #    'default': TextTraceVisualisation('*')
        #},
        Cell: {
            'default': TextTraceVisualisation('*'),
            'callbacks': [is_old_cell]
        }
    }
}
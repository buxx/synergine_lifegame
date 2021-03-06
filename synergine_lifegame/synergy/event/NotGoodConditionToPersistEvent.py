from synergine_lifegame.synergy.event.AliveAroundEvent import AliveAroundEvent
from synergine.core.exceptions import NotConcernedEvent
from synergine_xyz.mechanism.AroundMechanism import AroundMechanism
from synergine_lifegame.cst import ALIVE, COL_ALIVE


class NotGoodConditionToPersistEvent(AliveAroundEvent):
    """
    This event is applied when die condition are here. So when less of 2 or more of 3 alive cell are around
    of observed cell.
    """

    _mechanism = AroundMechanism
    """This event need to know what is around concerned cell. So we use AroundMechanism who give us list of around
    objects ids."""

    _concern = COL_ALIVE
    """This event only concern alive cells."""

    def _prepare(self, object_id, context, parameters={}):
        """
        According to “Conway’s Game of Life”, event match if less of 2 or more of 3 alive cell are around.
        """
        cell_near_count = self._get_alive_cell_around_count(context, parameters)
        if cell_near_count < 2 or cell_near_count > 3:
            return parameters
        #  If event not match, we must raise an NotConcernedEvent.
        raise NotConcernedEvent()

import sys

import pyved_engine as pyv

from src.game_objects.background import ColorBackground
from src.game_objects.label import Label
from src.game_objects.button import Button

import globals


class ScoreState(pyv.BaseGameState):
    def __init__(self, ident):
        super().__init__(ident)
        self.components = [
            ColorBackground(color="#36354A"),
            score_label := Label(480, 150, "0", 50, "white"),
            high_score_label := Label(480, 220, "0", 50, "white"),
            Button(480, 350, " Home ", 50, "white",
                   callback=lambda: pyv.get_ev_manager().post(pyv.EngineEvTypes.StateChange,
                                                              state_ident=globals.GameStates.Home)),
            Button(480, 450, " Replay ", 50, "white",
                   callback=lambda: pyv.get_ev_manager().post(pyv.EngineEvTypes.StateChange,
                                                              state_ident=globals.GameStates.Game)),
            Button(480, 550, " Quit ", 50, "white", callback=lambda: sys.exit(0))
        ]
        self.score_label = score_label
        self.high_score_label = high_score_label

    def enter(self):
        for i in self.components:
            i.turn_on()
        globals.SharedVars.HIGH_SCORE = max(globals.SharedVars.SCORE, globals.SharedVars.HIGH_SCORE)
        self.score_label.update_text("Score: " + str(globals.SharedVars.SCORE))
        globals.SharedVars.SCORE = 0
        self.high_score_label.update_text("High Score: " + str(globals.SharedVars.HIGH_SCORE))

    def release(self):
        for i in self.components:
            i.turn_off()

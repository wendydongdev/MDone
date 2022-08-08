from application import db
from __future__ import annotations
from abc import ABC, abstractmethod

class Task(db.Document):
    taskID = db.IntField(unique=True)
    title = db.StringField(max_length=100)
    description = db.StringField(max_length=255)
    phase = db.IntField()
    deadline = db.DateField()

    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def updatephase(self):
        self._state.handle1()

    def delete(self):
        self._state.handle2()


class State(ABC):

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def updatephase(self) -> None:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass



class TaskTODO(State):
    def updatephase(self) -> None:
        self.context.transition_to(ConcreteStateB())

    def delete(self) -> None:
        pass



class taskOverDue(State):
    def updatephase(self) -> None:
        print("ConcreteStateB handles request1.")

    def delete(self) -> None:
        pass
    #overdue task cannot be deleted


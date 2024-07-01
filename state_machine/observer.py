class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(*args, **kwargs)

class Observer:
    def update(self, *args, **kwargs):
        pass

class StateComponent(Observable):
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify_observers(value)

class StateChangeHandler(Observer):
    def update(self, state):
        print(f"State changed to: {state}")
        self.handle_state_change(state)

    def handle_state_change(self, state):
        if state == "running":
            self.start()
        elif state == "paused":
            self.pause()
        elif state == "stopped":
            self.stop()

    def start(self):
        print("Starting...")

    def pause(self):
        print("Pausing...")

    def stop(self):
        print("Stopping...")

component = StateComponent()
handler = StateChangeHandler()
component.add_observer(handler)

component.state = "running"
component.state = "paused"
component.state = "stopped"

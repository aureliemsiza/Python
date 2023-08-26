

class State:
    def __init__(self):
        pass
    
    def enter(self):
        pass
    
    def exit(self):
        pass
    
    def update(self):
        pass

class IdleState(State):
    def update(self):
        print("Character is idling.")

class ChaseState(State):
    def enter(self):
        print("Character is entering chase mode.")

    def update(self):
        print("Character is chasing the player.")

    def exit(self):
        print("Character is exiting chase mode.")

class AttackState(State):
    def enter(self):
        print("Character is entering attack mode.")

    def update(self):
        print("Character is attacking the player.")

    def exit(self):
        print("Character is exiting attack mode.")

class StateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, state_name, state):
        self.states[state_name] = state

    def set_state(self, state_name):
        if self.current_state:
            self.current_state.exit()
        self.current_state = self.states[state_name]
        self.current_state.enter()

    def update(self):
        if self.current_state:
            self.current_state.update()

# Usage
character_fsm = StateMachine()
character_fsm.add_state("idle", IdleState())
character_fsm.add_state("chase", ChaseState())
character_fsm.add_state("attack", AttackState())

character_fsm.set_state("idle")
character_fsm.update()
character_fsm.set_state("chase")
character_fsm.update()
character_fsm.set_state("attack")
character_fsm.update()

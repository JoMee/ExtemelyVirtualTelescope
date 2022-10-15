import statecontrol
import json


def write_state():
    state_to_write = statecontrol.get_initial_state()

    dump = json.dumps(state_to_write, indent=4)

    with open("state.json", "w") as outfile:
        outfile.write(dump)

    print(dump)

write_state()

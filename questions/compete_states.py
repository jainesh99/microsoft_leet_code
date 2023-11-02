def cellCompete(states, days):
    def compete(left_state, right_state):
        if left_state == right_state:
            return 0
        else:
            return 1

    for i in range(days):
        result_states = []

        for index, state in enumerate(states):
            if index - 1 < 0:
                new_state = compete(0, states[index + 1])
            elif index + 1 >= len(states):
                new_state = compete(states[index - 1], 0)
            else:
                new_state = compete(states[index - 1], states[index + 1])

            result_states.append(new_state)

        states = result_states

    return states


print(cellCompete([1, 0, 0, 0, 0, 1, 0, 0], 1))

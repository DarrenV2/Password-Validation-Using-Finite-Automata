class DFA:
    def __init__(self):
        self.start_state = "q1"
        self.accept_state = "q15"
        self.current_state = self.start_state

        # Transition table aka State dictionary
        self.transitions = {
            "q0":  {"a": "q0", "b": "q0", "A": "q0", "B": "q0", "0": "q0", "1": "q0"},
            "q1":  {"a": "q2", "b": "q2", "A": "q8", "B": "q8", "0": "q0", "1": "q0"},
            "q2":  {"a": "q4", "b": "q4", "A": "q9", "B": "q9", "0": "q5", "1": "q5"},
            "q3":  {"a": "q3", "b": "q3", "A": "q11", "B": "q11", "0": "q7", "1": "q7"},
            "q4":  {"a": "q3", "b": "q3", "A": "q13", "B": "q13", "0": "q6", "1": "q6"},
            "q5":  {"a": "q6", "b": "q6", "A": "q13", "B": "q13", "0": "q6", "1": "q6"},
            "q6":  {"a": "q7", "b": "q7", "A": "q14", "B": "q14", "0": "q7", "1": "q7"},
            "q7":  {"a": "q7", "b": "q7", "A": "q15", "B": "q15", "0": "q7", "1": "q7"},
            "q8":  {"a": "q9", "b": "q9", "A": "q9", "B": "q9", "0": "q12", "1": "q12"},
            "q9":  {"a": "q10", "b": "q10", "A": "q10", "B": "q10", "0": "q13", "1": "q13"},
            "q10": {"a": "q11", "b": "q11", "A": "q11", "B": "q11", "0": "q14", "1": "q14"},
            "q11": {"a": "q11", "b": "q11", "A": "q11", "B": "q11", "0": "q15", "1": "q15"},
            "q12": {"a": "q13", "b": "q13", "A": "q13", "B": "q13", "0": "q13", "1": "q13"},
            "q13": {"a": "q14", "b": "q14", "A": "q14", "B": "q14", "0": "q14", "1": "q14"},
            "q14": {"a": "q15", "b": "q15", "A": "q15", "B": "q15", "0": "q15", "1": "q15"},
            "q15": {"a": "q15", "b": "q15", "A": "q15", "B": "q15", "0": "q15", "1": "q15"},
        }

    def reset(self): # Defined Function used to reset DFA to start state
        self.current_state = self.start_state

    def process_input(self, string): 
        self.reset()
        for char in string:
            if char not in self.transitions[self.current_state]:
                return False
            self.current_state = self.transitions[self.current_state][char]
        return self.current_state == self.accept_state


def main():
    """Main function to run the DFA test cases."""
    print("=== DFA String Recognition Test ===\n")
    
    # Initialize DFA
    dfa = DFA()

    # # Test cases
    # test_cases = [
    #     "aAaaa",   # Valid
    #     "A01bb",   # Valid
    #     "b1aaa",   # Invalid (no uppercase)
    #     "B",       # Invalid (too short)
    #     "B1111",   # Valid
    #     "a111B",   # Valid
    #     "1111B",   # Invalid (doesn't start with a letter)
    # ]

    # # Run tests
    # for s in test_cases:
    #     result = "ACCEPTED" if dfa.process_input(s) else "REJECTED"
    #     print(f"{s} ➤ {result}")


if __name__ == "__main__":
    main()
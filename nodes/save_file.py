##################
# Safe file node #
##################


import os
from datetime import datetime
from agent_state import AgentState

# Define output directory relative to the project root
base_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(base_dir, "outputs")


def save_to_file(state: AgentState) -> AgentState:

    """
    This function saves the final question, answer, and agent trace to a timestamped text file in the outputs directory.
    """

    # Make sure the directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Create timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"agent_result_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)

    # Write question, answer, and trace to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("QUESTION\n")
        f.write("--------\n")
        f.write(state["question"] + "\n\n")

        f.write("ANSWER\n")
        f.write("------\n")
        f.write((state.get("current_answer") or "No confident answer.") + "\n\n")

        f.write("\nAGENT TRACE\n")
        f.write("-----------\n")
        f.write(" → ".join(state.get("trace", [])))

    # Return updated state
    return {
        **state,
        "done": True,
        "trace": state["trace"] + ["save_file"],
    }
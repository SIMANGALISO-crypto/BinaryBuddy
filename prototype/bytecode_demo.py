import dis
from collections import Counter

def sample_function(x, y):
    return (x + y) * 2

def explain_bytecode(func):
    print(f"Disassembly for: {func.__name__}\n")
    instructions = list(dis.get_instructions(func))
    for instr in instructions:
        explanation = f"{instr.opname} → {instr.argrepr}"
        print(f"{instr.offset:2}: {instr.opname:20} | {explanation}")

    # New feature: opcode count summary
    opcode_count = Counter(instr.opname for instr in instructions)
    print("\nOpcode Summary:")
    for opcode, count in opcode_count.items():
        print(f"{opcode}: {count}")

if __name__ == "__main__":
    explain_bytecode(sample_function)

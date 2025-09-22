import dis
import marshal
import sys
import types
from collections import Counter

def explain_pyc(path):
    with open(path, "rb") as f:
        f.read(16)  # skip .pyc header
        code_obj = marshal.load(f)

    if isinstance(code_obj, types.CodeType):
        print(f"Disassembly for {path}")
        instructions = list(dis.get_instructions(code_obj))
        for instr in instructions:
            print(f"{instr.offset:2}: {instr.opname:20} {instr.argrepr}")

        # Opcode count summary
        opcode_count = Counter(instr.opname for instr in instructions)
        print("\nOpcode Summary:")
        for opcode, count in opcode_count.items():
            print(f"{opcode}: {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pyc_reader.py <file.pyc>")
    else:
        explain_pyc(sys.argv[1])

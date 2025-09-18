import dis
import marshal
import sys
import types

def explain_pyc(path):
    with open(path, "rb") as f:
        f.read(16)  # skip header
        code_obj = marshal.load(f)
    if isinstance(code_obj, types.CodeType):
        print(f"Disassembly for {path}")
        for instr in dis.get_instructions(code_obj):
            print(f"{instr.offset:2}: {instr.opname:20} {instr.argrepr}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pyc_reader.py <file.pyc>")
    else:
        explain_pyc(sys.argv[1])

# Solution Overview: Advent of Code - Day 17: Chronospatial Computer

### My input:
The machine code equivalant is:
```angular2html
010 100 | 001 001 | 111 101 | 001 101 | 100 000 | 101 101 | 000 011 | 011 000
```
Derivable as such:
- Opcode 2 (bst), Operand 4: 010 100 (bst instruction, 4)
- Opcode 1 (bxl), Operand 1: 001 001 (bxl instruction, 1)
- Opcode 7 (cdv), Operand 5: 111 101 (cdv instruction, 5)
- Opcode 1 (bxl), Operand 5: 001 101 (bxl instruction, 5)
- Opcode 4 (bxc), Operand 0: 100 000 (bxc instruction, 0)
- Opcode 5 (out), Operand 5: 101 101 (out instruction, 5)
- Opcode 0 (adv), Operand 3: 000 011 (adv instruction, 3)
- Opcode 3 (jnz), Operand 0: 011 000 (jnz instruction, 0)


This solution simulates a 3-bit virtual machine to solve the Advent of Code 2024 puzzle. The problem involves determining the output of a program and finding the smallest seed value for register A that makes the program output a copy of itself (a quine).

## Key Components

### 1. **VirtualMachine Class**
- Models a 3-bit computer with registers A, B, and C.
- Executes instructions based on opcodes and operands, which are parsed from the program.
- Instructions include shifts, XOR operations, modulo operations, and jumps.
- The `run()` method executes the program, collecting output produced by `out` instructions.

### 2. **BitPattern Class**
- Represents a bit pattern with a mask and pattern.
- Allows merging bit patterns, shifting, and custom string representation where `1`/`0` are constrained bits and `.` represents unconstrained bits.
- `merge()` attempts to merge two patterns by checking if they are compatible.
- Supports shifting using `<<` for left shifts.

### 3. **Operations in VirtualMachine**
- The virtual machine supports 8 instructions:
    - **Shift operations** (`shift_a`, `shift_b`, `shift_c`) shift the contents of registers A, B, and C.
    - **XOR operations** (`xor_b_with_value`, `xor_b_with_c`) manipulate register B with values or register C.
    - **Modulo operations** (`store_b_remainder`) store the remainder of an operand modulo 8 in register B.
    - **Jump operation** (`jump_if_a_nonzero`) alters the program counter based on the value of register A.
    - **Output operation** (`output_value`) outputs a value derived from a combo operand.

### 4. **Part 1: Running the Program**
- Given an initial state (values for registers A, B, C, and a program), the program is executed.
- The `run()` method processes the program and prints the outputs generated by the `out` instruction.
- The program halts when all instructions are executed.

### 5. **Part 2: Finding the Minimum Quine Seed**
- The goal is to find the smallest seed for register A that causes the program to output an exact copy of itself.
- The `generate_base_patterns()` function constructs possible bit patterns for each instruction in the program.
- The `find_minimum_quine_seed()` function determines the smallest seed for register A that causes the program to output a quine.

### 6. **Key Methods**
- **`run()`**: Executes the program and collects output.
- **`generate_base_patterns()`**: Generates bit patterns based on the program's instructions.
- **`find_minimum_quine_seed()`**: Finds the smallest initial value for register A that outputs a copy of the program.

## Output
- **Part 1**: Prints the output produced by the `out` instructions in the program.
- **Part 2**: Finds and prints the smallest seed for register A that makes the program output a copy of itself.

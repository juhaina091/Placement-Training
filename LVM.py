'''You are designing a virtual machine for a new programming language called Lombok. The Lombok Virtual Machine (LVM) runs an assembler-like machine code. It operates on a stack and a single register.

In detail, the instructions work as follows:

PUSH x: This instruction pushes a given integer onto the stack. If the stack for example looks like this: [2, 3] and the machine executes the instruction PUSH -11,the stack looks like this afterwards: [-11, 2, 3]

STORE: This instruction takes the topmost integer from the stack and stores it in the register. If the stack for example looks like this: [3, 9, 4], the register contains any integer, and the machine executes the instruction STORE, the stack looks like this afterwards: [9, 4] and the register contains the integer 3.

LOAD: This instruction copies the content of the register and pushes it onto the stack. If the register for example contains the integer 6, the stack looks like this: [8, 7], and the machine executes the instruction LOAD, the stack looks like this afterwards: [6, 8, 7], and the register still contains the integer 6.

PLUS: This instruction takes the two topmost integers from the stack, adds them, and pushes the resulting integer back onto the stack. If the stack for example looks like this: [2, 3, 4], and the machine executes the instruction PLUS, the stack looks like this afterwards: [5, 4]

TIMES: This instruction takes the two topmost integers from the stack, multiplies them, and pushes the resulting integer back onto the stack. If the stack for example looks like this: [2, 3, 4], and the machine executes the instruction TIMES, the stack looks like this afterwards: [6, 4]

IFZERO n: This instruction removes the topmost integer from the stack, and checks if it is equal to 0. If that is the case, it jumps to the nth instruction (start counting at 0). If not, the machine continues as usual with the next instruction. See example below.

DONE: Finally, the DONE instruction prints out the integer on top of the stack, and terminates the program regardless of the following instructions.

Computation starts with the first instruction. Initially, the stack is empty and the register contains the number 0.

Input Format

14
PUSH 5
STORE
LOAD
LOAD
PUSH -1
PLUS
STORE
LOAD
IFZERO 13
LOAD
TIMES
PUSH 0
IFZERO 3
DONE

Constraints

NA

Output Format

120

Sample Input 0

14
PUSH 5
STORE
LOAD
LOAD
PUSH -1
PLUS
STORE
LOAD
IFZERO 13
LOAD
TIMES
PUSH 0
IFZERO 3
DONE
Sample Output 0

120
Contest ends in 41 minutes
Submissions: 18
Max Score: 50
Difficulty: Medium
'''n=int(input())
instr=[]
for i in range(n):
    k=input()
    instr.append(k)
stack=[]
reg=[]
i=0
while i<n:
    k=instr[i].split()
    #print(instr[i])
    if k[0]=='PUSH':
        stack.append(int(k[1]))
        #print(stack)
    elif k[0]=='STORE':
        m=stack.pop()
        reg.append(m)
        #print(stack)
        #print(reg)
    elif k[0]=='LOAD':
        m=reg[-1]
        stack.append(m)
        #print(stack)
        #print(reg)
    elif k[0]=='PLUS':
        m=stack.pop()+stack.pop()
        stack.append(m)
        #print(stack)
    elif k[0]=='TIMES':
        m=stack.pop()*stack.pop()
        stack.append(m)
        #print(stack)
    elif k[0]=='IFZERO':
        if stack.pop()==0:
            i=int(k[1])
            continue
    elif k[0]=='DONE':
        print(stack[-1])
        break
    i+=1
        
            

@ p1102.s
          .text
          .global _start

g:        mov r1, #2
          add r0, r0, r1
          svc 0
          

f:        mov r1, #1
          add r0, r0, r1
          mov pc, lr

_start:   mov r0, #1       @ move 1 into r0
          bl f             @ call f
          bl g             @ call g
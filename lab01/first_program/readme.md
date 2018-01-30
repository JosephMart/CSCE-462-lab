## Compile and Run

Assemble the code into an object file:
`as -o helloworld.o helloworld.s`

Compile the object file by a C compiler, it will be transformed into a executable:
`gcc -o helloworld helloworld.o`

Run your first prog
`./helloworld`
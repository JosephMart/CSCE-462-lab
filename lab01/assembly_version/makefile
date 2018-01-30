all: blink.o
	gcc -o blink blink.o

blink.o: blink.s
	as -o blink.o blink.s

clean:
	rm blink.o blink

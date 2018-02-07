#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <stdint.h>
#include <stddef.h>

#define PERI_BASE 0x3F000000
#define GPIO_BASE (PERI_BASE + 0x200000)
#define FUN_SEL_OFFSET 0x0
#define SET_OFFSET 0x1C
#define CLEAR_OFFSET 0x28
#define OUTPUT 1

void setPinMode(uint32_t* gpioBase, int pin, int mode);
void setPinOn(uint32_t* gpioBase, int pin);
void setPinOff(uint32_t* gpioBase, int pin);

int main(void){
	int pin = 18; //bcm numbering (RPi standard)
	int fd;
	void *gpioBase;
	
	if(-1 == (fd = open("/dev/mem", O_RDWR))){
		fprintf(stderr, "open() failed.\n");
		return 254;
	}

	if(MAP_FAILED == (gpioBase = mmap(NULL,4096, PROT_READ|PROT_WRITE,
		MAP_SHARED, fd, GPIO_BASE))){
		fprintf(stderr, "mmap() failed\n");
		return 254;
	}

	setPinMode(gpioBase, pin, OUTPUT);

	int i;
	for(i=0; i<1; i++){
		setPinOn(gpioBase, pin);
		sleep(1);
		setPinOff(gpioBase, pin);
		sleep(1);
	}
	close(fd);
}

void setPinMode(uint32_t* gpioBase, int pin, int mode) {
	uint32_t* gpioFunSel = (uint32_t*)((char*)gpioBase+FUN_SEL_OFFSET);
	int funSelIndex = pin/10;
	int funSelShift = 3*(pin%10);
	gpioFunSel[funSelIndex] = (gpioFunSel[funSelIndex] | (mode<<funSelShift));
}

void setPinOn(uint32_t* gpioBase, int pin) {
	uint32_t *gpioSet = (uint32_t*)((char*)gpioBase + SET_OFFSET);
	int gpioSCIndex = pin/32;
	int gpioSCShift = pin%32;
	gpioSet[gpioSCIndex] = (1<<gpioSCShift);
}

void setPinOff(uint32_t* gpioBase, int pin) {
	uint32_t *gpioClear = (uint32_t*)((char*)gpioBase + CLEAR_OFFSET);
	int gpioSCIndex = pin/32;
	int gpioSCShift = pin%32;
	gpioClear[gpioSCIndex] = (1<<gpioSCShift);
}


SRC = pywindow
FLAGS = -shared -fPIC

$(SRC)/so/main.so: $(SRC)/c/main.c
	gcc $(FLAGS) -o pywindow/so/main.so pywindow/c/main.c
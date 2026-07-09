SRC = pywindow
FLAGS = -shared -fPIC -I/opt/homebrew/include -L/opt/homebrew/lib -lraylib -framework OpenGL -framework Cocoa -framework IOKit -framework CoreVideo

$(SRC)/so/main.so: $(SRC)/c/main.c
	rm -rf $(SRC)/__pycache__
	gcc $(FLAGS) -o $(SRC)/so/main.so $(SRC)/c/main.c
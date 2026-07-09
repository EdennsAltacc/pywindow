#include <raylib.h>

int test(const char *title, int x, int y, void (*main_loop)(void)) {
    InitWindow(x, y, title);
    SetTargetFPS(60);
    
    while (!WindowShouldClose()) {
        main_loop();
    }
    
    CloseWindow();
    return 0;
}

void begin_drawing(void) {
    BeginDrawing();
}

void end_drawing(void) {
    EndDrawing();
}

void clear_background(Color background) {
    ClearBackground(background);
}
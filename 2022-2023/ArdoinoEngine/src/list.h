#include <Arduino.h>
class List{
public:
    
    int length;
    int data[16];
    void append(int item) {
        if (length < 16) data[length++] = item;

    }
    void remove(int index) {
        if (index >= length) return;
        memmove(&data[index], &data[index+1], length - index - 1);
        length--;
    }
};

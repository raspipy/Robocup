#include <Arduino.h>
#include <LinkedList.h>

LinkedList<int> left_motor = LinkedList<int>();
LinkedList<int> right_motor = LinkedList<int>();


void IncrementRound(LinkedList<int> List){
    List[-1]++;

}
void NewStep(LinkedList<int> List){
    List.add(0);
}




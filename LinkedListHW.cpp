#include <iostream>
#include <vector>
using namespace std;

// Node structure
struct Node {
    int data;
    Node* next;
};

// Helper function to print your list
void print_list(Node* head) {
    Node* current = head;
    while (current != nullptr) {
        cout << current->data << " -> ";
        current = current->next;
    }
    cout << "nullptr" << endl;
}

// Helper function to create a list from a vector of values
Node* create_list(vector<int> values) {
    if (values.empty()) {
        return nullptr;
    }
    
    Node* head = new Node{values[0], nullptr};
    Node* current = head;
    
    for (int i = 1; i < values.size(); i++) {
        current->next = new Node{values[i], nullptr};
        current = current->next;
    }
    return head;
}


// Reverse the linked list
Node* reverse_list(Node* head) {
    // Your code here
    return nullptr;
}


int main() {
    // Test the functions
    Node* head = create_list({10, 20, 30, 40});
    
    cout << "Original list: ";
    print_list(head);
    
    head = reverse_list(head);
    
    cout << "Reversed list: ";
    print_list(head);
    
    // Clean up memory (optional but good practice)
    while (head != nullptr) {
        Node* temp = head;
        head = head->next;
        delete temp;
    }
    
    return 0;
}
#include <iostream>
#include <string>
using namespace std;

// The encryption function
string encrypt(const string& message, const string& key) {
    // Set variables
    string encrypted_msg;
    int key_len = key.length();
    for (int i = 0; i < message.length(); i++) { // For every character in the message:
        char character = toupper(message[i]);
        char shift = toupper(key[i % key_len]);  // To solve the problem with the difference in length between the message and the key
        if (isalpha(character)) { // Encrypt just the alphabetic
            encrypted_msg += char('A'+(character + shift) % 26);
        } else {
            encrypted_msg += character; // Do nothing with special codes
        }
    }
    return encrypted_msg;
}
// The decryption function
string decrypt(const string& message, const string& key) {
    // Set variables
    string decrypted_msg;
    int key_len = key.length();
    for (int i = 0; i < message.length(); i++) { // For every character in the message:
        char character = toupper(message[i]);
        char shift = toupper(key[i % key_len]);  // To solve the problem with the difference in length between the message and the key
        if (isalpha(character)) { // decrypt just the alphabetic
            decrypted_msg += char('A'+(character-shift+26) % 26); 
        } else {
            decrypted_msg += character; // Do nothing with special codes
        }
    }
    return decrypted_msg;
}
// The main function
int main()
{
    cout << "\n\n                -= Welcome to Vignere cipher program =-\nA) Encrypt message        B) Decrypt message        C) Exit the program\n";
    string choice;
    cout << "Please enter your choice (A/B/C) : ";
    getline(cin, choice);
    if (choice == "A" || choice == "a") {
        string message, key;
        cout << "Enter the message: ";
        getline(cin, message);
        cout << "Enter the key: ";
        getline(cin, key);
        string encrypted_msg = encrypt(message, key);
        cout << "The encrypted message is: " << encrypted_msg << endl;
        main();
    }
    else if (choice == "B" || choice == "b") {
        string message, key;
        cout << "Enter the message: ";
        getline(cin, message);
        cout << "Enter the key: ";
        getline(cin, key);
        string encrypted_msg = decrypt(message, key);
        cout << "The decrypted of the message is: " << encrypted_msg << endl;
        main();
        }
    else if (choice == "C" || choice == "c") {
        cout << "Thank you for using the program. Goodbye\n" << endl;
    }
    else {
        cout << "Invalid choice. Please try again." << endl;
        main();
    }
    return 0;
}

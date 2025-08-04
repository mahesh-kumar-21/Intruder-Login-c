#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char username[100];
    char password[100];

    printf("🔐 Welcome to Secure Login\n");
    printf("👤 Username: ");
    fgets(username, sizeof(username), stdin);
    strtok(username, "\n");

    printf("🔑 Password: ");
    fgets(password, sizeof(password), stdin);
    strtok(password, "\n");

    const char *correct_username = "mahesh";
    const char *correct_password = "1234";

    if (strcmp(username, correct_username) == 0 && strcmp(password, correct_password) == 0) {
        printf("✅ Login successful!\n");
    } else {
        printf("❌ Incorrect password!\n");

        // 🔧 Use full path to Python and the script
        const char *command = "\"C:\\Users\\palav\\AppData\\Local\\Programs\\Python\\Python312\\python.exe\" capture_image.py";
        int result = system(command);

        if (result != 0) {
            printf("❌ Failed to run capture script (code %d)\n", result);
        }
    }

    return 0;
}

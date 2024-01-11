from django.http import JsonResponse

class PasswordCracker:
    def __init__(self, target_password):
        self.target_password = target_password
        self.common_passwords = [
            "password", "password123", "letmein", "qwerty",
            "123456", "abc123", "admin", "welcome", "monkey", "sunshine"
        ]
        self.password_variations = [
            "", "123", "1234", "12345", "123456", "!", "@", "#", "$", "%",
            "^", "&", "*", "(", ")", "-", "_", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "<", ">"
        ]
    # Checks if the password and combinations are the same
    def crack_password(self):
        for password in self.common_passwords:
            for variation in self.password_variations:
                if self.attempt_password(password + variation):
                    return True
        return False

    def attempt_password(self, attempt):
        return attempt == self.target_password

# Show the results
def test_password(request, password):
    cracker = PasswordCracker(password)
    welcome = "ZEPO Practical Case 3 -> Dictionary Attack"
    if cracker.crack_password():
        return JsonResponse({"----": welcome, "success": True, "message": "Password cracked!"})
    else:
        return JsonResponse({"----": welcome,"success": False, "message": "Password not cracked."})

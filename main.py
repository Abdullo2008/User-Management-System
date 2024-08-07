# Creating Model
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f"User: username={self.username}, email={self.email}, password={self.password}"


# User CRUD(Create, Read, Update, Delete)
class UserManager:
    def __init__(self):
        self.users = []

    def create_user(self, username, password, email):
        if any(user.username == username for user in self.users):
            print("Username already exists.")
            return None
        user = User(username, password, email)
        self.users.append(user)
        print(f"User {username} created successfully.")
        return user

    def delete_user(self, username):
        self.users = [user for user in self.users if user.username != username]
        print(f"User {username} deleted successfully.")

    def update_user(self, username, new_username=None, new_password=None, new_email=None):
        for user in self.users:
            if user.username == username:
                if new_username:
                    if new_username in self.users:
                        print("Username already exists.")
                        return None
                    else:
                        user.username = new_username
                if new_password:
                    user.password = new_password
                if new_email:
                    user.email = new_email
                print(f"User {username} updated successfully.")
                return user
        print("User not found.")
        return None

    def list_users(self):
        count = 0
        if self.users:
            for user in self.users:
                count += 1
                print(f'{count}-{user}')
        else:
            print("No users yet")


# Project displayer (main function)
def main():
    user_manager = UserManager()
    while True:
        print("\nOptions:")
        print("1. Create user")
        print("2. Delete user")
        print("3. Update user")
        print("4. List users")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            if username:
                pass
            else:
                print("You entered nothing!!")
                continue
            password = input("Enter password: ")
            if password:
                if len(password) < 4:
                    print('!!WARNING!!')
                    print('-----------')
                    print('Your password is too short')
                    confirm_pass = input('Are you sure(y/N):').lower()
                    if confirm_pass == 'y':
                        pass
                    else:
                        continue
            else:
                print('You entered nothing')
                continue
            email = input("Enter email: ")
            domains = ['.com', '.org', '.edu', '.net', '.int', '.gov']
            if email[-4:] in domains:
                user_manager.create_user(username, password, email)
            else:
                print('Enter valid email!!')
        elif choice == '2':
            username = input("Enter username to delete: ")
            user_manager.delete_user(username)
        elif choice == '3':
            username = input("Enter username to update: ")
            new_username = input('Enter new username to update (leave blank to keep current): ')
            new_password = input("Enter new password (leave blank to keep current): ")
            if new_password:
                if len(new_password) < 4:
                    print('!!WARNING!!')
                    print('-----------')
                    print('Your password is too short')
                    confirm_pass = input('Are you sure(y/N):').lower()
                    if confirm_pass == 'y':
                        pass
                    else:
                        continue
            new_email = input("Enter new email (leave blank to keep current): ")
            domains = ['.com', '.org', '.edu', '.net', '.int', '.gov']
            if new_email:
                if new_email[-4:] in domains:
                    user_manager.update_user(username, new_username, new_password, new_email)
                else:
                    print('Enter valid email!!')
        elif choice == '4':
            user_manager.list_users()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


# Running project
if __name__ == "__main__":
    main()

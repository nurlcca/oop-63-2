def log_execution(func):
    def wrapper(*args):
        print(f"Функция {func.__name__} вызена с аргументами {args}")
        
        result = func(*args)
        
        print(f"Результат: {result}")
        print("Функция завершена")
        
        return result
    return wrapper


@log_execution
def add(a, b):
    return a + b


print("=== Проверка log_execution ===")
add(5, 3)



def require_admin(func):
    def wrapper(user):
        if user.role != "admin":
            print("Доступ запрещён")
            return
        return func(user)
    return wrapper


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


@require_admin
def delete_database(user):
    print("База данных удалена")


print("\n=== Проверка require_admin ===")

admin_user = User("Ardager", "admin")
normal_user = User("Azamat", "user")

print("\nАдмин пытается удалить:")
delete_database(admin_user)

print("\nОбычный пользователь пытается удалить:")
delete_database(normal_user)
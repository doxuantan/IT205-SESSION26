# Tính đóng gói ECAPSULATION
# Gom dữ liệu thuộc tính và phương thức vào trong class đồng thời che dấu đi thông tin quan trọng bên trong

# Tính Kế thừa Inheritance
# Cho phép một lớp con tái sử dụng những lớp cũ mà lớp cha đã có tránh viết code lại từ đầu
# class Animal():
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type

# # lớp con kế thừa animal
# class Dog(Animal):
#     def __init__(self, name, type, sound):
#         super().__init__(name, type)
#         # từ khóa supper lấy lại những thuộc tính từ lớp cha
#         self.sound = sound

    
#     def breed(self):
#         print("Đây là một loại động vật")

# class Dog(Animal):
#     def __init__(self, name, type, sound):
#         super().__init__(name, type)
#         # từ khóa supper lấy lại những thuộc tính từ lớp cha
#         self.sound = sound
# # ghi đè methods overwrite
#     def breed(self):
#         print("Đây là một loại động vật có vú")
# dog1 = Dog("Corgi", "Chân ngắn", "GÂU GÂU")
# dog1.breed()
# print(f'dog1: {dog1.name} {dog1.type} {dog1.sound}')




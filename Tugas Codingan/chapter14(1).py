#Tugas Kelompok Chapter 14 Ahmad Gary Shahroom Putra,Adythia Pradiptha Koesnaedi,Kevin Dhiyo Faziliki,Muhammad Hisyam Fata,Muhammad Nabil Ihsan,Romario Galiano
def check_and_divide(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return "Input harus berupa angka"
    if b == 0:
        return "Pembagian dengan nol tidak boleh"
    return a / b
input_a = input("Masukkan bilangan integer a: ")
input_b = input("Masukkan bilangan integer b: ")
try:
    converted_a = int(input_a)
    converted_b = int(input_b)
    print(check_and_divide(converted_a, converted_b))
except ValueError:
    print("Input harus berupa angka")
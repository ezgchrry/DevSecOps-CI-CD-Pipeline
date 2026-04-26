#bu dosya "ürünümüzü" temsil etmektedir.
#kodumuz kullanıcının girdiği şifrenin uzunluğunu kontrol ediyor. eğer 8 karakterden büyükse güçlü, küçükse zayıf sonucunu dönüyor.
#fonksiyonel gereksinimler burada tanımlandı.
def check_password_strength(password):
    if len(password) >= 8:
        return "Güçlü"
    return "Zayıf"

if __name__ == "__main__":
    print(check_password_strength("12345678"))

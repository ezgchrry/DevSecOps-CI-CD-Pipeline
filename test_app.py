# burada yazılımın kalitesini ölçüyoruz
# pytest kütüphanesini kullanarak app.py içindeki fonksiyonu farklı senaryolarla test ediyoruz
# yazılım kalitesini manuel değil, otomatik olarak ölçmemize olanak tanıyor
from app import check_password_strength

def test_check_password_strength():
    assert check_password_strength("abcdefgh") == "Güçlü"
    assert check_password_strength("123") == "Zayıf"

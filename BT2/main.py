from abc import ABC, abstractmethod


# Lớp cha trừu tượng
class Hero(ABC):

    @abstractmethod
    def use_ultimate(self):
        pass


# Lớp Pháp Sư
class Mage(Hero):

    def use_ultimate(self):
        print("🔥 Pháp Sư tung chiêu: MƯA SAO BĂNG!")


# Lớp Sát Thủ
class Assassin(Hero):

    def use_ultimate(self):
        print("🗡️ Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")


# --- LOADING TRẬN ĐẤU ---
print("--- LOADING TRẬN ĐẤU ---")

team_heroes = [Mage(), Assassin()]

print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")

# Đa hình (Polymorphism)
for hero in team_heroes:
    hero.use_ultimate()
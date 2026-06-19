from abc import ABC, abstractmethod


class Champion(ABC):
    """
    Lớp trừu tượng đại diện cho một quân cờ trong game.
    """

    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name

        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        """
        Tính sát thương kỹ năng.
        """
        pass

    def get_combat_power(self):
        """
        Tính chiến lực tổng hợp.
        """
        return self.base_hp + self.calculate_skill_damage()

    def __add__(self, other):
        """
        Hỗ trợ cộng chiến lực.
        """

        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()

        if isinstance(other, (int, float)):
            return self.get_combat_power() + other

        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __gt__(self, other):
        """
        So sánh chiến lực.
        """
        return self.get_combat_power() > other.get_combat_power()


class Warrior(Champion):
    """
    Hệ Chiến Binh.
    """

    def __init__(
            self,
            champion_id,
            name,
            base_hp,
            base_atk,
            shield_bonus):

        super().__init__(
            champion_id,
            name,
            base_hp,
            base_atk)

        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        return self.base_atk * 2 + self.shield_bonus


class Mage(Champion):
    """
    Hệ Pháp Sư.
    """

    def __init__(
            self,
            champion_id,
            name,
            base_hp,
            base_atk,
            ability_power):

        super().__init__(
            champion_id,
            name,
            base_hp,
            base_atk)

        self.ability_power = ability_power

    def calculate_skill_damage(self):
        return self.base_atk * self.ability_power


champion_pool = [
    Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
    Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
    Mage("MAG01", "Rikkei Wizard", 800, 500, 2.0)
]


def find_champion(champion_id):
    """
    Tìm quân cờ theo mã.
    """
    for champion in champion_pool:
        if champion.champion_id == champion_id:
            return champion
    return None


def display_champions():
    """
    Hiển thị danh sách quân cờ.
    """

    print("\n--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")

    print(
        f"{'Mã':<8}|{'Tên tướng':<20}|{'Hệ':<10}|"
        f"{'HP':<8}|{'ATK':<8}|{'Chỉ số riêng':<20}|{'Chiến lực'}"
    )

    print("-" * 100)

    for champion in champion_pool:

        if isinstance(champion, Warrior):
            role = "Warrior"
            extra = f"Armor: {champion.shield_bonus}"

        else:
            role = "Mage"
            extra = f"Mana: {champion.ability_power}"

        print(
            f"{champion.champion_id:<8}|"
            f"{champion.name:<20}|"
            f"{role:<10}|"
            f"{champion.base_hp:<8}|"
            f"{champion.base_atk:<8}|"
            f"{extra:<20}|"
            f"{champion.get_combat_power():.0f}"
        )

    print("-" * 100)


def add_champion():
    """
    Thêm quân cờ mới.
    """

    print("\n1. Warrior")
    print("2. Mage")

    choice = input("Chọn hệ: ")

    champion_id = input("Nhập mã tướng: ").strip()

    if find_champion(champion_id):
        print("Mã tướng đã tồn tại!")
        return

    name = input("Nhập tên tướng: ")

    try:
        hp = int(input("Nhập HP: "))
        atk = int(input("Nhập ATK: "))

        if choice == "1":

            armor = int(input("Nhập Armor: "))

            champion = Warrior(
                champion_id,
                name,
                hp,
                atk,
                armor)

        elif choice == "2":

            ap = float(input("Nhập Ability Power: "))

            champion = Mage(
                champion_id,
                name,
                hp,
                atk,
                ap)

        else:
            print("Lựa chọn không hợp lệ!")
            return

        champion_pool.append(champion)

        print("\nThêm tướng thành công!")
        print(
            f"Mã: {champion.champion_id} | "
            f"Tên: {champion.name} | "
            f"Chiến lực: {champion.get_combat_power():.0f}"
        )

    except ValueError:
        print("Dữ liệu nhập không hợp lệ!")


def compare_champions():
    """
    So sánh 2 quân cờ.
    """

    print("\n--- SO SÁNH SỨC MẠNH 2 QUÂN CỜ ---")

    id1 = input("Nhập mã tướng thứ nhất: ").strip()
    id2 = input("Nhập mã tướng thứ hai: ").strip()

    c1 = find_champion(id1)
    c2 = find_champion(id2)

    if not c1:
        print(f"Mã tướng {id1} không hợp lệ!")
        return

    if not c2:
        print(f"Mã tướng {id2} không hợp lệ!")
        return

    if c1 > c2:
        print(
            f"Kết quả: {c1.champion_id} - "
            f"{c1.name} mạnh hơn "
            f"{c2.champion_id} - {c2.name}"
        )
    else:
        print(
            f"Kết quả: {c2.champion_id} - "
            f"{c2.name} mạnh hơn "
            f"{c1.champion_id} - {c1.name}"
        )


def calculate_team_power():
    """
    Tính tổng chiến lực đội hình.
    """

    print("\n--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH ---")

    ids = input(
        "Nhập danh sách mã tướng, cách nhau bằng dấu phẩy: "
    )

    ids = [x.strip() for x in ids.split(",")]

    team = []

    for champion_id in ids:

        champion = find_champion(champion_id)

        if champion:
            team.append(champion)
        else:
            print(
                f"Mã tướng {champion_id} "
                f"không hợp lệ, bỏ qua!"
            )

    if not team:
        print("Không có tướng hợp lệ.")
        return

    print("\nDanh sách đội hình:")

    for index, champion in enumerate(team, start=1):
        print(
            f"{index}. "
            f"{champion.champion_id} - "
            f"{champion.name} | "
            f"Chiến lực: "
            f"{champion.get_combat_power():.0f}"
        )

    total_power = sum(team)

    print(f"\nTổng chiến lực đội hình: {total_power:.0f}")


def main():
    """
    Menu chính.
    """

    while True:

        print("\n========== RIKKEI RPG ==========")
        print("1. Hiển thị bể tướng")
        print("2. Thêm quân cờ")
        print("3. So sánh quân cờ")
        print("4. Tính tổng chiến lực đội hình")
        print("5. Thoát")

        choice = input("Chọn chức năng (1-5): ")

        match choice:

            case "1":
                display_champions()

            case "2":
                add_champion()

            case "3":
                compare_champions()

            case "4":
                calculate_team_power()

            case "5":
                print(
                    "Cảm ơn bạn đã sử dụng "
                    "Rikkei RPG - Auto-Battler Manager!"
                )
                break

            case _:
                print("Lựa chọn không hợp lệ!")


main()
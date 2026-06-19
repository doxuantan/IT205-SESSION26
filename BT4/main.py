from abc import ABC, abstractmethod


inventory = []


class Equipment(ABC):
    """
    Lớp trừu tượng cho mọi trang bị.
    """

    @abstractmethod
    def calculate_total_damage(self):
        pass


class Weapon(Equipment):
    """
    Vũ khí vật lý.
    """

    def __init__(self, name, base_damage, upgrade_level=0):
        self.name = name
        self.base_damage = base_damage
        self.upgrade_level = upgrade_level

    def calculate_total_damage(self):
        return self.base_damage + self.upgrade_level * 10

    def __gt__(self, other):

        if not isinstance(other, Equipment):
            raise TypeError(
                "Chỉ có thể so sánh giữa các trang bị!"
            )

        return (
            self.calculate_total_damage()
            >
            other.calculate_total_damage()
        )

    def __add__(self, other):

        if not isinstance(other, Equipment):
            raise TypeError(
                "Chỉ có thể dung hợp giữa các trang bị!"
            )

        new_name = (
            f"Fusion({self.name} + {other.name})"
        )

        new_damage = (
            self.base_damage
            + other.base_damage
        )

        new_level = (
            self.upgrade_level
            + other.upgrade_level
        )

        return Weapon(
            new_name,
            new_damage,
            new_level
        )


class MagicMixin:
    """
    Thuộc tính phép thuật.
    """

    def __init__(self, magic_power):
        self.magic_power = magic_power

    def cast_glow(self):
        print("✨ Vũ khí phát sáng!")


class MagicSword(Weapon, MagicMixin):
    """
    Kiếm ma thuật.
    """

    def __init__(
            self,
            name,
            base_damage,
            upgrade_level,
            magic_power):

        Weapon.__init__(
            self,
            name,
            base_damage,
            upgrade_level
        )

        MagicMixin.__init__(
            self,
            magic_power
        )

    def calculate_total_damage(self):

        return (
            self.base_damage
            + self.upgrade_level * 10
            + self.magic_power
        )


def display_inventory():

    print("\n--- KHO VŨ KHÍ ---")

    if not inventory:
        print("Kho vũ khí hiện đang trống.")
        return

    print(
        f"{'STT':<5}"
        f"{'Tên':<25}"
        f"{'Loại':<15}"
        f"{'Cấp':<10}"
        f"{'Sát thương'}"
    )

    for i, item in enumerate(
            inventory,
            start=1):

        print(
            f"{i:<5}"
            f"{item.name:<25}"
            f"{type(item).__name__:<15}"
            f"{item.upgrade_level:<10}"
            f"{item.calculate_total_damage()}"
        )


def input_positive_int(message):

    while True:

        try:
            value = int(input(message))

            if value <= 0:
                print(
                    "Giá trị phải lớn hơn 0!"
                )
                continue

            return value

        except ValueError:
            print("Vui lòng nhập số!")


def create_weapon():

    print("\n--- RÈN VŨ KHÍ VẬT LÝ ---")

    name = input(
        "Nhập tên vũ khí: "
    ).title()

    damage = input_positive_int(
        "Nhập sát thương gốc: "
    )

    level = input_positive_int(
        "Nhập cấp cường hóa: "
    )

    weapon = Weapon(
        name,
        damage,
        level
    )

    inventory.append(weapon)

    print("\n>> Rèn thành công!")
    print(
        f"Tên: {weapon.name}"
    )
    print(
        f"Sát thương: "
        f"{weapon.calculate_total_damage()}"
    )


def create_magic_sword():

    print("\n--- RÈN KIẾM MA THUẬT ---")

    name = input(
        "Nhập tên kiếm: "
    ).title()

    damage = input_positive_int(
        "Nhập sát thương gốc: "
    )

    level = input_positive_int(
        "Nhập cấp cường hóa: "
    )

    magic = input_positive_int(
        "Nhập sức mạnh phép thuật: "
    )

    sword = MagicSword(
        name,
        damage,
        level,
        magic
    )

    inventory.append(sword)

    print("\n>> Rèn kiếm thành công!")
    print(
        f"Sát thương tổng: "
        f"{sword.calculate_total_damage()}"
    )


def compare_weapon():

    print("\n--- THẨM ĐỊNH VŨ KHÍ ---")

    if len(inventory) < 2:
        print(
            "Cần ít nhất 2 vũ khí!"
        )
        return

    first = inventory[0]
    second = inventory[1]

    print(
        f"Vũ khí 1: "
        f"{first.name}"
    )

    print(
        f"Vũ khí 2: "
        f"{second.name}"
    )

    damage1 = first.calculate_total_damage()
    damage2 = second.calculate_total_damage()

    if damage1 == damage2:
        print(
            "Hai vũ khí ngang sức."
        )

    elif first > second:
        print(
            f"{first.name} "
            f"mạnh hơn "
            f"{second.name}"
        )

    else:
        print(
            f"{second.name} "
            f"mạnh hơn "
            f"{first.name}"
        )


def fusion_weapon():

    print("\n--- DUNG HỢP VŨ KHÍ ---")

    if len(inventory) < 2:
        print(
            "Cần ít nhất 2 vũ khí!"
        )
        return

    first = inventory[0]
    second = inventory[1]

    new_weapon = first + second

    inventory.pop(0)
    inventory.pop(0)

    inventory.append(new_weapon)

    print(
        "\n>> Dung hợp thành công!"
    )

    print(
        f"Vũ khí mới: "
        f"{new_weapon.name}"
    )

    print(
        f"Cấp: "
        f"{new_weapon.upgrade_level}"
    )

    print(
        f"Sát thương: "
        f"{new_weapon.calculate_total_damage()}"
    )


def main():

    while True:

        print(
            "\n===== LÒ RÈN VŨ KHÍ RIKKEI ====="
        )

        print("1. Xem kho")
        print("2. Rèn Weapon")
        print("3. Rèn MagicSword")
        print("4. Thẩm định")
        print("5. Dung hợp")
        print("6. Thoát")

        choice = input(
            "Chọn chức năng: "
        )

        match choice:

            case "1":
                display_inventory()

            case "2":
                create_weapon()

            case "3":
                create_magic_sword()

            case "4":
                compare_weapon()

            case "5":
                fusion_weapon()

            case "6":
                print(
                    "Thoát Lò Rèn. "
                    "Hẹn gặp lại Anh hùng!"
                )
                break

            case _:
                print(
                    "Lựa chọn không hợp lệ!"
                )


main()
from abc import ABC, abstractmethod


class Companion(ABC):
    """
    Lớp trừu tượng đại diện cho sinh vật đồng hành.
    """

    def __init__(self, name, level=1, **kwargs):
        self.name = name
        self.level = level

        super().__init__(**kwargs)

    def __add__(self, other):
        """
        Lai tạo sinh vật.
        """

        if type(self) != type(other):
            raise TypeError(
                "Chỉ có thể lai tạo 2 sinh vật cùng loài!"
            )

        new_name = f"{self.name} {other.name}"

        if isinstance(self, Dragon):

            return Dragon(
                new_name,
                bonus_atk=self.bonus_atk + other.bonus_atk,
                bonus_speed=self.bonus_speed + other.bonus_speed,
                level=max(self.level, other.level) + 1
            )

        elif isinstance(self, Pet):

            return Pet(
                new_name,
                bonus_atk=self.bonus_atk + other.bonus_atk,
                level=max(self.level, other.level) + 1
            )

        elif isinstance(self, Mount):

            return Mount(
                new_name,
                bonus_speed=self.bonus_speed + other.bonus_speed,
                level=max(self.level, other.level) + 1
            )

    @abstractmethod
    def unleash_skill(self):
        pass


class Pet(Companion):
    """
    Thú cưng chiến đấu.
    """

    def __init__(
            self,
            name,
            bonus_atk,
            level=1,
            **kwargs):

        self.bonus_atk = bonus_atk

        super().__init__(
            name=name,
            level=level,
            **kwargs
        )

    def unleash_skill(self):

        print(
            f">> {self.name} gầm gừ:"
        )

        print(
            f"Tấn công kẻ thù, gây "
            f"{self.bonus_atk} sát thương!"
        )


class Mount(Companion):
    """
    Thú cưỡi.
    """

    def __init__(
            self,
            name,
            bonus_speed,
            level=1,
            **kwargs):

        self.bonus_speed = bonus_speed

        super().__init__(
            name=name,
            level=level,
            **kwargs
        )

    def unleash_skill(self):

        print(
            f">> {self.name} hí vang:"
        )

        print(
            f"Tăng tốc độ di chuyển thêm "
            f"{self.bonus_speed} điểm!"
        )


class Dragon(Pet, Mount):
    """
    Rồng vừa chiến đấu vừa di chuyển.
    """

    def __init__(
            self,
            name,
            bonus_atk,
            bonus_speed,
            level=1):

        super().__init__(
            name=name,
            bonus_atk=bonus_atk,
            bonus_speed=bonus_speed,
            level=level
        )

    def unleash_skill(self):

        print(
            f">> {self.name} thị uy:"
        )

        print(
            f"- Tấn công kẻ thù, gây "
            f"{self.bonus_atk} sát thương!"
        )

        print(
            f"- Tăng tốc độ di chuyển thêm "
            f"{self.bonus_speed} điểm!"
        )


if __name__ == "__main__":

    print("===== TEST BẪY 1 =====")

    try:
        c = Companion("Test")
    except TypeError as e:
        print("Lỗi:", e)

    print("\n===== TEST LAI TẠO PET =====")

    p1 = Pet(
        "Sói Trắng",
        bonus_atk=50
    )

    p2 = Pet(
        "Sói Đen",
        bonus_atk=60
    )

    p3 = p1 + p2

    print(
        f"Tên: {p3.name}"
    )

    print(
        f"Level: {p3.level}"
    )

    print(
        f"ATK: {p3.bonus_atk}"
    )

    print("\n===== TEST BẪY 2 =====")

    m1 = Mount(
        "Ngựa",
        bonus_speed=10
    )

    try:
        test = p1 + m1
    except TypeError as e:
        print("Lỗi:", e)

    try:
        test = p1 + 100
    except TypeError as e:
        print("Lỗi:", e)

    print("\n===== TEST DRAGON =====")

    d1 = Dragon(
        "Rồng Lửa",
        bonus_atk=500,
        bonus_speed=200
    )

    print(
        f"ATK: {d1.bonus_atk}"
    )

    print(
        f"Speed: {d1.bonus_speed}"
    )

    print("\n===== TEST ĐA HÌNH =====")

    equipped = [
        p3,
        m1,
        d1
    ]

    for companion in equipped:
        companion.unleash_skill()
        print()
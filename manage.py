from dataclasses import dataclass


@dataclass
class UpstairsNeighbor:
    name: str
    favorite_tool: str
    has_metal_balls: bool
    is_awake: bool = True

    def start_renovation(self):
        """Метод імітації раптового ремонту."""
        if self.is_awake:
            print(
                f"[{self.name}] починає ремонт! Звучить улюблений інструмент: {self.favorite_tool}. Ваша люстра нервово хитається.")
        else:
            print(f"[{self.name}] зараз спить... Стіни відпочивають від {self.favorite_tool}.")

    def drop_metal_ball(self):
        """Знайомий кожному звук падіння чавунної кулі."""
        if self.has_metal_balls and self.is_awake:
            print(f"[{self.name}] упускає металеву кулю. Звук: 'Дзинь... гуп-гуп... коть-коть-коть' по ламінату.")
        elif not self.has_metal_balls:
            print(f"[{self.name}] сьогодні екологічний сусід — металевих куль не тримає.")
        else:
            print(f"[{self.name}] уві сні міцно стискає свою металеву кулю, щоб не впала.")

    def move_furniture(self, time_of_day: str):
        """Пересування меблів у найбільш непідходящий час."""
        if self.is_awake:
            print(
                f"[{self.name}] вважає, що {time_of_day} — найкращий час, щоб пересунути ту саму стару радянську шафу через усю кімнату.")
        else:
            print(f"[{self.name}] бачить сни, шафа залишається на місці. Поки що.")

    def toggle_sleep(self):
        self.is_awake = not self.is_awake
        if self.is_awake:
            print(f"⚠️ Увага! [{self.name}] прокинувся! Готуйте вушні затички.")
        else:
            print(f"🛑 [{self.name}] нарешті заснув. Настала настільки ідеальна тиша, що аж лякає...")


if __name__ == "__main__":
    classic_neighbor = UpstairsNeighbor(
        name="Петрович",
        favorite_tool="Перфоратор 'Бош'",
        has_metal_balls=True
    )

    gen_z_neighbor = UpstairsNeighbor(
        name="Студент Антон",
        favorite_tool="Bluetooth-колонка на максималках",
        has_metal_balls=False,
        is_awake=False
    )

    print("--- День із життя Петровича ---")
    classic_neighbor.start_renovation()
    classic_neighbor.drop_metal_ball()
    classic_neighbor.move_furniture("3:15 ночі")
    classic_neighbor.toggle_sleep()
    classic_neighbor.start_renovation()

    print("\n--- День із життя студента Антона ---")
    # Демонстрація методів для молодого сусіда, який спочатку спав
    gen_z_neighbor.start_renovation()
    gen_z_neighbor.toggle_sleep()
    gen_z_neighbor.start_renovation()
    gen_z_neighbor.drop_metal_ball()
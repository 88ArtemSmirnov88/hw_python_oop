from typing import Sequence, Union
from dataclasses import dataclass, asdict


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    MESSAGE = ('Тип тренировки: {}; '
               'Длительность: {:.3f} ч.; '
               'Дистанция: {:.3f} км; '
               'Ср. скорость: {:.3f} км/ч; '
               'Потрачено ккал: {:.3f}.')

    def get_message(self) -> None:
        t = asdict(self)
        return self.MESSAGE.format(*t.values())


class Training:
    """Базовый класс тренировки."""
    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65
    MIN_IN_HR: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError(
            'Пожалуйста, не считайте калории для объекта этого класса, '
            'а считайте их только для объектов классов '
            'дочерних этому классу')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            training_type=self.__class__.__name__,
            duration=self.duration,
            distance=self.get_distance(),
            speed=self.get_mean_speed(),
            calories=self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

    Coeff_calorie_1 = 18
    Coeff_calorie_2 = 20

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        """Вернуть информацию о потраченных калориях для тренировки: бег."""
        return ((self.Coeff_calorie_1 * self.get_mean_speed()
                - self.Coeff_calorie_2) * self.weight
                / self.M_IN_KM * self.duration * self.MIN_IN_HR)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    Coeff_calorie_1 = 0.035
    Coeff_calorie_2 = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Вернуть информацию о потраченных калориях
        для тренировки: спортивная ходьба."""
        return ((self.Coeff_calorie_1 * self.weight
                + (self.get_mean_speed() ** 2 // self.height)
                * self.Coeff_calorie_2 * self.weight)
                * self.duration * self.MIN_IN_HR)


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    Coeff_calorie_1 = 1.1
    Coeff_calorie_2 = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Вернуть информацию о средней скорости для тренировки: плавание."""
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Вернуть информацию о потраченных калориях
        для тренировки: плавание."""
        return ((self.get_mean_speed() + self.Coeff_calorie_1)
                * self.Coeff_calorie_2 * self.weight)


Read_workout_type: dict = {
    'SWM': Swimming,
    'RUN': Running,
    'WLK': SportsWalking
}


def read_package(workout_type: str, data:
                 Sequence[Union[int, float]]) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type in Read_workout_type:
        return Read_workout_type[workout_type](*data)
    else:
        raise ValueError('Тренировка не найдена')


def main(training: Training) -> None:
    """Главная функция."""
    info = InfoMessage.get_message(training.show_training_info())
    print(info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
class InfoMessage:
    """Информационное сообщение о тренировке."""

<<<<<<< HEAD
    def __init__(
            self,
            training_type: str,
            duration: float,
            distance: float,
            speed: float,
            calories: float,
    ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
=======
    def __init__(self, training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float,
                 ) -> None:
        self.training_type = training_type
        self.distance = distance
        self.speed = speed
        self.calories = calories
        self.duration = duration
>>>>>>> 13e8083f6da2b3cd11649938fb88cf763767469d

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""
<<<<<<< HEAD

    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    MIN_IN_HOUR: int = 60

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
    ) -> None:
=======
    LEN_STEP = 0.65
    M_IN_KM = 1000
    TRAINING_TYPE = ''

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
>>>>>>> 13e8083f6da2b3cd11649938fb88cf763767469d
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = self.get_distance() / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
<<<<<<< HEAD
        raise NotImplementedError(
            'Определите get_spent_calories в %s.' % (self.__class__.__name__)
        )

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__, self.duration,
                           self.get_distance(), self.get_mean_speed(),
                           self.get_spent_calories())
=======
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        info_message = InfoMessage(self.__class__.__name__,
                                   self.duration,
                                   self.get_distance(),
                                   self.get_mean_speed(),
                                   self.get_spent_calories())
        return info_message
>>>>>>> 13e8083f6da2b3cd11649938fb88cf763767469d


class Running(Training):
    """Тренировка: бег."""
<<<<<<< HEAD

    SPEED_MULTIPLIER: int = 18
    SPEED_DEDUCTION: int = 20

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return (
                (self.SPEED_MULTIPLIER * self.get_mean_speed()
                 - self.SPEED_DEDUCTION) * self.weight
                / self.M_IN_KM * self.duration
                * self.MIN_IN_HOUR
        )
=======
    CF_RUN_1 = 18
    CF_RUN_2 = 20
    TRAINING_TYPE = 'RUN'

    def get_spent_calories(self) -> float:
        cal = self.CF_RUN_1 * self.get_mean_speed() - self.CF_RUN_2
        calories = cal * self.weight / self.M_IN_KM * self.duration * 60
        return calories
>>>>>>> 13e8083f6da2b3cd11649938fb88cf763767469d


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
<<<<<<< HEAD

    WEIGHT_MULTIPLIER_1: float = 0.035
    NUM_DEGREE: int = 2
    WEIGHT_MULTIPLIER_2: float = 0.029

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
            height: float,
    ) -> None:
=======
    CF_WALK_1 = 0.035
    CF_WALK_2 = 2
    CF_WALK_3 = 0.029
    TRAINING_TYPE = 'WLK'

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: int) -> None:
>>>>>>> 13e8083f6da2b3cd11649938fb88cf763767469d
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
<<<<<<< HEAD
        """Получить количество затраченных калорий."""
        return (
                (self.WEIGHT_MULTIPLIER_1 * self.weight
                 + (self.get_mean_speed() ** self.NUM_DEGREE
                    // self.height) * self.WEIGHT_MULTIPLIER_2
                 * self.weight)
                * (self.duration * self.MIN_IN_HOUR)
        )
=======
        calories_1 = self.CF_WALK_1 * self.weight
        calories_2 = self.get_mean_speed() ** 2 // self.height
        calories_3 = calories_2 * self.CF_WALK_3 * self.weight
        calories = (calories_1 + calories_3) * self.duration * 60
        return calories
>>>>>>> 13e8083f6da2b3cd11649938fb88cf763767469d


class Swimming(Training):
    """Тренировка: плавание."""
<<<<<<< HEAD

    LEN_STEP: float = 1.38
    SPEED_SUMMAND: float = 1.1
    SPEED_MULTIPLIER: int = 2

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
            length_pool: int,
            count_pool: int,
    ) -> None:
=======
    CF_SW_1 = 1.1
    CF_SW_2 = 2
    LEN_STEP = 1.38
    TRAINING_TYPE = 'SWM'

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int) -> None:
>>>>>>> 13e8083f6da2b3cd11649938fb88cf763767469d
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
<<<<<<< HEAD
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return (
                (self.get_mean_speed()
                 + self.SPEED_SUMMAND)
                * self.SPEED_MULTIPLIER
                * self.weight
        )


TRAINING_CODE_DICT = {'SWM': Swimming, 'RUN': Running, 'WLK': SportsWalking}
=======
        speed_1 = self.length_pool * self.count_pool
        self.speed = speed_1 / super().M_IN_KM / self.duration
        return self.speed

    def get_spent_calories(self) -> float:
        calories_1 = self.get_mean_speed() + self.CF_SW_1
        calories = calories_1 * self.CF_SW_2 * self.weight
        return calories
>>>>>>> 13e8083f6da2b3cd11649938fb88cf763767469d


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
<<<<<<< HEAD
    return TRAINING_CODE_DICT[workout_type](*data)
=======
    type_dict = {'SWM': Swimming, 'RUN': Running, 'WLK': SportsWalking}
    return type_dict[workout_type](*data)
>>>>>>> 13e8083f6da2b3cd11649938fb88cf763767469d


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

import rt_with_exceptions as task
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            r = task.Runner('Вася', -5)
            if r.speed <= 0:
                raise ValueError(f'Скорость не может быть отрицательной, сейчас: {r.speed}')
            for _ in range(10):
                r.walk()
            self.assertEqual(r.distance, 50)
            logging.info('"test_run" выполнен успешно')
        except ValueError:

            logging.warning(msg='Скорость не может быть отрицательной,', exc_info=True)


    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runner = task.Runner(2)
            if not isinstance(runner.name, str):
                raise TypeError(f'Имя не может быть {type(runner.name).__name__}')
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning(msg="Неверный тип данных для имени экземпляра Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        partner1 = task.Runner('Kate')
        partner2 = task.Runner('Anna')
        for _ in range(10):
            partner1.walk()
            partner2.run()
        self.assertNotEqual(partner1.distance, partner2.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding="utf-8",
                    format='%(asctime)s | %(levelname)s | %(message)s')



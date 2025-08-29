import unittest
from pathlib import Path

from project.core import database, generator, models


class TestGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        db_file = Path(__file__).resolve().parent.parent / "data" / "db.sqlite3"
        if db_file.exists():
            db_file.unlink()
        database.connect_to_db()
        database.create_tables()
        database.load_initial_data()

    def _exercise_names(self, session):
        names = []
        for gb in session.blocks_obj:
            for eb in gb.exercises:
                names.append(eb.exercise.name)
        return names

    def test_variability_zero_same(self):
        params = {
            'duration_minutes': 45,
            'type_of_session': 'collective',
            'variability': 0,
            'objective': 'Endurance',
            'focus': 'Full-body',
            'available_equipment': ['Kettlebell', 'Bodyweight']
        }
        res1 = generator.generate_session(params)
        res2 = generator.generate_session(params)
        self.assertEqual(self._exercise_names(res1), self._exercise_names(res2))

    def test_variability_high_diff(self):
        params = {
            'duration_minutes': 45,
            'type_of_session': 'collective',
            'variability': 90,
            'objective': 'Endurance',
            'focus': 'Full-body',
            'available_equipment': ['Kettlebell', 'Bodyweight']
        }
        res1 = generator.generate_session(params)
        res2 = generator.generate_session(params)
        self.assertNotEqual(self._exercise_names(res1), self._exercise_names(res2))

    def test_generation_error(self):
        params = {
            'duration_minutes': 45,
            'type_of_session': 'collective',
            'objective': 'Force',
            'focus': 'Haltérophilie',
            'available_equipment': ['Aucun']
        }
        with self.assertRaises(generator.GenerationError):
            generator.generate_session(params)

    def test_volume_factor(self):
        base_params = {
            'duration_minutes': 45,
            'type_of_session': 'collective',
            'focus': 'Full-body',
            'available_equipment': ['Kettlebell', 'Bodyweight']
        }
        params1 = base_params.copy()
        params1['volume_factor'] = 1.0
        sess1 = generator.generate_session(params1)
        params2 = base_params.copy()
        params2['volume_factor'] = 1.5
        sess2 = generator.generate_session(params2)
        core1 = [b for b in sess1.blocks_obj if b.block.block_type == 'Core']
        core2 = [b for b in sess2.blocks_obj if b.block.block_type == 'Core']
        self.assertGreater(len(core2), len(core1))


if __name__ == '__main__':
    unittest.main()

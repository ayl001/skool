# Ajout du répertoire parent au sys.path pour pouvoir importer les modules
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '../../')))
# Imports standard et tiers
import re
import unittest
from io import StringIO
from unittest.mock import MagicMock, Mock
# Importation des classes de l'application
from business.school import School
from models.course import Course
from models.teacher import Teacher
from models.student import Student


class TestSchool(unittest.TestCase):

    def test_add_course(self):
        # Création de l'objet School
        school = School()

        # Création d'un mock pour représenter l'objet Course
        course = Mock(spec=Course)  # Simule un objet de type Course

        # Valeur attendue : le mock course
        expected_value = course

        # Appel de la méthode add_course avec le mock course
        school.add_course(course)

        # Vérifie que le dernier cours ajouté est bien le mock course
        self.assertEqual(school.courses[-1], expected_value)

    def test_add_teacher(self):
        school = School()

        # Création d'un mock pour représenter l'objet Teacher
        teacher = Mock(spec=Teacher)

        # Valeur attendue : le mock teacher
        expected_value = teacher

        # Appel de la méthode add_teacher avec le mock teacher
        school.add_teacher(teacher)

        # Vérifie que le dernier enseignant ajouté est bien le mock teacher
        self.assertEqual(school.teachers[-1], expected_value)

    def test_add_student(self):
        school = School()

        # Création d'un mock pour représenter l'objet Student
        student = Mock(spec=Student)

        # Valeur attendue : le mock student
        expected_value = student

        # Appel de la méthode add_student avec le mock student
        school.add_student(student)

        # Vérifie que le dernier étudiant ajouté est bien le mock student
        self.assertEqual(school.students[-1], expected_value)

    # ... reste du code du test

    def test_display_courses_list(self):

        # Création de l'objet School
        school = School()
        # Création de MagicMocks pour les objets Course, Teacher et Student
        course_1 = MagicMock(spec=Course)
        course_2 = MagicMock(spec=Course)
        student_1 = MagicMock(spec=Student)
        student_2 = MagicMock(spec=Student)

        # Configuration des mocks pour la méthode
        # 'students_taking_it' de chaque cours
        course_1.students_taking_it = [student_1, student_2]
        course_2.students_taking_it = [student_1]

        # Configuration des mocks pour la représentation des cours
        course_1.__str__.return_value = "Maths"
        course_2.__str__.return_value = "Science"

        # Ajout des cours à l'école
        school.courses = [course_1, course_2]

        # Redirection de la sortie print dans un objet StringIO
        # pour capter ce qui est imprimé
        captured_output = StringIO()
        sys.stdout = captured_output

        # Appel de la méthode display_courses_list
        school.display_courses_list()

        # Format de la sortie attendue
        expected_output = (
            "cours de Maths\n"
            "- <MagicMock spec='Student' id='...'>\n"
            "- <MagicMock spec='Student' id='...'>\n\n"
            "cours de Science\n"
            "- <MagicMock spec='Student' id='...'>\n\n"
        )

        # Remplace les IDs dynamiques par "..." pour permettre la comparaison
        actual_output = re.sub(r"<MagicMock spec='Student' id='[^']*'>",
                               "<MagicMock spec='Student' id='...'>",
                               captured_output.getvalue())

        # Vérification de ce qui a été imprimé par la méthode
        self.assertEqual(actual_output, expected_output)

        # Restauration de la sortie standard après le test
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()

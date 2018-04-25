import os
import custom_parser
from project_setup import Project
from genetic_algorithm import GeneticAlgorithm

if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'activities.csv')
    component_list = custom_parser.parse(csv_path=csv_path)
    '''for component in component_list:
        component.fancy_print()
        print('\n')'''
    project = Project(component_list)
    project.print_planning()
    gen_algo = GeneticAlgorithm(component_list)
    gen_algo.run(10000)

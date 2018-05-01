import os
import custom_parser
from project_setup import Project
from genetic_algorithm import GeneticAlgorithm
from visualization import visualize

if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'activities.csv')
    component_list = custom_parser.parse(csv_path=csv_path)

    project = Project(component_list)
    project.print_planning()
    print("Min:", project.calc_min_fitness())
    print("Max:", project.calc_max_fitness())

    gen_algo = GeneticAlgorithm(component_list)
    gen_algo.run(300)

    print("Best project planning:")
    gen_algo.get_best_project().print_planning()

    visualization_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'example', 'index.html')
    visualize(gen_algo.get_best_project(), visualization_path)

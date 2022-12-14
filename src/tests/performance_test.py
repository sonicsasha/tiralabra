import time
import os
import sys
from enum import Enum
import xlsxwriter

# Needed so that the classes are properly imported.
sys.path.append("src")

from labyrinth import Labyrinth
from generators.path_generator import PathGenerator
from generators.maze_generator_dfs import MazeGeneratorDFS
from generators.maze_generator_prim import MazeGeneratorPrim


# pylint: disable=line-too-long
# When doing test cases, the prints are long. Dividing prints into multiple lines end up being confusing.


class PerformanceTestScenarios(Enum):
    """An enumerator used to determine what the user wants to test."""

    RANDOM_PATH = 1
    DFS_MAZE = 2
    PRIM_MAZE = 3


# pylint: disable=too-many-arguments
def execute_and_report_tests_to_worksheet(
    test_cases: list,
    worksheet: xlsxwriter.workbook.Worksheet,
    test_title: str,
    x_axis_name: str,
    y_axis_name: str,
    scenario: PerformanceTestScenarios,
):
    """A function, which runs tests on a given set of inputs and then exports
    writes those results to an Excel file and makes a graph out of the results.

    Args:
        test_cases (list): A list of dictionaries with a given dataset. Has to include the following keys: width, height and 'steps required'.
        worksheet (xlsxwriter.workbook.Worksheet): Worksheet to which the data will be written. Will overwrite existing data.
        test_title (str): What the test is called. Is the title of the graph.
        x_axis_name (str): What the x axis of the graph should be called.
        y_axis_name (str): What the y axis of the graph should be called.
        scenario (TestScenarios): What tests should be run with the given data. Check the class TestScenarios for possible values.
    """
    print(f"Now testing: {test_title}")

    worksheet.write_row("A1", [test_title])

    worksheet.write_row("A3", ["Width", "Height", "Steps required", "Execution time"])
    row_number = 4

    for case in test_cases:
        print(
            f"Testing with parameters width: {case['width']}, height: {case['height']}, steps required: {case['steps required']}"
        )
        labyrinth = Labyrinth(case["width"], case["height"], case["steps required"])
        start_time = time.time()

        if scenario == PerformanceTestScenarios.RANDOM_PATH:
            PathGenerator(labyrinth).generate_random_shortest_path()
            PathGenerator(labyrinth).generate_sidesteps()
        elif scenario == PerformanceTestScenarios.DFS_MAZE:
            PathGenerator(labyrinth).generate_random_shortest_path()
            PathGenerator(labyrinth).generate_sidesteps()
            MazeGeneratorDFS(labyrinth).generate_maze_around_path()
        elif scenario == PerformanceTestScenarios.PRIM_MAZE:
            PathGenerator(labyrinth).generate_random_shortest_path()
            PathGenerator(labyrinth).generate_sidesteps()
            MazeGeneratorPrim(labyrinth).generate_maze_around_path()

        execution_time = time.time() - start_time

        print(f"Finished test in {execution_time} seconds")
        print()

        worksheet.write_row(
            f"A{row_number}",
            [case["width"], case["height"], case["steps required"], execution_time],
        )
        row_number += 1

    chart = workbook.add_chart({"type": "scatter", "subtype": "straight_with_markers"})

    chart.add_series(
        {
            "categories": f"={worksheet.get_name()}!$C$4:$C${row_number-1}",
            "values": f"={worksheet.get_name()}!$D$4:$D${row_number-1}",
        }
    )

    chart.set_style(15)
    chart.set_x_axis({"name": x_axis_name})
    chart.set_y_axis({"name": y_axis_name})
    chart.set_title({"name": test_title})
    worksheet.insert_chart("F4", chart)


if __name__ == "__main__":
    FILE_NAME = "performance_report.xlsx"
    workbook = xlsxwriter.Workbook(FILE_NAME)
    worksheet_path = workbook.add_worksheet("Path")

    # Test the performance of the sidestep algorithm
    # Everything is done on a 10001x10001 maze so that the size of the labyrinth would have minimal effect on the performance of the algorithm.
    path_generation_test_cases = [
        {"width": 10001, "height": 10001, "steps required": 20000},
        {"width": 10001, "height": 10001, "steps required": 24000},
        {"width": 10001, "height": 10001, "steps required": 28000},
        {"width": 10001, "height": 10001, "steps required": 38000},
        {"width": 10001, "height": 10001, "steps required": 48000},
        {"width": 10001, "height": 10001, "steps required": 55000},
        {"width": 10001, "height": 10001, "steps required": 60000},
        {"width": 10001, "height": 10001, "steps required": 68000},
        {"width": 10001, "height": 10001, "steps required": 76000},
        {"width": 10001, "height": 10001, "steps required": 84000},
        {"width": 10001, "height": 10001, "steps required": 92000},
        {"width": 10001, "height": 10001, "steps required": 100000},
        {"width": 10001, "height": 10001, "steps required": 140000},
        {"width": 10001, "height": 10001, "steps required": 180000},
        {"width": 10001, "height": 10001, "steps required": 220000},
        {"width": 10001, "height": 10001, "steps required": 260000},
        {"width": 10001, "height": 10001, "steps required": 300000},
        {"width": 10001, "height": 10001, "steps required": 340000},
        {"width": 10001, "height": 10001, "steps required": 380000},
        {"width": 10001, "height": 10001, "steps required": 420000},
        {"width": 10001, "height": 10001, "steps required": 460000},
        {"width": 10001, "height": 10001, "steps required": 500000},
        {"width": 10001, "height": 10001, "steps required": 620000},
        {"width": 10001, "height": 10001, "steps required": 760000},
        {"width": 10001, "height": 10001, "steps required": 880000},
    ]

    # Test the maze generation algorithms with these inputs. Notice then when input is raised by x, the labyrinth grows in size by x^2.
    maze_generation_test_cases = [
        {"width": 5, "height": 5},
        {"width": 11, "height": 11},
        {"width": 51, "height": 51},
        {"width": 101, "height": 101},
        {"width": 301, "height": 301},
        {"width": 501, "height": 501},
        {"width": 1001, "height": 1001},
        {"width": 2001, "height": 2001},
        {"width": 5001, "height": 5001},
        {"width": 8001, "height": 8001},
        {"width": 10001, "height": 10001},
    ]

    for test_case in maze_generation_test_cases:
        # When testing the maze generation algorithms, we only want to use the minimum amount of steps
        test_case["steps required"] = test_case["width"] + test_case["height"] - 2

    # Test the path generating algorithm.
    execute_and_report_tests_to_worksheet(
        path_generation_test_cases,
        worksheet_path,
        "Execution time in relation to sidesteps done in a 10001x10001 grid when generating a random path",
        "Amount of sidesteps done",
        "Execution time (s)",
        PerformanceTestScenarios.RANDOM_PATH,
    )

    # Test the randomized DFS algorithm.
    worksheet_dfs = workbook.add_worksheet("DFS")

    execute_and_report_tests_to_worksheet(
        maze_generation_test_cases,
        worksheet_dfs,
        "Execution time in relation to the size of the maze when generating a maze using DFS",
        "Size of a side of the maze",
        "Execution time (s)",
        PerformanceTestScenarios.DFS_MAZE,
    )

    # Test the randomized Prim's algorithm.
    worksheet_prim = workbook.add_worksheet("Prim")

    execute_and_report_tests_to_worksheet(
        maze_generation_test_cases,
        worksheet_prim,
        "Execution time in relation to the size of the maze when generating a maze using PRIM",
        "Size of a side of the maze",
        "Execution time (s)",
        PerformanceTestScenarios.PRIM_MAZE,
    )

    # pylint: disable=anomalous-backslash-in-string
    # False positive when printing \performance
    print(f"Tests done! Wrote the contents to {os.path.abspath(FILE_NAME)}")
    # pylint: enable=anomalous-backslash-in-string
    workbook.close()

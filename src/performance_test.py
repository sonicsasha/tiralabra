import time
import os
from enum import Enum
import xlsxwriter

from labyrinth import Labyrinth


#pylint: disable=line-too-long
#When doing test cases, the prints are long. Dividing prints into multiple lines end up being confusing.

class TestScenarios(Enum):
    """An enumerator used to determine what the user wants to test."""
    RANDOM_PATH = 1
    DFS_MAZE = 2
    PRIM_MAZE = 3

#pylint: disable=too-many-arguments
def execute_and_report_tests_to_worksheet(test_cases: list, worksheet : xlsxwriter.workbook.Worksheet, test_title: str, x_axis_name: str, y_axis_name: str, scenario: TestScenarios):
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

    worksheet.write_row("A1",[test_title])

    worksheet.write_row("A3",["Width","Height","Steps required", "Execution time"])
    row_number = 4

    for case in test_cases:
        print(f"Testing with parameters width: {case['width']}, height: {case['height']}, steps required: {case['steps required']}")
        labyrinth = Labyrinth(case["width"], case["height"], case["steps required"])
        start_time = time.time()

        if scenario == TestScenarios.RANDOM_PATH:
            labyrinth.generate_random_shortest_path()
            labyrinth.generate_sidesteps()
        elif scenario == TestScenarios.DFS_MAZE:
            labyrinth.generate_random_shortest_path()
            labyrinth.generate_sidesteps()
            labyrinth.generate_maze_around_path_dfs()
        elif scenario == TestScenarios.PRIM_MAZE:
            labyrinth.generate_random_shortest_path()
            labyrinth.generate_sidesteps()
            labyrinth.generate_maze_around_path_prim()

        execution_time = time.time()-start_time

        print(f"Finished test in {execution_time} seconds")
        print()

        worksheet.write_row(f"A{row_number}", [case['width'],case['height'],case['steps required'],execution_time])
        row_number += 1

    chart = workbook.add_chart({"type": "scatter",
                                "subtype": "straight_with_markers"})

    chart.add_series({
        "categories": f"={worksheet.get_name()}!$C$4:$C${row_number-1}",
        "values": f"={worksheet.get_name()}!$D$4:$D${row_number-1}"
        })

    chart.set_style(15)
    chart.set_x_axis({"name": x_axis_name})
    chart.set_y_axis({"name": y_axis_name})
    chart.set_title({"name": test_title})
    worksheet.insert_chart("F4", chart)



if __name__ == "__main__":
    workbook = xlsxwriter.Workbook("performance_report.xlsx")
    worksheet_path = workbook.add_worksheet("Path")

    #Test the performance of the sidestep algorithm
    #Everything is done on a 10001x10001 maze so that the size of the labyrinth would have minimal effect on the performance of the algorithm.
    path_generation_test_cases =    [{"width": 10001, "height": 10001, "steps required": 20000},
                                    {"width": 10001, "height": 10001, "steps required": 20004},
                                    {"width": 10001, "height": 10001, "steps required": 20040},
                                    {"width": 10001, "height": 10001, "steps required": 20400},
                                    {"width": 10001, "height": 10001, "steps required": 24000},
                                    {"width": 10001, "height": 10001, "steps required": 28000},
                                    {"width": 10001, "height": 10001, "steps required": 38000},
                                    {"width": 10001, "height": 10001, "steps required": 48000},
                                    {"width": 10001, "height": 10001, "steps required": 55000},
                                    {"width": 10001, "height": 10001, "steps required": 60000}]

    #Test the maze generation algorithms with these inputs. Notice then when input is raised by x, the labyrinth grows in size by x^2.
    maze_generation_test_cases =    [{"width": 5, "height": 5},
                                    {"width": 11, "height": 11},
                                    {"width": 51, "height": 51},
                                    {"width": 101, "height": 101},
                                    {"width": 301, "height": 301},
                                    {"width": 501, "height": 501},
                                    {"width": 1001, "height": 1001},
                                    {"width": 2001, "height": 2001},
                                    {"width": 5001, "height": 5001},
                                    {"width": 8001, "height": 8001},
                                    {"width": 10001, "height": 10001}
                                    ]

    for test_case in maze_generation_test_cases:
        #When testing the maze generation algorithms, we only want to use the minimum amount of steps
        test_case["steps required"] = test_case["width"] + test_case["height"] - 2



    #Test the path generating algorithm.
    execute_and_report_tests_to_worksheet(path_generation_test_cases,
            worksheet_path,
            "Execution time in relation to sidesteps done in a 10001x10001 grid when generating a random path",
            "Amount of sidesteps done",
            "Execution time (s)",
            TestScenarios.RANDOM_PATH)

    #Test the randomized DFS algorithm.
    worksheet_dfs = workbook.add_worksheet("DFS")

    execute_and_report_tests_to_worksheet(maze_generation_test_cases,
    worksheet_dfs,
    "Execution time in relation to the size of the maze when generating a maze using DFS",
    "Size of a side of the maze",
    "Execution time (s)",
    TestScenarios.DFS_MAZE)

    #Test the randomized Prim's algorithm.
    worksheet_prim = workbook.add_worksheet("Prim")

    execute_and_report_tests_to_worksheet(maze_generation_test_cases,
    worksheet_prim,
    "Execution time in relation to the size of the maze when generating a maze using PRIM",
    "Size of a side of the maze",
    "Execution time (s)",
    TestScenarios.PRIM_MAZE)

    #pylint: disable=anomalous-backslash-in-string
    #False positive when printing \performance
    print(f"Tests done! Wrote the contents to {os.path.dirname(__file__)}\performance_report.xlsx")
    #pylint: enable=anomalous-backslash-in-string
    workbook.close()

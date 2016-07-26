"""
Finds the rolling average and the rolling maximum for windows of
two sizes: 3 and 20
Start with [0] index and i++ until i = N
Returns tuple with ((win1-avg), (win2-max), (win2-avg), (win2-max))

In python shell:
    - from logic import main
    - import your own list, or
    - from logic import demo_list
    - call 'main(your_chosen_list)'

functions:
      iterator;
      validator;
      get_window;
      get_window_average;
      get_window_max;
      set_results_to_tuple;
"""


def validator(window_size, index):
    """Return bool, True if list index range is at or greater to windowsize."""
    return window_size <= index + 1


def get_window(the_list, window_size, index):
    """Return values of list within the specified window."""
    window_max = index + 1
    window_min = window_max - window_size
    window = the_list[window_min:window_max]
    return window


def get_window_average(window):
    """Pass in window values and return their average."""
    return int(sum(window)/len(window))


def get_window_max(window):
    """Pass in window values and the highest value."""
    return max(window)


def results_to_tuple(results):
    """Pass in list and return tuple of list."""
    return tuple(results)


def print_results(tupled_results):
    """Pass in item for print."""
    print(tupled_results)


def iterator(the_list, window_sizes):
    """Iterate over list indeces and print results of window sizes."""
    for index, value in enumerate(the_list):
        results = []

        for window_size in window_sizes:

            if validator(window_size, index):
                window = get_window(the_list, window_size, index)
                window_average = get_window_average(window)
                window_max = get_window_max(window)
            else:
                window_average = None
                window_max = None

            results.append(window_average)
            results.append(window_max)

        tupled_results = results_to_tuple(results)
        print_results(tupled_results)


demo_list = list(range(1, 41))  # import to debug/test module after alterations


def main(demo_list):
    window_sizes = [3, 20]
    iterator(demo_list, window_sizes)

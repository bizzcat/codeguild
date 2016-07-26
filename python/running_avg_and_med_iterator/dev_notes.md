Problem split into two solutions simply by accident. modular logic, using basic function call stacks as opposed to classes was created first without thorough reading of instructions. Prior to submission, I noticed my error and came back to create class_logic to meet Python project requirements.

No third-party libraries or packages were used in development.


---------------------------------------------

To execute modular_logic, open python shell and:
  - from logic import main
  - from logic import demo_list  (or import your own list)
  - main(your_chosen_list)

To execute class_logic, simply enter in terminal:
  - python3 class_logic.py

---------------------------------------------

Was having trouble in Class iterator:

results
```
3        # window length
20       # window length
(38, 39, 29, 39)
3
20
(39, 40, 30, 40)
2        # <-- begins decreasing
19
(39, 40, 31, 40)
1
18
(40, 40, 31, 40)
0
```

Corresponidng error message:
```  
Traceback (most recent call last):
    File "logic2.py", line 108, in <module>
      for result in AvgMedTuple_iter(demo_list, window_sizes):
    File "logic2.py", line 96, in __next__
      window_average = get_window_average(window)
    File "logic2.py", line 72, in get_window_average
      return int(sum(window)/len(window))
  ZeroDivisionError: division by zero
```


Fixed by:
```
if self.index < len(self.list):
        self.index += 1

    else:
        raise StopIteration
```
---------------------------------------------

If I had more time to work on the problem I would certainly work to flatten the function call stack; improve naming convention; write clear and comprehensive doc strings; improve both efficiency and modularity of functions for more performant space-time quotient

If I had to return the median as a third value in the tuple I would generate a function stack similar to this:
```
def even(num)
  return num % 2 == 0


def get_window_median(window):
  if even(len(window)):
    second_index = len(window) / 2
    first_index = second_index - 1

    second_value = window[second_index]
    first_value = window[first_index]

    return (second_value / first_value) / 2

  else:
    index = int(len(window))

    return window(index)
```

---------------------------------------------

With substantially larger window sizes (1^4, 1^6), I would:
  - create two iterators:

    - one iterates over range(1^4, 1^6) with a 1^4 window, and pass in 'None' as last two values in tuple by default; the other iterates over range(1^6, N), with both 1^4 and 1mil window sizes.
    (eliminates precisely 1,010,000 unnecessary computations)

  - improve the space-time equation by creating the two iterators above

  - for each of my retrieval functions in modular_logic (ie: 'get_XYZ'), I would pass in both windows and return coupled values, instead of iterating through each window individually and aggregating results later.

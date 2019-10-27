import os


def find_files(suffix, path):
    """
        Find all files beneath path with file name suffix.

        Note that a path may contain further subdirectories
        and those subdirectories may also contain further subdirectories.

        There are no limit to the depth of the subdirectories can be.

        Args:
          suffix(str): suffix if the file name to be found
          path(str): path of the file system

        Returns:
           a list of paths
    """

    # check if path is valid and is a valid directory
    if not isinstance(path, str) or not isinstance(suffix, str) or not os.path.isdir(path):
        return []

    # get all the files+directories inside current directory
    files_and_directories = os.listdir(path)

    # filter files
    output = []
    for file in files_and_directories:
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path) and full_path.endswith(suffix):
            output.append(full_path)
        elif os.path.isdir(full_path):
            # walk through all the files inside this directory and its sub-directories in a recursive way
            output += find_files(suffix, full_path)
            pass

    return output


def test_cases():
    files = find_files(".c", "./testdir")
    print(files) # should return ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
    assert (files == ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c'])

    # edge cases
    # invalid directory
    files = find_files(".c", "./abcd-ramz") # should return empty list
    print(files)
    assert (files == [])

    # invalid suffix
    files = find_files(None, "./testdir")  # should return empty list
    print(files)
    assert (files == [])

    #None path
    files = find_files(None, None)  # should return empty list
    print(files)
    assert (files == [])

    # empty suffix
    files = find_files("", "testdir")  # should return all files, not adding assert because on Mac there are extra files (.DS_Store) so assert will fail even if code correct
    print(files)

test_cases()
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

    files_with_suffix = list()
    try:
        if os.path.isdir(path):
            listing = os.listdir(path)
            listing = [f"{path}/{ele}" for ele in listing]

            for sub_path in listing:
                if os.path.isfile(sub_path) and sub_path.endswith(suffix, len(suffix)):
                    files_with_suffix.append(sub_path)
                elif os.path.isdir(sub_path):
                    files_with_suffix = files_with_suffix + find_files(suffix, sub_path)
        elif os.path.isfile(path) and path.endswith(suffix):
            files_with_suffix.append(path)
    except Exception as e:
        pass

    return files_with_suffix


# Preparing data
# Download the testdir.zip and unzip it at $HOME

# Test #1: Finding all the files with suffix .c in the testdir
print(f"\n{'#' * 10} Test #1 {'#' * 10} ")
for _path_ in find_files(".c", f"{os.environ['HOME']}/testdir"):
    print(_path_)
# Output: ($HOME will replaced with the actual path string)
# $HOME/testdir/subdir3/subsubdir1/b.c
# $HOME/testdir/t1.c
# $HOME/testdir/subdir5/a.c
# $HOME/testdir/subdir1/a.c

# Test #2: Path of the file which exists and have a suffix .c
print(f"\n{'#' * 10} Test #2 {'#' * 10} ")
for _path_ in find_files(".c", f"{os.environ['HOME']}/testdir/subdir3/subsubdir1/b.c"):
    print(_path_)
# Output: ($HOME will replaced with the actual path string)
# $HOME/testdir/subdir3/subsubdir1/b.c

# Test #3: Path of the file which exists and does not have a suffix .c
print(f"\n{'#' * 10} Test #3 {'#' * 10} ")
for _path_ in find_files(".c", f"{os.environ['HOME']}/testdir/t1.h"):
    print(_path_)
# Output: ($HOME will replaced with the actual path string)
#

# Test #4: Empty String
print(f"\n{'#' * 10} Test #4 {'#' * 10} ")
for _path_ in find_files(".c", ""):
    print(_path_)
# Output: ($HOME will replaced with the actual path string)
#

# Test #5: Null
print(f"\n{'#' * 10} Test #5 {'#' * 10} ")
for _path_ in find_files(".c", None):
    print(_path_)
# Output: ($HOME will replaced with the actual path string)
#

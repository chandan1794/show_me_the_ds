from collections import deque


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __repr__(self):
        return f"Group Name: {self.name}"


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    group_queue = deque()
    group_queue.append(group)
    try:
        while True:
            curr_group = group_queue.pop()
            if user in curr_group.get_users():
                return True
            else:
                group_queue.extend(curr_group.get_groups())
    except Exception as err:
        return False


# Preparing Data
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test 1: Child exists
print(f"\n{'#' * 10} Test #1 {'#' * 10} ")
print(is_user_in_group(sub_child_user, parent))
# Output: True

# Test 2: Child does not exists
print(f"\n{'#' * 10} Test #2 {'#' * 10} ")
print(is_user_in_group("parent", parent))
# Output: False

# Test 3: Empty Value
print(f"\n{'#' * 10} Test #3 {'#' * 10} ")
print(is_user_in_group("", parent))
# Output: False

# Test 4: Null Value
print(f"\n{'#' * 10} Test #4 {'#' * 10} ")
print(is_user_in_group(None, parent))
# Output: False

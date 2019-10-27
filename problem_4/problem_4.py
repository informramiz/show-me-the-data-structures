"""
In Windows Active Directory, a group can consist of user(s) and group(s) themselves.
We can construct this hierarchy as such. Where User is represented by str representing their ids.

Write a function that provides an efficient look up of whether the user is in a group.
"""


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


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None or len(user) == 0 or group is None:
        return False

    if user in group.users:
        return True

    # search in sub-groups
    for sub_group in group.groups:
        return is_user_in_group(user, sub_group)

    # user not found
    return False


def test():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    output = is_user_in_group(sub_child_user, parent) # should be True
    print(output)
    assert (output is True)

    output = is_user_in_group(sub_child_user, child)  # should be True
    print(output)
    assert (output is True)

    output = is_user_in_group("Ramiz", parent)  # should be False
    print(output)
    assert (output is False)

    # edge cases
    output = is_user_in_group("", parent)  # should be False
    print(output)
    assert (output is False)

    output = is_user_in_group(None, parent)  # should be False
    print(output)
    assert (output is False)


test()

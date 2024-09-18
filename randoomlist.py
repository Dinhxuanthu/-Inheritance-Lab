import random

class RandomList(list):
    def get_random_element(self):
        if not self:
            raise IndexError("The list is empty.")
        random_index = random.randint(0, len(self) - 1)
        return self.pop(random_index)

# Example usage
random_list = RandomList([1, 2, 3, 4, 5])

print(f"Original list: {random_list}")
random_element = random_list.get_random_element()
print(f"Random element removed: {random_element}")
print(f"List after removal: {random_list}")

class Myclass:
    def __init__(self, value):
        self.__value = value

    def show(self):
        print(f"value is {self.__value}")

    @property #getter
    def ten_value(self):
        return 10 * self.__value

    @ten_value.setter #setter
    def ten_value(self, new_value):
        self.__value = new_value / 10


obj = Myclass(10)
obj.ten_value = 34
print(obj.ten_value)
obj.show()


# Your code is **correct**, and it’s a great example of using both `@property` and `@property.setter` in Python!

# Let me walk you through it step by step to explain what's happening — especially the logic behind the setter and getter.

# ---

# ## ✅ Code Breakdown

# ```python
# class Myclass:
#     def __init__(self, value):
#         self.__value = value
# ```

# * Private attribute `__value` is set in the constructor.

# ---

# ```python
#     def show(self):
#         print(f"value is {self.__value}")
# ```

# * Simple method to print the current value of `__value`.

# ---

# ```python
#     @property
#     def ten_value(self):
#         return 10 * self.__value
# ```

# * When you do `obj.ten_value`, this method is called.
# * It returns 10 times the internal value.

# ---

# ```python
#     @ten_value.setter
#     def ten_value(self, new_value):
#         self.__value = new_value / 10
# ```

# * When you **assign** a value to `obj.ten_value`, this setter is triggered.
# * It takes `new_value`, and stores `new_value / 10` in `__value`.

# ---

# ## 📦 Runtime Flow

# ### Step 1:

# ```python
# obj = Myclass(10)
# ```

# * `__value` is now `10`.

# ### Step 2:

# ```python
# obj.ten_value = 34
# ```

# * The **setter** runs:

#   * `self.__value = 34 / 10` → `3.4`

# ### Step 3:

# ```python
# print(obj.ten_value)
# ```

# * The **getter** runs:

#   * `10 * 3.4 = 34.0`

# 🖨️ **Output:**

# ```
# 34.0
# ```

# ### Step 4:

# ```python
# obj.show()
# ```

# 🖨️ **Output:**

# ```
# value is 3.4
# ```

# ---

# ## ✅ Final Output of Your Code:

# ```
# 34.0
# value is 3.4
# ```

# ---

# ## 💡 Summary

# | Action               | Method Used        | Effect                         |
# | -------------------- | ------------------ | ------------------------------ |
# | `obj.ten_value`      | `@property` getter | Returns `10 * __value`         |
# | `obj.ten_value = 34` | `@setter`          | Sets `__value = 34 / 10 = 3.4` |
# | `obj.show()`         | Regular method     | Prints the actual `__value`    |

# Let me know if you want to add a **deleter**, validation, or type-checking!
 
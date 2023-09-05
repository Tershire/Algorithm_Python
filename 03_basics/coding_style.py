# coding_style.py

# Tershire
# 2023 SEP 05


# use immutable initial value for an argument /////////////////////////////////
def compute_error_X(a, b = []):
    if b == []:
        pass

def compute_error_O(a, b = None):
    if b == None:
        pass

# concise flow control ////////////////////////////////////////////////////////
a = []
if not a:
    print("yea")

b = None
if not b:
    print("yeb")

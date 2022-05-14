# Function Call:
#
# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
# Output:
#
#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474
# Situations that will return an error:
# Error: Too many problems.
# Error: Operator must be '+' or '-'.
# Error: Numbers must only contain digits.
# Error: Numbers cannot be more than four digits.
# -----------------------------------------------
# There should be a single space between the operator and the longest of the two operands,
# the operator will be on the same line as the second operand, both operands will be in the
# same order as provided (the first will be the top one and the second will be the bottom.
# Numbers should be right-aligned.
# There should be four spaces between each problem.
# There should be dashes at the bottom of each problem.
# The dashes should run along the entire length of each problem individually.
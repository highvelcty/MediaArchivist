"""
Warnings to ignore from the nitpicky = True setting found in the conf.py. Most of these are
undocumented python entities
"""
nitpick_ignore = [
    ('py:class:', 'unittest.case.TestCase'),
]
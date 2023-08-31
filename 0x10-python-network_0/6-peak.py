#!/usr/bin/python3
""" Python script finds a peak in a list of unsorted integers. """

def find_peak(l):
    """
    args: l : list of integers to find peak
    Returns: peak of l
    """
    s = len(l)
    m_e = s
    m = s // 2

    if s == 0:
        return None

    while True:
        m_e = m_e // 2
        if (m < s - 1 and l[m] < l[m + 1]):
            if m_e // 2 == 0:
                m_e = 2
            m = m + m_e // 2
        elif m_e > 0 and l[m] < l[m - 1]:
            if m_e // 2 == 0:
                m_e = 2
            m = m - m_e // 2
        else:
            return l[m]

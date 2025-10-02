# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 17:22:34 2025

@author: fwedyan
"""
from array_stack import ArrayStack


def compute_span_array(prices):
    """
    Computes the span array using a custom Stack class.
    
    Parameters:
    prices (List[int]): List of daily stock prices.
    
    Returns:
    List[int]: Span array.
    """
    span = []
    # Stack stores tuples of (index, price)
    stack = ArrayStack()  

    for i, price in enumerate(prices):
        while not stack.is_empty() and stack.top()[1] <= price:
            stack.pop()

        if stack.is_empty():
            span.append(i + 1)
        else:
            span.append(i - stack.top()[0])

        stack.push((i, price))

    return span

# Example usage
if __name__ == "__main__":
    prices = [100, 80, 60, 70, 60, 75, 85]
    span_array = compute_span_array(prices)
    print("Prices:", prices)
    print("Span array:", span_array)

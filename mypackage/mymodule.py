def top_n(items, n):
    """Return the top n items in array in a descending order
    
    Args:
        items(array):List or array-like object
        n(int): num of items to return
    
    Egs:
        >>> top_n([8,3,2,7,4], 3)
        [8,7,3]
    """
    for i in range(len(items) - 1):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j+1]: # if this item is bigger than the next item...
                items[j], items[j+1] = items[j+1], items[j] # swap the two!
    
    # get last n items in descending order
    return items[-n:][::-1]

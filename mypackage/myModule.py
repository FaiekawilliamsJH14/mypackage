def top_n(items, n):
    """Return the top n items in an array, in desc order.

    Args:
        items (array): list or array - or array-like object
        n (int): num of the items to return

    Return:
        array: top n items, in dec order

    Egs:
        >>>top_n([8, 3, 2, 7, 4], 3)
        [873]
    """
    for i in range(n):  # keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:  # if this item is bigger than next item...
                items[j], items[j+1] = items [j+1], items[j]  # swap the two

        # get last two items
        top_n = items[-n:]

        # return in descending order
        return top_n[::-1]        
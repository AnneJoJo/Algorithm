# You are going on a road trip, and would like to create a suitable music playlist. The trip will require N songs, though you only have M songs downloaded,
# where M < N. A valid playlist should select each song at least once, and guarantee a buffer of B songs between repeats.


def playlist(N,M,B):
    """

    :param N: total songs
    :param M: songs only have
    :param B: buffer for shuffle to prevent repeat case
    :return: the total ways of playlist. use number would be ok
    if b is 0 we could repeat the song any way
    if b is 1, just make sure two same song won't be next each other




    while N >= 0:
        if buffer > 0:
            res.append(one of M) m has be new
            if m still has song add if not repeat old song

            buffer--
        else:
           resize buffer


    """


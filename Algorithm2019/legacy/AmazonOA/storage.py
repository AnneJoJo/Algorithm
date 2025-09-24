def storage_optimization(n: int, m: int, h: List[int], v: List[int]) -> int:
    max_h = 0
    max_w = 0
    h_ptr = 0
    v_ptr = 0
    prev_h = 0
    for hc in range(1, n+2):
        if hc != h[h_ptr]:
            max_h = max(max_h, hc - prev)
            prev = hc
        else:
            if h_ptr < len(h) - 1:
            h_ptr += 1
    prev_w = 0
    for vc in range(1,m+2):
        if vc != v[v_ptr]:
            max_w = max(max_w, vc - prev)
            prev = vc
        else:
            if v_ptr < len(v) - 1:
            v_ptr += 1
    return max_h * max_w
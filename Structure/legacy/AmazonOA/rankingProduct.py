def solution(URLS, sort_column, sort_order, results_per_page, page_index):
    ordered = []
    for item in URLS:
        ordered.append((name,URLS[name][0],URLS[name][1])) 
        ordered.sort(key=lambda x: x[sort_column], reverse=(sort_order == False))
    start_index = results_per_page * page_index
    return [name for name, _, _ in ordered[start_index:start_index + results_per_page]]
        
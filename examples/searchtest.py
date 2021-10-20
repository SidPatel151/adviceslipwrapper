from client import Client

test = Client()

ans = input('enter random query if you want: ')
ans = ans if ans else 'spiders'
res = int(input('enter amount of times you want to search the total results : '))
res = res if res else 1

test.search_times(res, ans)

test.get_all_search(ans) # <- this returns everything in json format




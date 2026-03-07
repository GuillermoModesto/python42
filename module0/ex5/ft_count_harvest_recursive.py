def ft_count_harvest_recursive(days = int(input("Days until harvest: "))):
    def ft_helper(i):
        if (i != 0):
            ft_helper(i - 1)
            print(f"Day {i}")
    ft_helper(days)
    print("Harvest time!")
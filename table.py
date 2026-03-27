from char import hiragana


def show_table():
    print("\nTabla de Hiragana:")
    for n in range(0, 47, 5):
        for pair in hiragana[n : n + 5]:
            print(f"    {pair[0]}/{pair[1]}".ljust(10), end="")
        print()

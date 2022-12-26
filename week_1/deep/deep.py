user = input(
    "What is the Answer to the Great Question of Life, the universe, and Everything? ").strip().upper()

if (user in ['42', 'FORTY-TWO', 'FORTY TWO']):
    print("Yes")
else:
    print("No")

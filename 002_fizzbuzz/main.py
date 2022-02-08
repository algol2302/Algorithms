def fizzbuzz():
    # loop
    for i in range(1, 101):
        fizz = "fizz" * (not i % 3)
        buzz = "buzz" * (not i % 5)
        print(f"{fizz}{buzz}" or i)

    # lambda
    fizz = "fizz"
    buzz = "buzz"
    print(
        *map(
            lambda x: f"{fizz * (not x % 3)}{buzz * (not x % 5)}" or f"{x}",
            range(1, 101),
        ),
        sep="\n",
    )


if __name__ == "__main__":
    fizzbuzz()

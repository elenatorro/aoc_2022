def cleanup():
    file = open('input', 'r')
    lines = file.readlines()
    total = len(
        list(
            filter(
                lambda sections:
                sections[0].issubset(
                    sections[1]) or sections[1].issubset(sections[0]),
                map(
                    lambda sections:
                  (
                      set(range(int(sections[0][0]), int(sections[0][1]) + 1)),
                      set(range(int(sections[1][0]), int(sections[1][1]) + 1))
                  ),
                    map(
                      lambda line:
                      (
                          line[0].split('-'), line[1].split('-')
                      ),
                      map(
                          lambda line:
                          line.split(','),
                          lines)))
            )
        )
    )

    print(f'** Total: {total}')


if __name__ == "__main__":
    cleanup()

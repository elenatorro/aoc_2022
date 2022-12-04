def cleanup():
    total = 0
    file = open('input', 'r')
    lines = file.readlines()
    total = len(
        list(
            filter(
                lambda sections:
                list(sections[0] & sections[1]),
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

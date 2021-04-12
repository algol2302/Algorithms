def convert(s: str, num_rows: int) -> str:
    # TODO brute-force solution:
    pass


def main():
    res_0 = convert(s="PAYPALISHIRING", num_rows=3) == "PAHNAPLSIIGYIR"
    print((
        f'Input: s=PAYPALISHIRING, num_rows=3'
        f'Output PAHNAPLSIIGYIR: {res_0}'
    ))
    print('----------------')
    res_1 = convert(s="PAYPALISHIRING", num_rows=4) == "PINALSIGYAHRPI"
    print((
        f'Input: s=PAYPALISHIRING, num_rows=4'
        f'Output PINALSIGYAHRPI: {res_1}'
    ))
    print('----------------')
    res_2 = convert(s="A", num_rows=1) == "A"
    print((
        f'Input: s=A, num_rows=1'
        f'Output A: {res_2}'
    ))


if __name__ == '__main__':
    main()

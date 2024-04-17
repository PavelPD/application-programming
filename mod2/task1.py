def get_summary_rss(file_path):
    summ = 0
    with open(file_path, 'r') as output_file:
        lines = output_file.readlines()[1:]
        for i_line in lines:
            summ += int(i_line.split()[5])
    bits = summ
    kbits = summ / 1024
    mbits = kbits / 1024
    return f"Объем потребляемой памяти: {bits} B, {round(kbits, 2)} KiB, {round(mbits, 2)} MiB"


if __name__ == '__main__':
    file_path = 'output_file.txt'
    summary_rss: str = get_summary_rss(file_path)
    print(summary_rss)
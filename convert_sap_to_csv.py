import re


def main(file_name):

    file_name_output = file_name.replace(".txt", ".csv")

    with open(file_name, "r") as f:
        lines = f.readlines()
        lines = lines[3:]  # top tree line
        lines = lines[:-1]  # bottom line
        # print(lines)

        with open(file_name_output, "w") as wf:
            # iterate each line
            for number, line in enumerate(lines):
                # remove header first two rows
                if number not in [0, 1]:
                    # Replace last character with empty string
                    line = re.sub(r".$", "", line)
                    line = line.lstrip("|")  # remove first | on the left
                    line = line.replace("|", ";")  # change delimeters
                    wf.write(line)


if __name__ == "__main__":
    pass

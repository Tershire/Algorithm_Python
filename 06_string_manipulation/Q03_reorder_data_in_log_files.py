# Q03_reorder_data_in_log_files.py
# LeetCode #937

# Tershire
# 2023 SEP 26


# KEY TAKEAWAY ****************************************************************
# > lambda

# case ////////////////////////////////////////////////////////////////////////
# logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero", "let0 art can"]
# logs = ["27 85717 7", "2 y xyr fc", "52 314 99", "d 046099 0", "m azv x f", "7e apw c y", "8 hyyq z p", "6 3272401", "c otdk cl", "8 ksif m u"]
logs = ["zoey i love you", "lucas i love you", "rong i love you"]


# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# list of tuples
# 40 [ms]
def f1(logs: list[str]) -> list[str]:
    # separate and collect logs ===============================================
    id_and_texts = []
    digit_logs = []
    for log in logs:
        for i, letter in enumerate(log):
            if letter == " ":
                test_letter = log[i + 1]  # token following the first " "
                if test_letter.isalpha():
                    id_and_texts.append((log[:i], log[i + 1:]))
                else:
                    digit_logs.append(log)
                break

    # reorder letter logs =====================================================
    # criterion #1: by content
    id_and_texts = sorted(id_and_texts, key=lambda item: item[1])
    # print(id_and_texts)

    # criterion #2: by key
    LENGTH = len(id_and_texts)
    sub_id_and_texts = []
    previous_i = 0
    previous_content = ""
    for i, id_and_text in enumerate(id_and_texts):
        current_key = id_and_text[0]
        current_content = id_and_text[1]
        if current_content != previous_content:
            if sub_id_and_texts:  # if not empty, correct the order
                id_and_texts[previous_i:i] = sorted(sub_id_and_texts)
            # update
            previous_i = i
            previous_content = current_content
            sub_id_and_texts = [(current_key, current_content)]
        else:
            sub_id_and_texts.append((current_key, current_content))
            if i == LENGTH - 1 and sub_id_and_texts:  # case: reaches the end
                id_and_texts[previous_i:LENGTH] = sorted(sub_id_and_texts)
    # print(id_and_texts)

    reordered_letter_logs = [id_and_text[0] + " " + id_and_text[1] for id_and_text in id_and_texts]
    # print(reordered_letter_logs)

    # join
    return reordered_letter_logs + digit_logs


# -----------------------------------------------------------------------------
# lambda & +
# 45 [ms]
def f1B(logs: list[str]) -> list[str]:
    letter_logs, digit_logs = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letter_logs + digit_logs


# -----------------------------------------------------------------------------
# me x book
# 45 [ms]
# I was concerned about the split() check since it seemed costly.
# but the result is not so different from f1B. why (?)
def f2(logs: list[str]) -> list[str]:
    letter_logs, digit_logs = [], []
    for log in logs:
        for i, letter in enumerate(log):
            if letter == " ":
                test_letter = log[i + 1]  # token following the first " "
                if test_letter.isalpha():
                    letter_logs.append(log)
                else:
                    digit_logs.append(log)
                break

    letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letter_logs + digit_logs


# test ////////////////////////////////////////////////////////////////////////
print(f1(logs))
print(f1B(logs))
print(f2(logs))
